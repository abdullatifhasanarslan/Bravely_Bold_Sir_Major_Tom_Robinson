from pyprocessing import *

scale_y = 30
WIDTH,HEIGHT = 900,800

COLORS = {"VARIABLE":(155,155,0),
		  "INTEGER":(255,255,255),
		  "FLOAT":(100,100,255),
		  "TRUE":(0,255,0),
		  "FALSE":(255,0,0),
		  "LIST_BORDER":(200,0,200),
		  "LIST_ELEMENT":(200,0,200),
		  "STRING":(255,255,100)}

action=[True,False,False,False]

class Variable:
	
	variable_count = 0
	all_variables = []
	max_size = 200

	def __init__(self,x=50,y=-1,width=100,height=scale_y,name=""):
		self.name = str(name)
		self.X, self.Y = int(x), int(y)
		self.x, self.y = int(x), int(y)
		self.width, self.height = int(width), int(height)
		Variable.all_variables.append(self)

	def move(self,x,y):
		speed = 20
		remaining_x = int(x)-self.x
		remaining_y = int(y)-self.y
		#Going in x axis-----------
		if(remaining_x>0):
			remaining_x-=speed
			self.x += speed
			if remaining_x<0:
				self.x = int(x)
			return False
		elif(remaining_x<0):
			remaining_x+=speed
			self.x -= speed
			if remaining_x>0:
				self.x = int(x)
			return False
		#Going in y axis-----------
		if(remaining_y>0):
			remaining_y-=speed
			self.y += speed
			if remaining_y<0:
				self.y = int(y)
			return False
		elif(remaining_y<0):
			remaining_y+=speed
			self.y -= speed
			if remaining_y>0:
				self.y = int(y)
			return False
		return True
		#self.x, self.y = x, y

	def variableblock():
		noFill()
		stroke(255)
		rect(30,5,220,Variable.variable_count*(scale_y+25)+15)
		stroke(0)

		# THIS IS HOW IT ACTUALLY SHOULD

		# noFill()
		# stroke(255)
		# total_height = 0
		# max_width = 0
		# for variable in Variable.all_variables:
		# 	#rect(variable.x-20,variable.y-5,variable.width+20,variable.height+15)
		# 	total_height+=variable.height+15
		# 	if variable.width > max_width:
		# 		max_width=variable.width
		# rect(30,5,max_width+40,total_height+15)
		# stroke(0)

	def display(self):		
		color = COLORS["VARIABLE"]
		fill(color[0],color[1],color[2])
		rect(self.x,self.y,100,self.height)
		textSize(10)
		text(self.name,self.x+self.width/2,self.y+self.height+15)


	def destroy(self):
		Variable.all_variables.remove(self)		
		Variable.variable_count-=1
		del self

class Bool(Variable):

	def __init__(self,value=True,x=50,y=-1,height=scale_y,name=""):
		if y==-1:
			y=Variable.variable_count*(scale_y+25)
		Variable.__init__(self,x,y,100,height,name) #width may change
		self.value = value
		if self.value == True:
			self.angle = PI
		elif self.value == False:
			self.angle = 0
		else:
			self.angle = PI/2
		Variable.variable_count+=1

	def display(self):
		#fixed part
		color = COLORS["VARIABLE"]
		fill(color[0],color[1],color[2])

		rect(self.x+self.height,self.y,10,self.height)
		arc(self.x+self.height,int(self.y+self.height/2),15,15,PI/2,TWO_PI-PI/2)

		#lever part
		rectMode(CORNERS)
		pushMatrix()
		translate(self.x+self.height,int(self.y+self.height/2))
		rotate(self.angle)
		if self.value == True:
			color = COLORS["TRUE"]
			fill(color[0],color[1],color[2])
		elif self.value == False:
			color = COLORS["FALSE"]
			fill(color[0],color[1],color[2])
		else:
			color = COLORS["VARIABLE"]
			fill(color[0],color[1],color[2])
		rect(0,0,3,self.height/2)
		popMatrix()
		rectMode(CORNER)
		textSize(10)
		text(self.name+" = "+str(self.value),self.x+self.width/2,self.y+self.height+15)
	
	#CONTINUE FROM HERE
	def NOT(self):
		pass

