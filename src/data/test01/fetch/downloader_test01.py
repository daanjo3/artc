import zipfile, urllib.request, shutil

RESOURCE_URL = "https://labs.brill.com/ictestset/data.zip"
TARGET_LOC = "resource/data.zip"


def main():
    with urllib.request.urlopen(RESOURCE_URL) as response, open(TARGET_LOC, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        with zipfile.ZipFile(file_name) as zf:
            zf.extractall()

if __name__ == "__main__":
    main()