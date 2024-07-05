import cv2
from pyzbar.pyzbar import decode 

def BarcodeReader(image): 
	
	# Decode the barcode image 
	detectedBarcodes = decode(image) 
	
	# If not detected then print the message 
	if not detectedBarcodes: 
		return False
	else:

		for barcode in detectedBarcodes: 
			
			# Locate the barcode position in image 
			(x, y, w, h) = barcode.rect 
			
			# Put the rectangle in image using 
			# cv2 to highlight the barcode 
			cv2.rectangle(image, (x-10, y-10), 
						(x + w+10, y + h+10), 
						(255, 0, 0), 2) 
			
			if barcode.data!="": 
			
			# Print the barcode data
				print(barcode.data) 
				print(barcode.type)
				return  barcode.data, barcode.type


cam = cv2.VideoCapture(0)

cv2.namedWindow("التحضير")

image_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("التحضير", frame)
    
    if BarcodeReader(frame) != False:
        barcodeData, barcodeType = BarcodeReader(frame)
        cam.release()


    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
cam.release()

cv2.destroyAllWindows()