class Integer(Variable):
	
	def __init__(self,value=0,x=50,y=-1,height=scale_y,name=""):
		if y==-1:
			y=Variable.variable_count*(scale_y+25)+10
		Variable.__init__(self,x,y,value,height,name)
		self.value = value
		Variable.variable_count+=1

	def display(self):
		color = COLORS["INTEGER"]
		fill(color[0],color[1],color[2])
		if(self.value<=Variable.max_size):
			rect(self.x,self.y,self.value,self.height)
		else:
			rect(self.x,self.y,Variable.max_size-80,self.height)
			#...
			strokeWeight(10)
			stroke(color[0],color[1],color[2])
			point(self.x+Variable.max_size-65,self.y+int(scale_y/2));point(self.x+Variable.max_size-50,self.y+int(scale_y/2));point(self.x+Variable.max_size-35,self.y+int(scale_y/2)); # ...
			stroke(0);strokeWeight(1)
			#...
			rect(self.x+Variable.max_size-20,self.y,20,self.height)
		textSize(10)
		text(str(self.name+"="+str(self.value)),self.x,self.y+self.height+15)

		fill(0)	#This is necessary because it effects whole program

	"""
	#NOT USED-----------------------	
	def __add__(a,b):
		global x
		if type(b)==Integer:
			if action[0] and a.move(WIDTH/2,HEIGHT/2):
				action[0]=False;action[1]=True
			elif action[1]:
				x=Integer(value=b.value,x=b.x,y=b.y,name="copy b")
				action[1]=False;action[2]=True
			elif action[2]:
				if a.value <= Variable.max_size:
					if x.move(WIDTH/2+a.value,HEIGHT/2):
						a.value+=x.value
						x.destroy()
						action[2]=False;action[3]=True
				else:
					if x.move(WIDTH/2+Variable.max_size,HEIGHT/2):
						a.value+=x.value
						x.destroy()
						action[2]=False;action[3]=True
			elif action[3] and a.move(a.X,a.Y):
				action[3]=False;action[0]=True
		return a
	"""



class Float(Variable):

	def __init__(self,value=0.0,x=50,y=-1,height=scale_y,name=""):
		if y==-1:
			y=Variable.variable_count*(scale_y+25)+10
		Variable.__init__(self,x,y,value,height,name)
		self.value = value
		self.integer = int(value)
		self.decimal = value%1
		Variable.variable_count+=1

	def display(self):
		color = COLORS["FLOAT"]
		fill(color[0],color[1],color[2])
		if(self.value<Variable.max_size):
			rect(self.x,self.y,self.integer,self.height)	#integer
			rect(self.x+self.integer,self.y+scale_y,10,-int(self.decimal*scale_y))	#decimal
		else:
			#integer
			rect(self.x,self.y,Variable.max_size-80,self.height)
			#...
			strokeWeight(10)
			stroke(color[0],color[1],color[2])
			point(self.x+Variable.max_size-65,self.y+int(scale_y/2));point(self.x+Variable.max_size-50,self.y+int(scale_y/2));point(self.x+Variable.max_size-35,self.y+int(scale_y/2)); # ...
			stroke(0);strokeWeight(1) 
			#...
			rect(self.x+Variable.max_size-20,self.y,20,self.height)
			#decimal
			rect(self.x+Variable.max_size,self.y+scale_y,10,-int(self.decimal*scale_y))	#decimal
		textSize(10)
		text(str(self.name+"="+str(self.value)),self.x,self.y+self.height+15)
	
		fill(0)	#This is necessary because it effects whole program

	"""
	#NOT USED-----------------------
	def __add__(c,a):
		global x
		if action[0]:
			if a.value <= Variable.max_size:
				if c.move(WIDTH/2+a.value,HEIGHT/2):
					action[0]=False;action[1]=True
			else:
				if c.move(WIDTH/2+Variable.max_size,HEIGHT/2):
					action[0]=False;action[1]=True
		elif action[1]:
			x=Float(value=float(a.value),x=a.x,y=a.y,name="copy a")
			action[1]=False;action[2]=True
		elif action[2] and x.move(WIDTH/2,HEIGHT/2):
			c.value+=x.value
			c.integer=int(c.value)
			c.decimal=c.value%1
			c.x=x.x
			x.destroy()
			action[2]=False;action[3]=True
		elif action[3] and c.move(c.X,c.Y):
			action[3]=False;action[0]=True
		return a
	"""

