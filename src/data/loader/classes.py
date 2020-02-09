import json
import itertools
from threading import Thread

class DataObject():
    name = ""
    path = ""
    iconclasses = []

    def __init__(self, name, path, iconclasses):
        self.name = name
        self.path = path
        self.iconclasses = iconclasses
    
    def __str__(self):
        return "-" * 40 + "\nname: {}\npath: {}\nclasses: {}".format(self.name, self.path, self.iconclasses)

def n_iconclass_divider(iconclasses):
    return [iconclass_divider(ic) for ic in iconclasses]

# Divides the iconclasses to their hierarchy, ex. A11 -> [A, A1, A11]
# Weird input such as ':', '(', or names are ignored
def iconclass_divider(iconclass):
    iconclasses = []
    current = ""

    if iconclass == None or iconclass == "":
        return []
    if not iconclass[0].isdigit:
        return []
    
    for ic in iconclass:
        if ic == ':' or ic == '(':
            return iconclasses
        current += ic
        iconclasses.append(current)
    return iconclasses


# Reader class which exposes the test01 dataset
class Test01Reader():
    # Location of the data
    directory_loc = ""
    # Location of the index file
    index_loc = ""

    # Last index element visited
    last = ""

    def __init__(self, directory_loc, index_loc):
        self.directory_loc = directory_loc
        self.index_loc = index_loc

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
                return DataObject(fn, self.directory_loc + fn, n_iconclass_divider(classes))
            if found_last:
                self.last = fn
                return DataObject(fn, self.directory_loc + fn, n_iconclass_divider(classes))
            if self.last == fn:
                found_last = True
        
        raise StopIteration


# Loader class that loads the data from a seperate thread
class Loader(Thread):
    reader = None

    def __init__(self, reader):
        super().__init__()
        self.reader = reader

    def run(self):
        pass
        # for obj in reader: