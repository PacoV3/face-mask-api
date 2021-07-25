from tensorflow import get_logger
import logging
get_logger().setLevel(logging.ERROR)
  
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2


class ThermalRecon:
    def __init__(self, model_location):
        self.thermal_model = load_model(model_location)

    def get_mask_p(self, image):
        predict_img = cv2.resize(image, (224, 224))
        predict_img = img_to_array(predict_img)
        predict_img = preprocess_input(predict_img)
        prediction = self.thermal_model.predict(np.expand_dims(predict_img, axis=0))[0]
        return prediction

def main():
    mask_recon = ThermalRecon(model_location="thermal_mask_detector.model")
    image = cv2.imread("examples/mask1.jpg")
    h, w = image.shape[:2]
    start_X, start_y = 10, 0
    end_X, end_y = w - 11, h - 1
    mask, no_mask = mask_recon.get_mask_p(image[start_y:end_y, start_X:end_X])
    print(f'Mask: {mask:0.2f}, No Mask: {no_mask:0.2f}')


if __name__ == "__main__":
    main()