import json
import itertools
from ArtC.loader import DataObject

DIRECTORY_PATH = "datasets/set01/data/"
INDEX_PATH = DIRECTORY_PATH + "data.json"

# Reader class which exposes the test01 dataset
class Reader():
    # Location of the data
    directory_loc = ""
    # Location of the index file
    index_loc = ""

    # Last index element visited
    last = ""
    leveled = True

    def __init__(self, directory_loc, index_loc, leveled=True):
        self.directory_loc = directory_loc
        self.index_loc = index_loc
        self.leveled = leveled

    def __iter__(self):
        return self

    # Iterating method (TODO improve so the file is not always read top-down for each iteration)
    def __next__(self):
        # TODO load once on init
        with open(self.index_loc, "r") as f:
            index = json.load(f)
        
        found_last = False

        # TODO remove used list items instead, remember position
        for fn, classes in index.items():
            if self.last == "":
                self.last = fn
                return DataObject(fn, self.directory_loc + fn, n_iconclass_divider(classes, leveled=self.leveled))
            if found_last:
                self.last = fn
                return DataObject(fn, self.directory_loc + fn, n_iconclass_divider(classes, leveled=self.leveled))
            if self.last == fn:
                found_last = True
        
        raise StopIteration

def n_iconclass_divider(iconclasses, leveled=True):
    return list(set([iconclass_divider(ic, leveled=leveled) for ic in iconclasses]))

# Divides the iconclasses to their hierarchy, ex. A11 -> [A, A1, A11]
# Weird input such as ':', '(', or names are ignored
def iconclass_divider(iconclass, leveled=True):
    iconclasses = []
    current = ""

    if iconclass == None or iconclass == "":
        return [] if leveled else ""
    if not iconclass[0].isdigit:
        return [] if leveled else ""
    
    for ic in iconclass:
        if ic == ':' or ic == '(':
            return iconclasses if leveled else current
        current += ic
        iconclasses.append(current)
    
    if leveled:
        return iconclasses
    return current