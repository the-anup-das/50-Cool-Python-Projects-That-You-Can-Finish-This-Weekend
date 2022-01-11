import cv2
import numpy as np
import sys
import time


vid = cv2.VideoCapture("http://192.168.0.100:8080/video")
ret, inputImage = vid.read()
# inputImage = cv2.imread("qrcode.jpg")
# while(True):
      
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
#     resized = cv2.resize(frame,(600,400))
#     # Display the resulting frame
#     cv2.imshow('frame', resized)
      
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break
#inputImage = cv2.imread("http://192.168.0.100:8080/photo.jpg")


# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        #cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)
        cv2.line(im, (0,int(10.1)), (100,100),(0,0,255),2)

    # Display results
    cv2.imshow("Results", im)

qrDecoder = cv2.QRCodeDetector()

# Detect and decode the qrcode
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
if len(data)>0:
    print("Decoded Data : {}".format(data))
    display(inputImage, bbox)
    rectifiedImage = np.uint8(rectifiedImage);
    cv2.imshow("Rectified QRCode", rectifiedImage);
else:
    print("QR Code not detected")
    cv2.imshow("Results", inputImage)

cv2.waitKey(0)
cv2.destroyAllWindows()