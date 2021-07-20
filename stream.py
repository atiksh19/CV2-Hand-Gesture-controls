""" necessary imports """
import math
import cv2
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput.mouse import Controller as mouseController
import time
import handTracker as htm

######################################

""" setting the dimensions """
camW, camH = 640, 360
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, camW)
cap.set(4, camH)

pTime = 0
trckr = htm.handTrack(detConf=0.9)
kboard = Controller()
mouse = mouseController()

######################################

pasted = 0
space = 0
switchedA = 0
switchedB = 0
minim = 0
maxim = 0
clicked = 0

def gesture(lndmrks):
	global pasted, space, switchedA, switchedB, minim, maxim, clicked
	#checking if each finger is open or closed
	thumb = True if (lndmrks[4][1] > lndmrks[3][1]) else False
	index = True if (lndmrks[8][2] < lndmrks[6][2]) else False
	middle = True if (lndmrks[12][2] < lndmrks[10][2]) else False
	ring = True if (lndmrks[16][2] < lndmrks[14][2]) else False
	pinky = True if (lndmrks[20][2] < lndmrks[18][2]) else False
	""" detecting gestures """
	#all fingers open 
	if(thumb and index and middle and ring and pinky):
		pasted = 0
		space = 0
		switchedA = 0
		switchedB = 0
		minim = 0
		maxim = 0
		clicked = 0
	#index finger open
	if(not thumb and index and not middle and not ring and not pinky):
		if space == 2:
			kboard.press(Key.space)
			kboard.release(Key.space)
			space += 1
		elif space < 2:
			space += 1
	#thumb and index open
	if(thumb and index and not middle and not ring and not pinky):
		kboard.press(Key.ctrl)
		kboard.press('c')
		kboard.release('c')
		kboard.release(Key.ctrl)
		pasted = 0
	#ring and pinky open
	if(not thumb and not index and not middle and ring and pinky):
		if pasted == 3:
			kboard.press(Key.ctrl)
			kboard.press('v')
			kboard.release('v')
			kboard.release(Key.ctrl)
			pasted += 1
		elif pasted < 3:
			pasted += 1
	#thumb open
	if(thumb and not index and not middle and not ring and not pinky):
		if switchedA == 4:
			kboard.press(Key.ctrl)
			kboard.press(Key.tab)
			kboard.release(Key.tab)
			kboard.release(Key.ctrl)
			switchedA += 1
		elif switchedA < 4:
			switchedA += 1
	#pinky open
	if(not thumb and not index and not middle and not ring and pinky):
		if switchedB == 4:
			kboard.press(Key.ctrl)
			kboard.press(Key.shift)
			kboard.press(Key.tab)
			kboard.release(Key.tab)
			kboard.release(Key.shift)
			kboard.release(Key.ctrl)
			switchedB += 1
		elif switchedB < 4:
			switchedB += 1
	#all closed
	if(not thumb and not index and not middle and not ring and not pinky):
		if minim == 4:
			kboard.press(Key.cmd)
			kboard.press(Key.down)
			kboard.release(Key.down)
			kboard.release(Key.cmd)
			minim += 1
		elif minim < 4:
			minim += 1
	#all but thumb open
	if(not thumb and index and middle and ring and pinky):
		if maxim == 4: 
			kboard.press(Key.cmd)
			kboard.press(Key.up)
			kboard.release(Key.up)
			kboard.release(Key.cmd)
			maxim += 1
		elif maxim < 4:
			maxim += 1
	if(not thumb and index and middle and not ring and not pinky):
		x = (int(lndmrks[8][1]) * 3) - ((int(lndmrks[8][1]) * 3) % 10)
		y = (int(lndmrks[8][2]) * 3) - ((int(lndmrks[8][2]) * 3) % 10)
		mouse.position = (x, y)
		if((math.dist(lndmrks[8], lndmrks[12]) < 14) and (clicked == 2)):
			mouse.press(Button.left)
			mouse.release(Button.left)
			clicked += 1
		elif(clicked < 2):
			clicked += 1
		else:
			clicked = 0

######################################

""" constant loop """
while True:
	#reading the image
	success, img = cap.read()
	#hand tracking
	img = trckr.findHands(img)
	lmList = trckr.findPosition(img)
	if(len(lmList) != 0):
		gesture(lmList)
	#streaming
	cv2.imshow("Img", img)
	#delay 1 millisecond
	cv2.waitKey(1)

######################################