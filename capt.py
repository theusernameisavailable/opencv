import io
import cv2

#start video capture from web-cam
vc = cv2.VideoCapture(0)

#import Haar cascade
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')

#read frame from video capture
rval, frame = vc.read()

while True:
    if frame is not None:
        #convert frame to gray grades
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #detect faces in frame
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        print "Found "+str(len(faces))+" face(s)"

        #add borders of faces in frame
        for (x,y,w,h) in faces:
            cv2.rectangle(gray, (x,y),(x+w,y+h),(255,255,0),2)

        #show frame after detection
        cv2.imshow('preview',gray)

    #repeat reading frames
    rval, frame = vc.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
