import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

def drawBox(img, bbox):
    
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    
    
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    if success:
       
        cv2.putText(img, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    else:
        
        cv2.putText(img, "LOST", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Initialize the video capture object
cap = cv2.VideoCapture("footvolleyball.mp4")


tracker = cv2.TrackerCSRT_create()


ret, img = cap.read()


bbox = cv2.selectROI("Select Object to Track", img, fromCenter=False, showCrosshair=True)


tracker.init(img, bbox)

while True:
    
    ret, img = cap.read()
    
    
    if not ret:
        break

   
    success, bbox = tracker.update(img)
    
    
    drawBox(img, bbox)

   
    cv2.imshow("Object Tracking", img)
    
    key = cv2.waitKey(25)
    if key == 32:
        print("Stopped!")
        break


cap.release()
cv2.destroyAllWindows()
