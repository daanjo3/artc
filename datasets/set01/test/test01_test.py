from datasets.set01 import Reader, DIRECTORY_PATH, INDEX_PATH

reader = Reader(DIRECTORY_PATH, INDEX_PATH, leveled=False)

for obj in iter(reader):
    print(obj)