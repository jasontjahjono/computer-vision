import cv2

img = cv2.imread("../DATA/00-puppy.jpg")

while True:
    cv2.imshow("Puppy", img)
    
    # if we waited at least 1 ms AND we've pressed a key Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()