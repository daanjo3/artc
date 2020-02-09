# ArtC
## *The Iconclass art classifier, a convolutional neural network.*

### Installation
1. Create the virtual environment `virtualenv -p python3 artc-py3-env`
1. Run the virtual environment `venv artc-py3-env/bin/active`
2. Install tensorflow if not yet present `pip install tensorflow`


### Directory structure
```
artc-py3-env/
resource/data/   <-- test set
            | *.jpg   <-- test image
            | data.json   <-- dataset index
src/
    | main.py  <-- program entry point
    | data/
        | loader/    <-- runtime dataset loader
        | sets/    <-- data set downloader
```