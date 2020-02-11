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


# Loader class that loads the data from a seperate thread
class Loader(Thread):
    reader = None

    def __init__(self, reader):
        super().__init__()
        self.reader = reader

    def run(self):
        pass
        # for obj in reader: