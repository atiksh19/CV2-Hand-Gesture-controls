""" necessary imports """
import cv2
import keyboard
import time
import handTracker as htm

######################################

""" setting the dimensions """
camW, camH = 640, 480
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, camW)
cap.set(4, camH)

pTime = 0
trckr = htm.handTrack(detConf=0.7)

######################################
def gesture(lndmrks):
	#checking if each finger is open or closed
	thumb = True if (lndmrks[4][1] > lndmrks[3][1]) else False
	index = True if (lndmrks[8][2] < lndmrks[6][2]) else False
	middle = True if (lndmrks[12][2] < lndmrks[10][2]) else False
	ring = True if (lndmrks[16][2] < lndmrks[14][2]) else False
	pinky = True if (lndmrks[20][2] < lndmrks[18][2]) else False
	#detecting gestures
	if(thumb and not index and not middle and not ring and not pinky):
		print("left")
	if(not thumb and not index and not middle and not ring and pinky):
		print("right")

######################################

""" constant loop """
while True:
	#setting the exit key
	if keyboard.is_pressed('q'):
		break
	#reading the image
	success, img = cap.read()
	#hand tracking
	img = trckr.findHands(img)
	lmList = trckr.findPosition(img)
	if(len(lmList) != 0):
		gesture(lmList)

	#calculating the fps
	cTime = time.time()
	fps = 1/(cTime - pTime)
	pTime = cTime

	#printing fps to screen
	cv2.putText(img, f'FPS: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
	#streaming
	cv2.imshow("Img", img)
	#delay 1 millisecond
	cv2.waitKey(1)

######################################