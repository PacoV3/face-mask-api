from tensorflow import get_logger
import logging
get_logger().setLevel(logging.ERROR)
  
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
class MaskRecon:
    def __init__(self, model_location):
        self.thermal_model = load_model(model_location)
    
    def get_mask(self, image):
        predict_image = cv2.resize(image, (224, 224))
        predict_image = img_to_array(image)
        predict_image = preprocess_input(predict_image)
        prediction = self.thermal_model.predict(np.expand_dims(predict_image, axis=0))[0]
        return prediction

