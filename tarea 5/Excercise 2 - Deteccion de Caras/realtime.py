import cv2
 
face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
 
 # Detects faces of different sizes in the input image
while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 2) 
    

    for (x,y,w,h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

        eyes = eye_cascade.detectMultiScale(img, scaleFactor = 1.2, minNeighbors = 4)
            
        for (x,y,w,h) in eyes:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0, 255, 0),5)
        
    cv2.imshow('img',img)

    k = cv2.waitKey(25)
    if k == 27:
       break

# Close the window
cap.release()
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
