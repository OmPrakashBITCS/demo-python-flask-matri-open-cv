import os
from better_profanity import profanity


def detect_badWords(text:str):
    # Load Data from personal file
    addPersonalSensors()

    # check if the text contains bad words
    isBadWords = profanity.contains_profanity(text)
    censerBadWord = ''
    if(isBadWords):
        censerBadWord = profanity.censor(text)
        return {
            "isBadWords": isBadWords,
            "censerBadWord": censerBadWord,
            "originalText": text
        }
    return {
        "isBadWords": isBadWords,
    }

def addPersonalSensors():
    folder_path = 'src/language'

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'r') as file:
            data = file.read()
            profanity.add_censor_words(data.splitlines())
