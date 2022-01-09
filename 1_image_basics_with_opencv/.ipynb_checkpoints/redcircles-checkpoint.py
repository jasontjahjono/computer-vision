import cv2
import numpy as np

img = cv2.imread("../DATA/dog_backpack.jpg")

def drawCircles(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0,0,255), 10)

cv2.namedWindow(winname="results")
cv2.setMouseCallback("results", drawCircles)
        
while True:
    cv2.imshow("results", img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

