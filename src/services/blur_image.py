import cv2 # type: ignore
from typing import List
import base64
import sys
from PIL import Image

def apply_gaussian_blur(images: List[str], kernel_size: int) -> List[str]:
    blurred_images = []

    for img in images:
        blurred_img = cv2.GaussianBlur(img, (kernel_size,kernel_size), cv2.BORDER_DEFAULT)

        # if faces:
        #     for (x, y, w, h) in faces[0]:
        #         face_region = img[y:y+h, x:x+w]
        #         blurred_face = cv2.GaussianBlur(face_region, (kernel_size, kernel_size), cv2.BORDER_DEFAULT)
        #         img[y:y+h, x:x+w] = blurred_face
        # else:
        #     img = cv2.GaussianBlur(img, (kernel_size, kernel_size), cv2.BORDER_DEFAULT)

        retval, buffer = cv2.imencode(".jpg", blurred_img)
        if not retval:
            raise ValueError("Error encoding image to JPEG")

        base_string = base64.b64encode(buffer).decode('utf-8')
        blurred_images.append(base_string)

    return blurred_images
