# import requests
# url = 'https://api.deepai.org/api/nsfw-detector'
# headers = {
#     'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'
# }
# response = requests.post(
#     url,
#     files={
#         'image': open('./img/image2.jpeg', 'rb'),
#     },
#     headers=headers
# )
# print(response.text)

from nudenet import NudeClassifier
import cv2

nude = NudeClassifier()

img2 = cv2.imread('./img/image2.jpeg')
img = cv2.imread('./img/image.jpeg')
# nude.classify(img2)
# nude.classify(img)
obj = {
    'img2': nude.classify(img2)[0],
    'img': nude.classify(img)[0]
}

print(obj)
