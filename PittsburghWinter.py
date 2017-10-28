from Tkinter import *
from eventBasedAnimationClass import EventBasedAnimationClass
import math
import random

class BubbleTroubleGame(EventBasedAnimationClass):
	def __init__(self, width, height):
		self.timerDelay = 6
		self.menuToggle = True 
		self.singlePlayerToggle = False
		self.multiPlayerToggle = False
		self.gameOverToggle = False
		self.levelEditorToggle = False
		self.levelEditingDone = False
		self.stayingAliveToggle = False
		self.instructionsToggle = False
		self.gameFinished = False
		self.level = 0
		self.width = width
		self.height = height
		self.ceilingHeight = 8
		self.bottomHeight = self.height - 100
		self.blockWidth = 25
		self.x = self.width/2
		self.y = self.bottomHeight - 21
		self.a = self.width/2 + 100
		self.b = self.bottomHeight - 21
		self.gravity = 0.3
		# Large Bubble
		self.lBubbleR = 30
		self.lMaxHeight = 150
		# Medium Bubble
		self.mBubbleR = 20
		# Small Bubble
		self.sBubbleR = 10
		self.arrowXCoordinates = [ ]
		self.arrowHeight = 400
		self.lastCollisionPoint = [ ] 
		self.largeBubbleList = [ ]
		self.mediumBubbleList = [ ]
		self.smallBubbleList = [ ]
		self.cloudList = [ ]
		self.largeCount = 0
		self.mediumCount = 0
		self.smallCount = 0
		self.largeMode = False
		self.mediumMode = False
		self.smallMode = False


	def bubbleMovement(self):
		lMaxHeight = self.lMaxHeight
		bottomHeight = self.bottomHeight
		if ((self.singlePlayerToggle == True or 
			self.multiPlayerToggle == True or
			self.stayingAliveToggle == True or 
			self.levelEditingDone == True) and
			self.gameOverToggle == False):
			for largeBubble in self.largeBubbleList:
				vertVelocity = largeBubble[2]
				horizVelocity = largeBubble[3]
				# determine movement mode
				if largeBubble[1] > 258:
					largeBubble[4] = "up"
				if largeBubble[1] <= 140:
					largeBubble[4] = "down" 
					largeBubble[2] = 2
				# act on given movement mode
				if largeBubble[4] == "down":
					largeBubble[2] += self.gravity
				if largeBubble[4] == "up":
					largeBubble[2] -= self.gravity
				if largeBubble[0] >= 700 or largeBubble[0] <= 0:
					largeBubble[3] = -1*largeBubble[3]
				largeBubble[1] += largeBubble[2]
				largeBubble[0] += largeBubble[3]
			for mediumBubble in self.mediumBubbleList:
				# determine movement mode
				if mediumBubble[1] > 298:
					mediumBubble[4] = "up"
				if mediumBubble[1] < 220:
					mediumBubble[4] = "down" 
					mediumBubble[2] = 2
				# act on given movement mode
				if mediumBubble[4] == "down":
					mediumBubble[2] += self.gravity
				if mediumBubble[4] == "up":
					mediumBubble[2] -= self.gravity
				if mediumBubble[0] >= 700 or mediumBubble[0] <= 0:
					mediumBubble[3] = -1*mediumBubble[3]
				mediumBubble[1] += mediumBubble[2]
				mediumBubble[0] += mediumBubble[3]
			for smallBubble in self.smallBubbleList:
				# determine movement mode
				if smallBubble[1] > 334:
					smallBubble[4] = "up"
				if smallBubble[1] < 280:
					smallBubble[4] = "down" 
					smallBubble[2] = 1
				# act on given movement mode
				if smallBubble[4] == "down":
					smallBubble[2] += self.gravity
				elif smallBubble[4] == "up":
					smallBubble[2] -= self.gravity
				if smallBubble[0] >= 700 or smallBubble[0] <= 0:
					smallBubble[3] = -1*smallBubble[3]
				smallBubble[1] += smallBubble[2] # add vert velocity
				smallBubble[0] += smallBubble[3] # add horiz velocity


	def increaseArrowLength(self):
		if len(self.arrowXCoordinates) == 1:
			if self.arrowHeight != 0:
				self.arrowHeight -= 16
			if self.arrowHeight == 0:
				self.arrowXCoordinates = [ ]
				self.arrowHeight = 360

	def determineLevel(self):
		if (self.largeBubbleList == [ ] and
			self.mediumBubbleList == [ ] and 
			self.smallBubbleList == [ ] and 
			self.gameOverToggle == False and
			(self.singlePlayerToggle == True or
			self.multiPlayerToggle == True)):
			self.level += 1
			if self.level == 1:
				self.largeBubbleList = [[200,150,1,2.5,"down"]]
				self.mediumBubbleList = [ ]
				self.smallBubbleList = [ ]
			elif self.level == 2:
				self.largeBubbleList = [[100,150,1,2.5,"down"],
										[300,150,1,2.5,"down"]]
				self.mediumBubbleList = [ ]
				self.smallBubbleList = [ ]
			elif self.level == 3:
				self.largeBubbleList = [[100,150,1,2.5,"down"]]
				self.mediumBubbleList = [[150,100,1,2.5,"down"],
										[200,150,1,2.5,"down"]]
				self.smallBubbleList = [ ]
			elif self.level == 4:
				self.largeBubbleList = [[100,150,1,2.5,"down"]]
				self.mediumBubbleList = [ ]
				self.smallBubbleList = [[200,270,1,2.5,"down"],
										[300,270,1,2.5,"down"],
										[400,270,1,2.5,"down"]]
			elif self.level == 5:
				self.largeBubbleList = [[100,150,1,2.5,"down"], 
										[300,150,1,2.5,"down"]]
				self.mediumBubbleList = [ ]
				self.smallBubbleList = [[200,270,1,2.5,"down"],
										[300,270,1,2.5,"down"],
										[400,270,1,2.5,"down"]]
			elif self.level == 6:
				# DRAW THE BEEAAAANIE
				self.gameOverToggle = True
				self.gameFinished = True
				self.drawSnowmanHat()

			# create diamonds background
			self.canvas.create_oval(537, 118, 568, 152, 
									fill="white", width=2, outline="gray")
			# draw steelers diamonds
			(height, width) = (8, 4)
			self.canvas.create_polygon(550, 127-height, 550+width, 127,
									   550, 127+height, 550-width, 127,
									   fill="gold")
			self.canvas.create_polygon(558, 135-height, 558+width, 135,
									   558, 135+height, 558-width, 135,
									   fill="red")
			self.canvas.create_polygon(550, 144-height, 550+width, 144,
									   550, 144+height, 550-width, 144,
									   fill="blue")

	def playStayingAlive(self):
		if self.stayingAliveToggle == True:
			largeBubbleList = self.largeBubbleList
			mediumBubbleList = self.mediumBubbleList
			smallBubbleList = self.smallBubbleList
			if 0 <= len(largeBubbleList)+len(mediumBubbleList) < 2:
				pickSizeBubble = random.randint(0, 2)
				pickHeightBubble = random.randint(100, 300)
				if pickSizeBubble == 0:
					self.largeBubbleList.append([5, pickHeightBubble, 
												1, 2.5, "down"])
				elif pickSizeBubble == 1:
					self.mediumBubbleList.append([5, pickHeightBubble, 
												1, 2.5, "down"])
				elif pickSizeBubble == 2:	
					self.smallBubbleList.append([5, pickHeightBubble, 
												1, 2.5, "down"])

	def addArrowCoord(self, x):
		self.arrowXCoordinates = self.arrowXCoordinates + [x]

	def arrowLBubbleCollision(self):
		lBubbleR = self.lBubbleR
		minimum = self.arrowHeight
		maximum = 400
		for largeBubble in self.largeBubbleList:
			x = largeBubble[0]
			y = largeBubble[1]
			if minimum < y < maximum and len(self.arrowXCoordinates) == 1:
				arrowX = self.arrowXCoordinates[0]
				if x-lBubbleR < arrowX < x+lBubbleR:
					self.mediumBubbleList.append([x-5, y, 1, -2.5, "up"])
					self.mediumBubbleList.append([x+5, y, 1, 2.5, "up"])
					self.largeBubbleList.remove(largeBubble)
					self.arrowXCoordinates = [ ]
					self.largeCount += 1

	def arrowMBubbleCollision(self):
		mBubbleR = self.mBubbleR
		minimum = self.arrowHeight
		maximum = 400
		for mediumBubble in self.mediumBubbleList:
			x = mediumBubble[0]
			y = mediumBubble[1]
			if minimum < y < maximum and len(self.arrowXCoordinates) == 1:
				arrowX = self.arrowXCoordinates[0]
				if x-mBubbleR < arrowX < x+mBubbleR:
					self.smallBubbleList.append([x-2, y, 1, -2.5,"up"])
					self.smallBubbleList.append([x+2, y, 1, 2.5,"up"])
					self.mediumBubbleList.remove(mediumBubble)
					self.arrowXCoordinates = [ ] 
					self.mediumCount += 1

	def arrowSBubbleCollision(self):
		sBubbleR = self.sBubbleR
		minimum = self.arrowHeight
		maximum = 400
		for smallBubble in self.smallBubbleList:
			x = smallBubble[0]
			y = smallBubble[1]
			if minimum < y < maximum and len(self.arrowXCoordinates) == 1:
				arrowX = self.arrowXCoordinates[0]
				if x-sBubbleR < arrowX < x+sBubbleR:
					self.smallBubbleList.remove(smallBubble)
					self.arrowXCoordinates = [ ] 
					self.smallCount += 1

	# returns t/f for character and bubble collision
	def distanceFormula(self, x1, y1, x2, y2, r):
		distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
		if distance < (r+20): # true if collides
			return True
		return False


	def bubbleCharacterCollision(self):
		lBubbleR = self.lBubbleR
		mBubbleR = self.mBubbleR
		sBubbleR = self.sBubbleR
		bottomHeight = self.bottomHeight
		x = self.x
		for largeBubble in self.largeBubbleList:
			x1 = largeBubble[0]
			y1 = largeBubble[1]
			x2 = x
			y2 = bottomHeight - 20
			if self.distanceFormula(x1, y1, x2, y2, lBubbleR):
				self.gameOverToggle = True
		for mediumBubble in self.mediumBubbleList:
			x1 = mediumBubble[0]
			y1 = mediumBubble[1]
			x2 = x
			y2 = bottomHeight - 20
			if self.distanceFormula(x1, y1, x2, y2, mBubbleR):
				self.gameOverToggle = True
		for smallBubble in self.smallBubbleList:
			x1 = smallBubble[0]
			y1 = smallBubble[1]
			x2 = x
			y2 = bottomHeight - 20
			if self.distanceFormula(x1, y1, x2, y2, sBubbleR):
				self.gameOverToggle = True

	def bubbleCharacter2Collision(self):
		if self.multiPlayerToggle == True:
			lBubbleR = self.lBubbleR
			mBubbleR = self.mBubbleR
			sBubbleR = self.sBubbleR
			bottomHeight = self.bottomHeight
			a = self.a
			for largeBubble in self.largeBubbleList:
				x1 = largeBubble[0]
				y1 = largeBubble[1]
				x2 = a
				y2 = bottomHeight - 20
				if self.distanceFormula(x1, y1, x2, y2, lBubbleR):
					self.gameOverToggle = True
			for mediumBubble in self.mediumBubbleList:
				x1 = mediumBubble[0]
				y1 = mediumBubble[1]
				x2 = a
				y2 = bottomHeight - 20
				if self.distanceFormula(x1, y1, x2, y2, mBubbleR):
					self.gameOverToggle = True
			for smallBubble in self.smallBubbleList:
				x1 = smallBubble[0]
				y1 = smallBubble[1]
				x2 = a
				y2 = bottomHeight - 20
				if self.distanceFormula(x1, y1, x2, y2, sBubbleR):
					self.gameOverToggle = True

	# go back to menu and reset everything
	def goBackToMenu(self):
		self.menuToggle = True
		self.instructionsToggle = False
		self.gameOverToggle = False
		self.multiPlayerToggle = False
		self.singlePlayerToggle = False
		self.gameFinished = False
		self.stayingAliveToggle = False
		self.levelEditorToggle = False
		self.levelEditingDone = False
		self.x = self.width/2
		self.y = self.bottomHeight - 20
		self.a = self.width/2 + 100
		self.b = self.bottomHeight - 20
		self.level = 0
		self.largeBubbleList = [ ]
		self.mediumBubbleList = [ ]
		self.smallBubbleList = [ ]
		self.cloudList = [ ]
		self.arrowXCoordinates = [ ]
		self.lastCollisionPoint = [ ]
		self.largeCount = 0
		self.mediumCount = 0
		self.smallCount = 0

	# make three clouds in random spaces
	def makeClouds(self):
		if len(self.cloudList) < 7:
			cloudX = random.randint(0, 800)
			cloudY = random.randint(50, 150)
			self.cloudList.append([cloudX, cloudY])

	def drawMenu(self):
		if self.menuToggle == True:
			width = self.width
			height = self.height
			menuTexts = ["Single-Player", "Multiplayer", "Stayin' Alive", 
						"Level Editor", "Instructions"]
			# draw background
			self.canvas.create_rectangle(0, 0, width, height,
										fill="SteelBlue")
			# draw menu background
			self.canvas.create_rectangle(50, 120,
										350, 460,
										fill = "LightSteelBlue")
			# draw buttons
			# draw single-player button

			y1 = [145, 205, 265, 325, 385]
			y2 = [195, 255, 315, 375, 435]
			for i in xrange(0,5):
				self.canvas.create_rectangle(60, y1[i],
											340, y2[i],
											fill = "WhiteSmoke")
			# draw menu texts
			for center in xrange(170, 411, 60):
				i = (center - 170)/50
				self.canvas.create_text(200, center, text=menuTexts[i],
										font="Arial 17 bold")
			# draw game title
			self.canvas.create_text(197, 73, text="PITTSBURGH\n    WINTER",
							font="Arial 30 bold", fill="LightSteelBlue")
			self.canvas.create_text(200, 70, text="PITTSBURGH\n    WINTER",
							font="Arial 30 bold", fill="MidnightBlue")

	def drawGameFinished(self):
		if self.gameFinished == True:
			width = self.width
			height = self.height
			self.canvas.create_text(width/2, height/2+50, 
									text="WELL DONE!",
									font="Arial 18")

	def drawMenuSnowman(self):
		if (self.menuToggle == True or self.instructionsToggle == True):
			lRadius = 90
			mRadius = 65
			sRadius = 50
			# draw body
			self.canvas.create_oval(550-lRadius, 370-lRadius,
									550+lRadius, 370+lRadius,
									fill="white", outline="white")
			self.canvas.create_oval(550-mRadius, 255-mRadius,
									550+mRadius, 255+mRadius,
									fill="white", outline="white")
			self.canvas.create_oval(550-sRadius, 175-sRadius,
									550+sRadius, 175+sRadius,
									fill="white", outline="white")
			# draw eyes
			self.canvas.create_oval(530-2, 175-2,
									530+2, 175+2,
									fill="black")
			self.canvas.create_oval(570-2, 175-2,
									570+2, 175+2,
									fill="black")
			self.canvas.create_arc(535, 170,
								   565, 200, 
								   start=250, extent=90,
								   style=ARC, width=2)

	def drawSnowmanHat(self):
		if (self.menuToggle == True or self.instructionsToggle == True):
			# draw hat
			self.canvas.create_arc(502, 110,
								   598, 210,
								   start=0, extent=180,
								   fill="black")
			self.canvas.create_rectangle(500, 158, 
										 600, 165,
										 fill="yellow", 
										 outline="yellow")
			# create diamonds background
			self.canvas.create_oval(537, 118, 568, 152, 
									fill="white", width=2, outline="gray")
			# draw steelers diamonds
			(height, width) = (8, 4)
			self.canvas.create_polygon(550, 127-height, 550+width, 127,
									   550, 127+height, 550-width, 127,
									   fill="gold")
			self.canvas.create_polygon(558, 135-height, 558+width, 135,
									   558, 135+height, 558-width, 135,
									   fill="red")
			self.canvas.create_polygon(550, 144-height, 550+width, 144,
									   550, 144+height, 550-width, 144,
									   fill="blue")

	def drawGameBackground(self):
		if (self.singlePlayerToggle == True or
			self.multiPlayerToggle == True or
			self.stayingAliveToggle == True or
			self.levelEditorToggle == True or 
			self.levelEditingDone == True):
				self.drawGameCeiling()
				self.drawGameBottom()

	def drawGameBackgroundColor(self):
		if (self.singlePlayerToggle == True or
			self.multiPlayerToggle == True or
			self.stayingAliveToggle == True or
			self.levelEditorToggle == True or
			self.levelEditingDone == True):
			width = self.width
			height = self.height
			self.canvas.create_rectangle(0, 0,
										width, height, 
										fill="white smoke")

	def drawGameCeiling(self):
		width = self.width
		height = self.height
		ceilingHeight = self.ceilingHeight
		# draw ceiling
		self.canvas.create_rectangle(0, 0, 
									width, ceilingHeight,
									fill="gray", outline="gray")
		# draw spikes on ceiling
		for i in xrange(1, width, 3):
			trianglePoints = [i-1, ceilingHeight, i, ceilingHeight+2, 
								i+1, ceilingHeight]
			self.canvas.create_polygon(trianglePoints, outline="darkgray", 
									   fill="darkgray")

	def drawGameOver(self):
		if self.gameOverToggle == True:
			width = self.width
			height = self.height
			self.canvas.create_text(width/2, height/2,
									text="GAME OVER",
									font="Arial 30 bold")

	def drawGameBottom(self):
		bottomHeight = self.bottomHeight
		width = self.width
		height = self.height 
		self.canvas.create_rectangle(0, bottomHeight,
									width, height, fill="dark gray",
									outline="maroon3")

	def drawSnowy1(self, x, y):
		if (self.singlePlayerToggle == True or 
			self.multiPlayerToggle == True or
			self.stayingAliveToggle == True or
			self.levelEditorToggle == True or
			self.levelEditingDone == True):
			self.x = x
			self.y = y
			self.canvas.create_oval(x-20, y-20, 
									x+20, y+20,
									fill="white", outline="light gray")
			self.canvas.create_oval(x-15, y-15-14, 
									x+15, y-15+14,
									fill="white", outline="light gray")
			self.canvas.create_oval(x-11, y-28-11, 
									x+11, y-28+11,
									fill="white", outline="light gray")

	def drawSnowy2(self, a, b):
		if self.multiPlayerToggle == True:
			self.a = a
			self.b = b
			self.canvas.create_oval(a-18, b-18, 
									a+18, b+18,
									fill="white", outline="light blue")
			self.canvas.create_oval(a-15, b-15-14, 
									a+15, b-15+14,
									fill="white", outline="light blue")
			self.canvas.create_oval(a-11, b-28-11, 
									a+11, b-28+11,
									fill="white", outline="light blue")

	def drawLevelEditButtons(self):
		if self.levelEditorToggle == True:
			width = self.width
			for x in xrange(width/2-100, width/2+101, 100):
				colors = ["SteelBlue", "LightSteelBlue", "LightCyan"]
				colorIndex = (x-200)/100 
				self.canvas.create_rectangle(x-50, 420, 
											x+50, 480, 
											fill=colors[colorIndex])
			for x in xrange(width/2-100, width/2+101, 100):
				text = ["Large Snow", "Medium Snow", "Small Snow"]
				textIndex = (x-200)/100 
				self.canvas.create_text(x, 450, 
										text=text[textIndex],
										font="Arial 12 bold")

	def drawLevelEditorPlayButton(self):
		if self.levelEditorToggle == True:
			width = self.width
			height = self.height
			self.canvas.create_rectangle(width/2+170, 420, 
										width/2+210, 480,
										fill="white")
			self.canvas.create_text(width/2+190, 450, 
									text="PLAY")
	def drawLevelEdits(self):
		if self.levelEditorToggle == True:
			for largeBubble in self.largeBubbleList:
				self.drawLBubble(largeBubble)
			for mediumBubble in self.mediumBubbleList:
				self.drawMBubble(mediumBubble)
			for smallBubble in self.smallBubbleList:
				self.drawSBubble(smallBubble)

	# draws large bubble based on coordinates list
	def drawLBubble(self, coordinates):
		x = coordinates[0]
		y = coordinates[1]
		lBubbleR = self.lBubbleR
		self.canvas.create_oval(x-lBubbleR, y-lBubbleR,
								x+lBubbleR, y+lBubbleR,
								fill="SteelBlue")

	# draws medium bubble based on coordinates list
	def drawMBubble(self, coordinates):
		x = coordinates[0]
		y = coordinates[1]
		mBubbleR = self.mBubbleR
		self.canvas.create_oval(x-mBubbleR, y-mBubbleR,
								x+mBubbleR, y+mBubbleR,
								fill="LightSteelBlue")

	# draws small bubble based on coordinates list
	def drawSBubble(self, coordinates):
		x = coordinates[0]
		y = coordinates[1]
		sBubbleR = self.sBubbleR
		self.canvas.create_oval(x-sBubbleR, y-sBubbleR,
								x+sBubbleR, y+sBubbleR,
								fill="LightCyan")

	def drawLevelLabel(self):
		if ((self.singlePlayerToggle == True or
			self.multiPlayerToggle == True) and 
			self.gameFinished == False):
			level = self.level
			width = self.width
			height = self.height
			self.canvas.create_text(width/2,
									450,
									text="LEVEL %d" % level,
									font="Arial 16 bold")

	def drawLevel(self):
		if (self.singlePlayerToggle == True or
			self.multiPlayerToggle == True or
			self.stayingAliveToggle == True or
			self.levelEditingDone == True):
			for largeBubble in self.largeBubbleList:
					self.drawLBubble(largeBubble)
			for mediumBubble in self.mediumBubbleList:
				self.drawMBubble(mediumBubble)
			for smallBubble in self.smallBubbleList:
				self.drawSBubble(smallBubble)

	def drawArrow(self):
		self.increaseArrowLength()
		for x in self.arrowXCoordinates:
			self.canvas.create_line(x, 400,
									x, self.arrowHeight,
									width=3)
			self.canvas.create_line(x-10, self.arrowHeight+10,
									x, self.arrowHeight,
									width=3)
			self.canvas.create_line(x+10, self.arrowHeight+10,
									x, self.arrowHeight,
									width=3)

	def drawBacktoMenuButton(self):
		if self.menuToggle == False:
			width = self.width
			height = self.height
			self.canvas.create_rectangle(25, 425,
										125, 475,
										fill="lightsteelblue")
			self.canvas.create_text(75, 450,
									text="MENU",
									font="Arial 13 bold")

	def drawClouds(self):
		if (self.singlePlayerToggle == True or
			self.multiPlayerToggle == True or
			self.stayingAliveToggle == True or
			self.levelEditingDone == True):
			self.makeClouds()
			for cloud in self.cloudList:
				cloudX = cloud[0]
				cloudY = cloud[1]
				self.canvas.create_oval(cloudX-40, cloudY-30,
										cloudX+40, cloudY+30,
										fill="white", 
										outline="white")
				self.canvas.create_oval(cloudX-70, cloudY-30,
										cloudX+10, cloudY+30,
										fill="white", 
										outline="white")
				self.canvas.create_oval(cloudX-10, cloudY-30,
										cloudX+70, cloudY+30,
										fill="white", 
										outline="white")
				self.canvas.create_oval(cloudX-40, cloudY,
										cloudX+40, cloudY+60,
										fill="white", 
										outline="white")
				self.canvas.create_oval(cloudX-40, cloudY-60,
										cloudX+40, cloudY,
										fill="white", 
										outline="white")
	def drawInstructions(self):
		if self.instructionsToggle == True:
			width = self.width
			height = self.height
			storyText = \
			"""			Snowy, a kind-hearted resident of Pittsburgh,
			was strolling through Schenley Park when the nasty
			wind blew his beloved Steelers beanie away.
			Help Snowy overcome the Pittsburgh winter 
			weather and find his beanie!"""
			instructionText = \
			"""			Use <-- and --> keys to move Snowy.
			Use -SPACEBAR- to shoot arrows at 
			the bouncing snow.
			If multiplayer, use A, D, and S.
			Clouds may obstruct your view, so 
			don't be fooled and don't
			get hit by snow!"""
			# draw background color
			self.canvas.create_rectangle(0, 0, width, height,
										fill="LightSteelBlue")
			# draw instructions panel background
			self.canvas.create_rectangle(20, 20,
										width-20, height-20, 
										fill="light gray")
			self.canvas.create_text(width/4-20, 2*height/7,
									text=storyText,
									font="arial 17 italic")
			self.canvas.create_text(width/4-70, 4*height/7,
									text=instructionText,
									font="arial 17")

	def drawStayingAliveCounts(self):
		if self.stayingAliveToggle == True:
			width = self.width
			self.canvas.create_oval(width/2-50-25, 450-25,
									width/2-50+25, 450+25,
									fill="SteelBlue")
			self.canvas.create_oval(width/2-15, 450-15,
									width/2+15, 450+15,
									fill="LightSteelBlue")
			self.canvas.create_oval(width/2+37-10, 450-10,
									width/2+37+10, 450+10,
									fill="LightCyan")
			self.canvas.create_text(width/2-50, 450, 
									text="%d"%self.largeCount)
			self.canvas.create_text(width/2, 450, 
									text="%d"%self.mediumCount)
			self.canvas.create_text(width/2+37, 450, 
									text="%d"%self.smallCount)

	def redrawAll(self):
		self.canvas.delete(ALL)
		self.drawMenu()
		self.drawInstructions()
		self.drawGameBackgroundColor()
		self.drawGameBackground()
		self.drawLevel()
		self.drawArrow()
		self.drawSnowy1(self.x, self.y)
		self.drawSnowy2(self.a, self.b)
		self.drawGameOver()
		self.drawLevelLabel()
		self.drawBacktoMenuButton()
		self.drawClouds()
		self.drawMenuSnowman()
		self.drawSnowmanHat()
		self.drawStayingAliveCounts()
		self.drawLevelEditButtons()
		self.drawLevelEdits()
		self.drawLevelEditorPlayButton()
		self.drawGameFinished()

	def onTimerFired(self):
		self.bubbleMovement()
		self.arrowLBubbleCollision()
		self.arrowMBubbleCollision()
		self.arrowSBubbleCollision()
		self.bubbleCharacterCollision()
		self.bubbleCharacter2Collision()
		self.determineLevel()
		self.playStayingAlive()

	def onTimerFiredWrapper(self):
		self.onTimerFired()
		self.redrawAll()
		self.canvas.after(self.timerDelay, self.onTimerFiredWrapper)

	def onKeyPressed(self, event):
		if (event.keysym == "Left"):
			self.x -= 15
		if (event.keysym == "Right"):
			self.x += 15
		if (event.keysym == "space"):
			self.addArrowCoord(self.x+10)
		if (event.keysym == "a"):
			self.a -= 15
		if (event.keysym == "d"):
			self.a += 15
		if (event.keysym == "s"):
			self.addArrowCoord(self.a+10)

	def onMousePressed(self, event):
		(x, y) = (event.x, event.y)
		width = self.width
		height = self.height
		# menu buttons
		if 60 < x < 340 and self.menuToggle == True:
			if 135 < y < 185:
				self.menuToggle = False
				self.singlePlayerToggle = True
			if 195 < y < 245:
				self.menuToggle = False
				self.multiPlayerToggle = True
			if 255 < y < 305:
				self.menuToggle = False
				self.stayingAliveToggle = True
			if 315 < y < 365:
				self.menuToggle = False
				self.levelEditorToggle = True
			if 375 < y < 425:
				self.menuToggle = False
				self.instructionsToggle = True
		# back to menu button
		if (50 < x < 150 and 425 < y < 475 and self.menuToggle == False):
			self.goBackToMenu()
		# adding bubbles in editor mode
		if self.levelEditorToggle == True and 20 < y < 370:
			if self.largeMode == True:
				self.largeBubbleList.append([x, y, 1, 2, "down"])
			elif self.mediumMode == True:
				self.mediumBubbleList.append([x, y, 1, 2, "down"])
			elif self.smallMode == True:
				self.smallBubbleList.append([x, y, 1, 2, "down"])
		# choosing editor mode
		if self.levelEditorToggle == True and 420 < y < 480:
			if width/2-150 < x < width/2-50:
				self.largeMode = True
				self.mediumMode = False
				self.smallMode = False
			elif width/2-50 < x < width/2+50:
				self.largeMode = False
				self.mediumMode = True
				self.smallMode = False
			elif width/2+50 < x < width/2+150:	
				self.largeMode = False
				self.mediumMode = False
				self.smallMode = True
			elif width/2+170 < x < width/2+210:
				self.levelEditorToggle = False
				self.levelEditingDone = True



	def initAnimation(self):
		self.root.bind("<Key>", lambda event: self.onKeyPressed(event))
		self.root.bind("<Button>", lambda event: self.onMousePressed(event))

	def run(self):
		self.root = Tk()
		self.canvas = Canvas(self.root, width=self.width, height=self.height)
		self.canvas.pack()
		self.initAnimation()
		self.onTimerFiredWrapper()
		self.root.mainloop()








bubbleTroubleGame = BubbleTroubleGame(width=700, height=500)
bubbleTroubleGame.run()












