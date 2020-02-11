import tensorflow as tf
import numpy as np
import json

def get_network(input_size, output_size):
    opt = tf.keras.optimizers.Adam(learning_rate=0.1)
    graph = tf.keras.Sequential([
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(input_size, input_size, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.Dense(output_size)
    ])

    graph.compile(
        optimizer=opt,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return graph

def train(input_network, training_input, training_output):
    scaled_input = training_input / 255
    scaled_input -= np.min(scaled_input)
    scaled_input /= np.max(scaled_input)

    return input_network.fit(scaled_input, training_output, 32, 1)

def make_prediction(input_network, image):
    np_image = np.array(image) / 255
    np_image -= np.min(np_image)
    np_image /= np.max(np_image)

    predictions = input_network.predict(np.array([np_image]))[0]
    predictions -= np.min(predictions)
    predictions /= np.max(predictions)

    to_return = []
    for i in range(len(predictions)):
        if predictions[i] > 0.75:
            to_return.append(config.labels[i])

    print(to_return)
    return json.dumps(to_return)