# evernote-to-notion

A simple python code that convert your evernote to notion.so **with all the images displayed**.

## Requirement

- Python >= 3.6.0 (Only for f-strings, which can be modified in earlier Python versions.)
- `requirements.txt`

## Installation

1. Install Python and pip.
2. Git clone or download this repo.
3. Open cmd/terminal and install required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Export your evernote to a `html` file in the same path as `convert.py`.
2. Open cmd/terminal and run
    ```
    python convert.py yourfile.html
    ```
    When the process finished, you'll see a file named `yourfile_output.html` in the path. 
    
    If you want to customize the output file name, run
    ```
    python convert.py yourfile.html -o some_customized_name.html
    ```
3. Open notion.so and directly import `yourfile_output.html`.
4. You'll see your evernote imported **with the images**. Enjoy:)


## Others

Thanks for the free image-uploading site sm.ms!

Note: sm.ms API may restrict the frequency of uploading images - please be patient. If there are TOO MANY images (eg. >50), I suggest you to build an OSS instead of using sm.ms. (You can just modify the uploading part if you do so.)


