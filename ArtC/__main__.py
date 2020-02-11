import numpy as np

from ArtC import config
from ArtC.neural import network

def main():
    config.init()

    print("Retrieving training data...")
    # TODO add loader here

    # Prepare labels
    # TODO add label loader here

    # labels = list()
    # for data in training_data:
    #     for label in data['ic']:
    #         if label not in labels:
    #             labels.append(label)

    # for data in training_data:
    #     containedlabels = list()
    #     for label in labels:
    #         if label in data['ic']:
    #             containedlabels.append(1.0)
    #         else:
    #             containedlabels.append(0.0)
    #     data['ic'] = containedlabels

    print("Building network...")
    config.neuralnet = network.get_network(256, len(labels))
    config.labels = labels

    training_input = []
    training_output = []

    for data in training_data:
        training_input.append(data['img'])
        training_output.append(data['ic'])

    print("Training network...")
    history = network.train(config.neuralnet, np.array(training_input), np.array(training_output))
    print("Done, ready for predictions")

    # TODO put this method in a thread and allow asynchronous sending of test data

if __name__ == "__main__":
    main()