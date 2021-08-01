from flask_restful import Resource, Api, reqparse
from mask_recon import MaskRecon
from flask import Flask
import numpy as np
import werkzeug
import cv2

mask_recon = MaskRecon(thermal_model_location="thermal_mask_detector.model",
                          rgb_model_location="mask_detector.model")
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument("files", type=werkzeug.datastructures.FileStorage,
                    location="files", action="append")


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


class ThermalModel(Resource):
    def post(self):
        data = parser.parse_args()
        if data["files"] == "":
            return {"data": [], "message": "No file sent", "status": "error"}
        photos = data["files"]
        # print(data)
        results = []
        if photos:
            for photo in photos:
                filestr = photo.read()
                # print(photo.filename)
                npimg = np.fromstring(filestr, np.uint8)
                image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
                mask, no_mask = mask_recon.get_mask_p(image, thermal=True)
                results.append(
                    {'mask': float(mask), 'no_mask': float(no_mask)})
            return {"data": results, "message": "Photos uploaded successfully", "status": "success"}
        return {"data": [], "message": "Something went wrong!", "status": "error"}


class MaskModel(Resource):
    def post(self):
        data = parser.parse_args()
        if data["files"] == "":
            return {"data": [], "message": "No file sent", "status": "error"}
        photos = data["files"]
        results = []
        if photos:
            for photo in photos:
                filestr = photo.read()
                npimg = np.fromstring(filestr, np.uint8)
                image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
                mask, no_mask = mask_recon.get_mask_p(image, thermal=False)
                results.append(
                    {'mask': float(mask), 'no_mask': float(no_mask)})
            return {"data": results, "message": "Photos uploaded successfully", "status": "success"}
        return {"data": [], "message": "Something went wrong!", "status": "error"}


api.add_resource(HelloWorld, "/")
api.add_resource(ThermalModel, "/thermal_model")
api.add_resource(MaskModel, "/mask_model")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
