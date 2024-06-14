from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


class Classifier:
    def __init__(self):
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        print("Loading model...")
        self.model = load_model("models/keras_Model.h5", compile=False)

        print("Loading labels...")
        self.class_names = open("models/labels.txt", "r").readlines()

    def inference(self, path: str):
        print("running inference on image: ", path)

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Replace this with the path to your image
        image = Image.open(path).convert("RGB")

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # Predicts the model
        prediction = self.model.predict(data)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]

        print("Class:", class_name[2:], end="")
        print("Confidence Score:", confidence_score)

        return class_name[2:], confidence_score
