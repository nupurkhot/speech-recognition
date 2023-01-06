import os
from shutil import copyfile

def separate(source,train):
	for filename in os.listdir(source):
		#filename = os.listdir(source)[0]
		label = filename.rsplit("_")[0]
		#print (filename)
	    #print (label)
		if train:
			copyfile(source + "/" + filename, "/home/speech-recognition/data/train-spectrograms" + "/" + str(label) + "/" + filename)
		else:
			copyfile(source + "/" + filename, "/home/speech-recognition/data/test-spectrograms" + "/" + str(label) + "/" + filename)

if __name__ == '__main__':
	separate("/home/speech-recognition/data/training-spectrograms",1)
	separate("/home/speech-recognition/data/testing-spectrograms",0)