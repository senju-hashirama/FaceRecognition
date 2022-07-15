import cv2
import face_recognition as fr
import os
from tkinter import Tk,filedialog
from threading import Thread

TOLERANCE = 0.6
kfiles=os.listdir("knownfaces")
kencodings=[]
labels=[]
print("""
   ____             ___                         _ __  _
  / __/__ ________ / _ \___ _______  ___ ____  (_) /_(_)__  ___
 / _// _ `/ __/ -_) , _/ -_) __/ _ \/ _ `/ _ \/ / __/ / _ \/ _ \\
/_/  \_,_/\__/\__/_/|_|\__/\__/\___/\_, /_//_/_/\__/_/\___/_//_/
                                   /___/
                                   
>> Copy images of faces to be detected in a folder called knownfaces in the same
directory as app.py

""")
print("Loading files....")
for i in(kfiles):
    
    file=fr.load_image_file("knownfaces/{}".format(i))
    print("Creating face encoding of {}".format(i))
    kencodings.append(fr.face_encodings(file)[0])
    labels.append(i.split(".")[0])



def recog_image(file):

            img=cv2.imread(file)
            scale_percent = 60
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            face_locations = fr.face_locations(img)
            face_encodings=fr.face_encodings(img,face_locations)


            c=0
            for i in kencodings:
                    lb=labels[c]
                    
                    a=fr.compare_faces(face_encodings,i,TOLERANCE)
                    c=c+1
                    if True in a:

                            top,right,bottom,left=(face_locations[a.index(True)])
                            cv2.rectangle(img,(right,top),(left,bottom),(255,0,0),2)
                            
                            
                            text_size, _ = cv2.getTextSize(lb, cv2.FONT_HERSHEY_TRIPLEX,0.5,1)
                            text_w, text_h = text_size
                            cv2.rectangle(img,(left,bottom),(left+text_w,bottom+text_h+5),(0,255,0),cv2.FILLED)
                            cv2.putText(img,lb,(left,bottom+text_h),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,0),1)    




                            
                            
            cv2.imshow("image",img)

            if cv2.waitKey() & 0xFF==ord("q"):
                        
                        cv2.destroyAllWindows()
                        return



def recog_video():
    a=int(input("""Select input source
1) Webcam
2) File
>> """))
    if a==1:

        video=cv2.VideoCapture(0)
    elif a==2:
        Tk().withdraw()
        file=filedialog.askopenfilename()
        video=cv2.VideoCapture(file)

    while True:
            ret,img=video.read()
            if ret:
                    face_locations = fr.face_locations(img)
                    face_encodings=fr.face_encodings(img,face_locations)
                    c=0
                    for i in kencodings:
                            lb=labels[c]
                            c=c+1
                            a=fr.compare_faces(face_encodings,i,TOLERANCE)
                            if True in a:

                                top,right,bottom,left=(face_locations[a.index(True)])
                                cv2.rectangle(img,(right,top),(left,bottom),(255,0,0),2)
                                text_size, _ = cv2.getTextSize(lb, cv2.FONT_HERSHEY_TRIPLEX,0.5,1)
                                text_w, text_h = text_size
                                cv2.rectangle(img,(left,bottom),(left+text_w,bottom+text_h+5),(0,255,0),cv2.FILLED)
                                cv2.putText(img,lb,(left,bottom+text_h),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,0),1)    

                                
                            else:
                                pass


                    cv2.imshow("image",img)
                    if cv2.waitKey(1) & 0xFF==ord("q"):
                        
                        cv2.destroyAllWindows()
                        break


while True:

        a=int(input("""
Detect face in:

1) Image
2) Video

3) Quit
>> """))

        if a==1:
            Tk().withdraw()
            file=filedialog.askopenfilename()
            recog_image(file)
        elif a==2:
            recog_video()
        elif a==3:
            break
        else:
            print("invalid option")
