# FaceRecognition
Simple Face Recognition application using FaceRecognition module.
The program can detect faces in an image,video file or a live video from webcam

The FaceRecognition module uses dlib’s state-of-the-art face recognition
built with deep learning.The model has an accuracy of 99.38% on the
Labeled Faces in the Wild benchmark.

# Limitations
The face recognition model is trained on adults and does not work very well on children. It tends to mix up children quite easy using the default comparison threshold of 0.6



# Installation 
1) Download app.py and requirements.txt
2) Run "pip install -r requirements.txt"
2) Create a directory called knownface in the same directory as app.py
3) Run app.py

# !!Caution!!
> Install dlib before running requirements.txt file.
> If you are running python 3.9 I have included the .whl file for dlib .
> Download it and run pip install dlib.whl
> If you are running a different version of python then look for the .whl file in GitHub and install it.

# Screenshots

![image](https://user-images.githubusercontent.com/85382114/179285762-b00c01db-8397-49f6-8a03-637058e5acf0.png)




![image](https://user-images.githubusercontent.com/85382114/179285825-05b64699-c653-4cbf-a5b0-5fda4236e059.png)




![image](https://user-images.githubusercontent.com/85382114/179286004-4e556c95-1d16-41f9-8cab-28bdcc9ac4a8.png)
