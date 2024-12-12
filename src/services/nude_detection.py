from typing import List
from nudenet import NudeClassifier

# initialize classifier (downloads the checkpoint file automatically the first time)
nude = NudeClassifier()


def detect_nudity(image_paths: List[str]):
    # Import module
    data = []
    for image_path in image_paths:
        prob = nude.classify(image_path)
        data.append(list(prob.values())[0])
        print(data)

    return data
