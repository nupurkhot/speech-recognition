# speech-recognition

**Speech recognition using Spectrograms**
Spectrogram is a plot of spectrum of frequencies present in a signal with respect to time. The signal strength is represented by the pixel intensity in the spectrogram. 
Convolutional neural network (CNN) can be used to classify the audio signals based on the information present in the spectrograms. 

**Data**
Dataset used in this project for training and validation of the CNN model is spoken digit dataset that is freely available on internet. It comprises of audio recordings from 4 different speakers. There are 500 recordings of each speaker with 50 recordings of each digit (0-9). The audio format is wave-file and the sampling rate is 8 kHz. Dataset was extended by adding the audio recordings of 4 new participants. The new custom dataset created is added in the data directory.

![image](https://user-images.githubusercontent.com/116115824/211112010-f2443144-91bf-42d3-aee7-f971c256fe84.png)
![image](https://user-images.githubusercontent.com/116115824/211112021-ab8a36a5-e376-400f-90b4-6da0cf7a2af1.png)

**Training**

![image](https://user-images.githubusercontent.com/116115824/211112083-9fb7d720-bd12-4d38-8d55-c9c21776bc31.png)
![image](https://user-images.githubusercontent.com/116115824/211112091-a6f087b2-e00e-4b05-b16e-285d54590ae7.png)
