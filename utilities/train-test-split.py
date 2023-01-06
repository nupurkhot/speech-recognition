import os
from shutil import copyfile


def separate(source):
    for filename in os.listdir(source):
        first_split = filename.rsplit("_", 1)[1]
        second_split = first_split.rsplit(".", 1)[0]
        if int(second_split) <= 4:
            copyfile(source + "/" + filename, "/home/speech-recognition/data/testing-spectrograms" + "/" + filename)
        else:
            copyfile(source + "/" + filename, "/home/speech_recognition/data/training-spectrograms" + "/" + filename)

if __name__ == '__main__':
    separate("/home/speech-recognition/data/spectrograms")