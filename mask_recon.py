from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2


class MaskRecon:
    def __init__(self, thermal_model_location, rgb_model_location):
        self.thermal_model = load_model(thermal_model_location)
        self.rgb_model = load_model(rgb_model_location)

    def get_mask_p(self, image, thermal):
        predict_img = cv2.resize(image, (224, 224)) if thermal else image
        predict_img = img_to_array(predict_img)
        predict_img = preprocess_input(predict_img)
        predict_img = np.expand_dims(predict_img, axis=0)
        prediction = self.thermal_model.predict(predict_img) if thermal else self.rgb_model.predict(predict_img)
        return prediction[0]


def main():
    mask_recon = MaskRecon(thermal_model_location="thermal_mask_detector.model",
                          rgb_model_location="mask_detector.model")
    image = cv2.imread("examples/mask_color1.jpg")
    h, w = image.shape[:2]
    start_X, start_y = 10, 0
    end_X, end_y = w - 11, h - 1
    mask, no_mask = mask_recon.get_mask_p(image[start_y:end_y, start_X:end_X], thermal=True)
    print(f'Mask: {mask:0.2f}, No Mask: {no_mask:0.2f}')


if __name__ == "__main__":
    main()
