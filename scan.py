# А вот это бот
# Он умеет находить qr коды на фотке, правда, у него не всегда получается

import cv2
import sys


if len(sys.argv)>1:
    inputImage = cv2.imread(sys.argv[1])
else:
    inputImage = cv2.imread('filename')
qrDecoder = cv2.QRCodeDetector()
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
if len(data)>0:
    print("Decoded Data : {}".format(data))
else:
    print("QR Code not detected")