class String(Variable):

	char_size = 30

	def __init__(self,value="",x=50,y=-1,height=scale_y,name=""):
		if y==-1:
			y=Variable.variable_count*(scale_y+25)+10
		Variable.__init__(self,x,y,len(value)*(String.char_size+10)+10,height,name)
		self.value = value
		Variable.variable_count+=1
	def display(self):
		#border
		color = COLORS["LIST_BORDER"]
		fill(color[0],color[1],color[2])
		stroke(color[0],color[1],color[2])

		rect(self.x,self.y,3,scale_y)				#left
		rect(self.x,self.y+scale_y-3,self.width,3)	#bot
		rect(self.x+self.width,self.y-3,3,scale_y)	#right

		#parts
		noStroke()

		current = self.x+13
		textSize(12)		#SIZE SHOULD BE ABLE TO BE SELECTED
		for char in self.value:
			#ELEMENT BORDER
			color = COLORS["LIST_ELEMENT"]
			fill(color[0],color[1],color[2])
			rect(current,self.y,3,scale_y-10)	#left
			rect(current,self.y+scale_y-13,String.char_size,3)	#bot
			rect(current+String.char_size-3,self.y,3,scale_y-10)	#right

			color = COLORS["STRING"]
			fill(color[0],color[1],color[2])
			text(char,int(current+3+(String.char_size-6)/2),int(self.y+scale_y/2))

			current += String.char_size+10
		textSize(10)
		text(str(self.name+"="+str(self.value)),self.x,self.y+self.height+15)


		stroke(0)
		###
class List(Variable):


	def __init__(self,value=[],x=50,y=-1,height=scale_y,name=""):
		if y==-1:
			y=Variable.variable_count*(scale_y+25)+10
		Variable.__init__(self,x,y,len(value)*(Variable.max_size+10)+10,height,name)
		self.value = value
		Variable.variable_count+=1
	def display(self):
		#border
		color = COLORS["LIST_BORDER"]
		fill(color[0],color[1],color[2])
		stroke(color[0],color[1],color[2])

		rect(self.x,self.y,3,scale_y)				#left
		rect(self.x,self.y+scale_y-3,self.width,3)	#bot
		rect(self.x+self.width,self.y-3,3,scale_y)	#right

		#parts
		noStroke()

		current = self.x+13
		textSize(12)		#SIZE SHOULD BE ABLE TO BE SELECTED
		for element in self.value:
			#ELEMENT BORDER
			color = COLORS["LIST_ELEMENT"]
			fill(color[0],color[1],color[2])
			rect(current,self.y,3,scale_y-10)	#left
			rect(current,self.y+scale_y-13,Variable.max_size+3,3)	#bot
			rect(current+Variable.max_size+6,self.y,3,scale_y-10)	#right

			#color = COLORS["STRING"]
			#fill(color[0],color[1],color[2])
			#text(char,int(current+3+(String.char_size-6)/2),int(self.y+scale_y/2))
			element.x=current+3; element.y=self.y-20
			element.display()

			current += Variable.max_size+13
		textSize(10)
		text(str(self.name+"="+str(self.value)),self.x,self.y+self.height+15)


		stroke(0)
		###
		#CONTINUE HERE

		#CONTINUE HERE