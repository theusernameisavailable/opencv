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
        #detect faces in frame
        faces = face_cascade.detectMultiScale(frame, 1.1, 5)
        print "Found "+str(len(faces))+" face(s)"

        #add borders of faces in frame
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

        #show frame after detection
        cv2.imshow('preview',frame)

    #repeat reading frames
    rval, frame = vc.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
