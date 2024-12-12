import os
from flask import request
from flask_restful import Resource
import urllib.request
import cv2
import numpy as np
from typing import List
from datetime import date
import json

from src.services.face_detection import detect_face
from src.services.nude_detection import detect_nudity
from src.services.blur_image import apply_gaussian_blur
from src.services.badWord_detection import detect_badWords

class AppController(Resource):
    def get(self, subpath):
        if subpath == 'version':
            return self.get_version()
        elif subpath == 'hello':
            return self.get_local_file_value()
        else:
            return {"error": "Invalid request data. URL not found."}, 400

    def post(self, subpath):
        if subpath == 'nudity':
            return self.detect_nudity()
        if subpath == 'blur':
            return self.get_blur_image();
        if subpath == 'proficiency':
            return self.is_contain_bad_words()
        else:
            return {"error": "Invalid request data. URL not found."}, 400


    def detect_nudity(self):
        img = self.__get_image_from_request()
        total_faces = detect_face([img])
        nudities = detect_nudity([img])

        '''
            Return Type for Nudity Detection:
            data = {
                "total_faces": Array of number [[5],[1]] # If there are multiple images, the number of faces will be an array of numbers.
                "nudities": Array of number [
                                                [
                                                    {
                                                        "unsafe": 0.010312849655747414,
                                                        "safe": 0.9896871447563171
                                                    }
                                                ]
                                                [
                                                    {
                                                        "unsafe": 0.010312849655747414,
                                                        "safe": 0.9896871447563171
                                                    }
                                                ]
                                            ] # If there are multiple images, the nudity will be an array of numbers as shown.
            }
        '''
        return {
            "data": {
                "total_faces": total_faces,
                "nudities": nudities
            }
        }
    
    def get_blur_image(self):
        img = self.__get_image_from_request()
        kernel_size = 15
        try:
            if request.files:
                if 'blur' in request.form:
                    kernel_size = int(request.form['blur'])
            elif request.is_json: 
                data = request.get_json()
                if 'blur' in data:
                    kernel_size = int(data['blur'])

            if kernel_size % 2 == 0:
                kernel_size += 1

        except ValueError:
            return {"error": "Invalid kernel size. Must be an integer."}, 400

        
        blurred_image = apply_gaussian_blur([img], kernel_size)

        '''
            Return Type for Blur Image:
            data = {
                "blurred_image": Array of string ["base64_string","base64_string"] # If there are multiple images, the blurred image will be an array of strings as shown.
                "kernel_size": 15 # If the kernel size is not provided, the default value will be 15.
            }
        '''

        return {
            "blurred_image" : blurred_image,
            "kernel_size": kernel_size
        }
    
    def is_contain_bad_words(self):
        data = json.loads(request.get_data())
        text = data['text']

        '''
            Return Type for Bad Word Detection:
            if the text contains bad words, return:
                {
                    "isBadWords": true,
                    "censerBadWord": "this is **** bad word",
                    "originalText": "this is fucking bad word"
                }
            else:
                {
                    "isBadWords": false,
                }
        '''

        return detect_badWords(text)
    
    def get_local_file_value(self):
        img1 = os.path.join(os.getcwd(), "img/image.jpeg")
        img2 = os.path.join(os.getcwd(), "img/image2.jpeg")

        total_faces = []
        nudities = [] 
        
        for path in [img1, img2]:
            img = cv2.imread(path)
            total_faces.append(detect_face([img]))
            nudities.append(detect_nudity([img]))

        return {
            "data": {
                "total_faces": total_faces,
                "nudities": nudities
            }
        } 
    
    def get_version(self):
        return {
            "version": "1.0.5",
            'date': date.today().strftime("%Y-%m-%d")
        }
    
    #Private Functions
    def __get_image_from_request(self):
        img = np.ndarray([])
        if request.files and 'file' in request.files:
            file = request.files['file']
            img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

        elif request.json and 'url' in request.json:
            img_url = request.json['url']
            if not img_url.startswith("https://") or img_url.startswith("http://"):
                return {"error": "Invalid request data. URL not found."}, 400

            img_data = urllib.request.urlopen(img_url).read()
            img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
        
        return img