import json

DATA_INDEX_FILE_PATH = "resource/data/data.json"

with open(DATA_INDEX_FILE_PATH) as f:
    data = json.load(f)

# Distribution of top-level IconClasses.
distribution = {}

n_empty_items = 0
empty_items = []
unrecognized_items = []

# Loop over all descriptions and parse the IconClasses.
for fn, classes in data.items():
    for iclass in classes:

        # Skip this item if the class is an empty string
        if iclass == None or iclass == "":
            n_empty_items += 1
            empty_items += [str(fn) + ":\t" + json.dumps(classes)]
            continue

        # Skip this item if it doesn't start with a digit
        if not iclass[0].isdigit():
            unrecognized_items += [str(fn) + ":\t" + json.dumps(classes)]
            continue

        # Count the first number (top-level class) for the distribution
        num = iclass[0]
        if num not in distribution.keys():
            distribution[num] = 0
        distribution[num] += 1

print "Result:"
print(json.dumps(distribution, indent=4, sort_keys=True))
print "Number of empty list items: " + str(n_empty_items)
print "Unrecognized list items:"
for item in unrecognized_items:
    print item

# Questions coming forward from this set:
# x
#