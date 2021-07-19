"""
	this is a python module by Murtaza's workshop
	with little tweaks according to what I needed

	It helps in the detection of hands using openCV
	I have added a few comments explaining the code if you are new to python
"""
#necessary imports
import cv2
import mediapipe as mp
import time
import keyboard

#creating a usable module
class handTrack():
	#initialization
	def __init__(self, mode = False, maxHnds = 2, detConf = 0.5, trackCon = 0.5):
		self.mode = mode
		self.maxHnds = maxHnds
		self.detConf = detConf
		self.trackCon = trackCon
		self.mpHands = mp.solutions.hands
		self.hands = self.mpHands.Hands(self.mode, self.maxHnds, self.detConf, self.trackCon)
		self.mpDraw = mp.solutions.drawing_utils

	#tracks the hands and draws the landmarks and connections over image
	def findHands(self, img, draw = True):
		#processing image
		imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imRGB)
		#draws over image only if hand is found
		if self.results.multi_hand_landmarks:
			for handLms in self.results.multi_hand_landmarks:
				self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
		#returning processed image
		return img

	#making a list of landmarks to process later
	def findPosition(self, img, handNo = 0):
		#landmark list initialized as an empty list
		lmList = []
		#if hand is found the landmarks list will be updated
		if self.results.multi_hand_landmarks:
			myHand = self.results.multi_hand_landmarks[handNo]
			for id, lm in enumerate(myHand.landmark):
				#storing height and width values
				h, w, c = img.shape
				#center position
				cx, cy, = int(lm.x * w), int(lm.y * h)
				#adding to the list
				lmList.append([id, cx, cy])
			return lmList
		return []

######################################END OF CODE