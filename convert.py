from bs4 import BeautifulSoup
from urllib.parse import urlparse
from tqdm import tqdm
import os, argparse
import requests
import time

def convert_html(input_file, output_file):
    f = open(input_file, encoding='utf8')
    soup = BeautifulSoup(f, 'lxml')
    imgs = soup.find_all('img')
    print(f'images: {len(imgs)}')

    for img in tqdm(imgs, ascii=True, leave=False):
        src = img.get('src')
        data_filename = img.get('data-filename')
        # print(data_filename)

        url = 'https://sm.ms/api/upload'

        with open(src, 'rb') as fp:
            response = requests.post(url, files={'smfile': fp}).json()

        if response['code'] == 'error':
            print(response['msg'])
            print('Retrying in 10 seconds...')
            time.sleep(10)
            with open(src, 'rb') as fp:
                response = requests.post(url, files={'smfile': fp}).json()
            # print(response)

        new_src = response['data']['url']

        img['src'] = new_src
        img['data-filename'] = urlparse(new_src).path.split('/')[-1]


    with open(output_file, 'w', encoding='utf8') as f:
        f.write(soup.prettify())
    
    print(f'output: {output_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input file')
    parser.add_argument('-o', nargs=1, type=str, help='output file')

    args = parser.parse_args()

    input_file = args.input
    if not args.o:
        output_file = os.path.basename(input_file).split('.')[0] + '_output.html'

    convert_html(input_file, output_file)
