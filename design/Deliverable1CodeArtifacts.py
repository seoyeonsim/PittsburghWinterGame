from Tkinter import *
from eventBasedAnimationClass import EventBasedAnimationClass
import math
import random

class BubbleTroubleGame(EventBasedAnimationClass):
	def __init__(self, width, height):
		self.timerDelay = 3
		self.menuToggle = True 
		self.singlePlayerToggle = False
		self.multiPlayerToggle = False
		self.gameOverToggle = False
		self.levelEditorToggle = False
		self.stayingAliveToggle = False
		self.instructionsToggle = False
		self.level = 0
		self.width = width
		self.height = height
		self.ceilingHeight = 8
		self.bottomHeight = self.height - 100
		self.blockWidth = 25
		self.x = self.width/2
		self.y = self.bottomHeight - self.blockWidth
		self.a = self.width/2 + 100
		self.b = self.bottomHeight - self.blockWidth
		self.gravity = 0.3
		#self.initialRightVelocity = 2
		#self.initialLeftVelocity = -2
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


	def bubbleMovement(self):
		lMaxHeight = self.lMaxHeight
		bottomHeight = self.bottomHeight
		if ((self.singlePlayerToggle == True or 
			self.multiPlayerToggle == True or
			self.stayingAliveToggle == True) and
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
				if smallBubble[1] > 330:
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
			self.gameOverToggle == False):
			self.level += 1
			if self.level == 1:
				self.largeBubbleList = [[200,150,1,2,"down"]]
				self.mediumBubbleList = [ ]
				self.smallBubbleList = [ ]
			elif self.level == 2:
				self.largeBubbleList = [[100,150,1,2,"down"],
										[300,150,1,2,"down"]]
				self.mediumBubbleList = [ ]
				self.smallBubbleList = [ ]
			elif self.level == 3:
				self.largeBubbleList = [[100,150,1,2,"down"],
										[300,150,1,2,"down"]]
				self.mediumBubbleList = [ ]
				self.smallBubbleList = [ ]
			elif self.level == 4:
				self.largeBubbleList = [[100,150,1,2,"down"], 
										[300,150,1,2,"down"]]
				self.mediumBubbleList = [ ]
				self.smallBubbleList = [ ]

	def playStayingAlive(self):
		if self.stayingAliveToggle == True:
			largeBubbleList = self.largeBubbleList
			mediumBubbleList = self.mediumBubbleList
			smallBubbleList = self.smallBubbleList
			if (0 <= (len(largeBubbleList)+len(mediumBubbleList)
				+len(smallBubbleList)) < 2):
				pickSizeBubble = random.randint(0, 2)
				pickHeightBubble = random.randint(100, 300)
				if pickSizeBubble == 0:
					self.largeBubbleList.append([5, pickHeightBubble, 
												1, 2, "down"])
				elif pickSizeBubble == 1:
					self.mediumBubbleList.append([5, pickHeightBubble, 
												1, 2, "down"])
				elif pickSizeBubble == 2:	
					self.smallBubbleList.append([5, pickHeightBubble, 
												1, 2, "down"])

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
					self.mediumBubbleList.append([x-5, y, 1, -1.8, "up"])
					self.mediumBubbleList.append([x+5, y, 1, 1.8, "up"])
					self.largeBubbleList.remove(largeBubble)
					self.arrowXCoordinates = [ ] 

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
					self.smallBubbleList.append([x-2, y, 1, -1.8,"up"])
					self.smallBubbleList.append([x+2, y, 1, 1.8,"up"])
					self.mediumBubbleList.remove(mediumBubble)
					self.arrowXCoordinates = [ ] 

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

	# returns t/f for character and bubble collision
	def distanceFormula(self, x1, y1, x2, y2, r):
		distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
		if distance < (r+25): # true if collides
			return True
		return False

	def bubbleCharacterCollision(self):
		blockWidth = self.blockWidth
		lBubbleR = self.lBubbleR
		mBubbleR = self.mBubbleR
		sBubbleR = self.sBubbleR
		blockWidth = self.blockWidth
		bottomHeight = self.bottomHeight
		x = self.x
		for largeBubble in self.largeBubbleList:
			x1 = largeBubble[0]
			y1 = largeBubble[1]
			x2 = x
			y2 = bottomHeight - blockWidth
			if self.distanceFormula(x1, y1, x2, y2, lBubbleR):
				self.gameOverToggle = True
		for mediumBubble in self.mediumBubbleList:
			x1 = mediumBubble[0]
			y1 = mediumBubble[1]
			x2 = x
			y2 = bottomHeight - blockWidth
			if self.distanceFormula(x1, y1, x2, y2, mBubbleR):
				self.gameOverToggle = True
		for smallBubble in self.smallBubbleList:
			x1 = smallBubble[0]
			y1 = smallBubble[1]
			x2 = x
			y2 = bottomHeight - blockWidth
			if self.distanceFormula(x1, y1, x2, y2, sBubbleR):
				self.gameOverToggle = True

	# go back to menu and reset everything
	def goBackToMenu(self):
		self.menuToggle = True
		self.instructionsToggle = False
		self.gameOverToggle = False
		self.multiPlayerToggle = False
		self.singlePlayerToggle = False
		self.stayingAliveToggle = False
		self.levelEditorToggle = False
		self.x = self.width/2
		self.y = self.bottomHeight - self.blockWidth
		self.a = self.width/2 + 100
		self.b = self.bottomHeight - self.blockWidth
		self.level = 0
		self.largeBubbleList = [ ]
		self.mediumBubbleList = [ ]
		self.smallBubbleList = [ ]
		self.cloudList = [ ]
		self.arrowXCoordinates = [ ]
		self.lastCollisionPoint = [ ]

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
			self.stayingAliveToggle == True):
				self.drawGameCeiling()
				self.drawGameBottom()

	def drawGameBackgroundColor(self):
		if (self.singlePlayerToggle == True or
			self.multiPlayerToggle == True or
			self.stayingAliveToggle == True or
			self.levelEditorToggle == True):
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

	def drawTestBlock(self, x, y):
		if (self.singlePlayerToggle == True or 
			self.multiPlayerToggle == True or
			self.stayingAliveToggle == True):
			self.x = x
			self.y = y
			blockWidth = self.blockWidth
			self.canvas.create_oval(x-20, y-20, 
									x+20, y+20,
									fill="white", outline="light gray")
			self.canvas.create_oval(x-15, y-15-14, 
									x+15, y-15+14,
									fill="white", outline="light gray")
			self.canvas.create_oval(x-11, y-28-11, 
									x+11, y-28+11,
									fill="white", outline="light gray")

	def drawSecondTestBlock(self, a, b):
		if self.multiPlayerToggle == True:
			self.a = a
			self.b = b
			blockWidth = self.blockWidth
			self.canvas.create_oval(a-blockWidth, b-blockWidth, 
									a+blockWidth, b+blockWidth,
									fill="white")

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
		if (self.singlePlayerToggle == True or
			self.multiPlayerToggle == True):
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
			self.stayingAliveToggle == True):
			for largeBubble in self.largeBubbleList:
					self.drawLBubble(largeBubble)
			for mediumBubble in self.mediumBubbleList:
				self.drawMBubble(mediumBubble)
			for smallBubble in self.smallBubbleList:
				self.drawSBubble(smallBubble)

	def drawArrow(self):
		self.increaseArrowLength()
		blockWidth = self.blockWidth
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
			self.stayingAliveToggle == True):
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
			Don't get hit by snow!"""
			# draw background color
			self.canvas.create_rectangle(0, 0, width, height,
										fill="LightSteelBlue")
			# draw instructions panel background
			self.canvas.create_rectangle(20, 20,
										width-20, height-20, 
										fill="light gray")
			self.canvas.create_text(width/4-20, 3*height/7,
									text=storyText,
									font="Helvetica 17 italic")
			self.canvas.create_text(width/4-40, 5*height/7-20,
									text=instructionText,
									font="Helvetica 18 bold")


	def redrawAll(self):
		self.canvas.delete(ALL)
		self.drawMenu()
		self.drawInstructions()
		self.drawGameBackgroundColor()
		self.drawGameBackground()
		self.drawLevel()
		self.drawTestBlock(self.x, self.y)
		self.drawSecondTestBlock(self.a, self.b)
		self.drawArrow()
		self.drawGameOver()
		self.drawLevelLabel()
		self.drawBacktoMenuButton()
		self.drawClouds()
		self.drawMenuSnowman()
		self.drawSnowmanHat()

	def onTimerFired(self):
		self.bubbleMovement()
		self.arrowLBubbleCollision()
		self.arrowMBubbleCollision()
		self.arrowSBubbleCollision()
		self.bubbleCharacterCollision()
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
			self.addArrowCoord(self.x+self.blockWidth/2)
		if (event.keysym == "a"):
			self.a -= 15
		if (event.keysym == "d"):
			self.a += 15
		if (event.keysym == "s"):
			self.addArrowCoord(self.a+self.blockWidth/2)

	def onMousePressed(self, event):
		(x, y) = (event.x, event.y)
		# menu buttons
		if 60 < x < 340:
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
		if (50 < x < 150 and 425 < y < 475 and self.menuToggle == False):
			self.goBackToMenu()

	
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












