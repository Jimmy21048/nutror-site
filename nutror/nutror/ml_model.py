import tensorflow as tf
import keras
import numpy as np
# from tensorflow import keras
# from keras.applications import EfficientNetB0, preprocess_input
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.utils import load_img, img_to_array


# Load the pre-trained model
model = keras.applications.EfficientNetB0(weights="imagenet")

def predict_image(img_path):
    """Load an image and make a prediction."""
    img = keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = keras.applications.efficientnet.preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded_predictions = keras.applications.efficientnet.decode_predictions(predictions, top=1)[0]

    return decoded_predictions