import cv2
 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("elon.jpg")
 
ret, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Detects faces of different sizes in the input image
faces = face_cascade.detectMultiScale(gray, 1.3, 2)

cv2.imshow('img',img)
k = cv2.waitKey(0)
 
# Close the window
cap.release()
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
