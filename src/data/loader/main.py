from classes import Test01Reader, DataObject

DIRECTORY_PATH = "resource/data/"
INDEX_PATH = "resource/data/data.json"

reader = Test01Reader(DIRECTORY_PATH, INDEX_PATH)

for obj in iter(reader):
    print(obj)