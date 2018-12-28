from pyprocessing import *
import copy
import random

scale_y = 30
WIDTH,HEIGHT = 900,800
SCALE=1

COLORS = {"VARIABLE":(155,155,0),
		  "INTEGER":(255,255,255),
		  "FLOAT":(100,100,255),
		  "TRUE":(0,255,0),
		  "FALSE":(255,0,0),
		  "LIST_BORDER":(200,0,200),
		  "LIST_ELEMENT":(200,0,200),
		  "CHAR":(255,255,100),
		  "CHAR_BG":(100,100,100),
		  "POINTER_BG":(100,100,100),
		  "FUNCTION":(0,0,200)}

action=[True,False,False,False]

class Variable:
	
	variable_count = 0
	all_variables = []
	max_size = 200

	#I know this is not nice. I will update it when I start to define functions
	#Because functions will have their own variable blocks. So variable block should be
	#an independent class
	variable_block_x=30
	variable_block_y=5
	variable_block_width=240
	variable_block_height=15

	def __init__(self,x=50,y=-1,width=100,height=scale_y,name="",temp=False):
		self.name = str(name)
		self.X, self.Y = int(x), int(y)
		self.x, self.y = int(x), int(y)
		self.width, self.height = int(width), int(height)
		Variable.all_variables.append(self)
		if not temp:
			Variable.variable_block_height+=self.height+25
			Variable.variable_count+=1

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
		strokeWeight(5)
		stroke(255)
		line(Variable.variable_block_x,Variable.variable_block_y,Variable.variable_block_x+Variable.variable_block_width,Variable.variable_block_y)#TOP
		line(Variable.variable_block_x+Variable.variable_block_width,Variable.variable_block_y,Variable.variable_block_x+Variable.variable_block_width,Variable.variable_block_y+Variable.variable_block_height)#RIGHT
		line(Variable.variable_block_x,Variable.variable_block_y+Variable.variable_block_height,Variable.variable_block_x+Variable.variable_block_width,Variable.variable_block_y+Variable.variable_block_height)#BOT
		stroke(0)

		# THIS IS HOW IT ACTUALLY SHOULD. IT SHOULD ADAPT WIDTH

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
		stroke(0)
		fill(0)
		color = COLORS["VARIABLE"]
		fill(color[0],color[1],color[2])
		rect(self.x,self.y,100,self.height)
		if self.name!="":
			textSize(10)
			text(self.name,self.x+self.width/2,self.y+self.height+15)

	def deepcopy(self):
		new_copy=copy.deepcopy(self)
		Variable.all_variables.append(new_copy)
		return new_copy
	def copy(self):
		new_copy=copy.copy(self)
		Variable.all_variables.append(new_copy)
		return new_copy

	def destroy(self):
		Variable.all_variables.remove(self)	
		#Variable.variable_count-=1						#I think these won't be necessary
		#Variable.variable_block_height-=self.height+25	#because I want to take C as language
														#and variables can not be deleted in C
		del self
	def __repr__(self):
		return self.name+" "+str(self.value)
"""
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
		Variable.variable_block_height+=self.height+25
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
		if self.name!="":
			text(self.name+" = "+str(self.value),self.x+self.width/2,self.y+self.height+15)
		else:
			text(str(self.value),self.x+self.width/2,self.y+self.height+15)
	
	#CONTINUE FROM HERE
	def NOT(self):
		pass
"""
class Integer(Variable):
	
	def __init__(self,value=0,x=50,y=-1,height=scale_y,name="",temp=False):
		if y==-1:
			y=Variable.variable_count*(scale_y+25)+10
		Variable.__init__(self,x,y,value,height,name,temp)
		self.value = value

	def display(self):
		stroke(0)
		fill(0)
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
		if self.name!="":
			text(str(self.name+"="+str(self.value)),self.x,self.y+self.height+15)
		else:
			text(str(self.value),self.x,self.y+self.height+15)

		fill(0)	#This is necessary because it effects whole program
	def __add__(a,b):
		return a.value+b.value
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

	def __init__(self,value=0.0,x=50,y=-1,height=scale_y,name="",temp=False):
		if y==-1:
			y=Variable.variable_count*(scale_y+25)+10
		Variable.__init__(self,x,y,value,height,name,temp)
		self.value = value
		self.integer = int(value)
		self.decimal = value%1

	def display(self):
		stroke(0)
		fill(0)
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
		if self.name!="":
			text(str(self.name+"="+str(self.value)),self.x,self.y+self.height+15)
		else:
			text(str(self.value),self.x,self.y+self.height+15)
	
		fill(0)	#This is necessary because it effects whole program
	def __add__(a,b):
		return a.value+b.value
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
class Char(Variable):
	char_size = 30

	def __init__(self,value="",x=50,y=-1,height=scale_y,name="",temp=False):
		if y==-1:
			y=Variable.variable_count*(scale_y+25)+10
		Variable.__init__(self,x,y,Char.char_size,height,name,temp)
		self.value = value
	def display(self):
		#parts
		stroke(0)
		fill(0)
		noStroke()
		textSize(12)		#SIZE SHOULD BE ABLE TO BE SELECTED
		
		color = COLORS["CHAR_BG"]
		fill(color[0],color[1],color[2])
		rect(self.x,self.y,Char.char_size,self.height)
		
		color = COLORS["CHAR"]
		fill(color[0],color[1],color[2])
		text(self.value,self.x+5,int(self.y+scale_y/2+5))
		textSize(10)
		if self.name!="":
			text(self.name+"="+self.value,self.x,self.y+self.height+15)
		stroke(0)

class Pointer(Variable):
	pointer_size = 30
	pointer_count = 0
	pointer_interval = 10
	def __init__(self,value=None,x=50,y=-1,height=scale_y,name="",temp=False):
		if y==-1:
			y=Variable.variable_count*(scale_y+25)+10
		Variable.__init__(self,x,y,Pointer.pointer_size,height,name,temp)
		self.value = value
		self.arrow_color=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
		self.arrow_distance=Pointer.pointer_count*Pointer.pointer_interval+40
		
		if type(self.value)==Variable or type(self.value)==Pointer or type(self.value)==None:
			self.color = COLORS["VARIABLE"]
		elif type(self.value)==Integer:
			self.color = COLORS["INTEGER"]
		elif type(self.value)==Float:
			self.color = COLORS["FLOAT"]
		elif type(self.value)==Char:
			self.color = COLORS["CHAR"]
		elif type(self.value)==List:
			self.color = COLORS["LIST"]
		
		Pointer.pointer_count+=1
	
	def display(self):
		stroke(0)
		fill(0)
		strokeWeight(4)
		#BG
		color = COLORS["POINTER_BG"]
		fill(color[0],color[1],color[2])
		rect(self.x,self.y,self.width,self.height)

		
		#COLOR
		stroke(self.color[0],self.color[1],self.color[2])

		#STAR
		line(self.x,self.y,self.x+self.width,self.y+self.height)					#LEFT-UP TO RIGHT-BOT
		line(self.x+self.width/2,self.y,self.x+self.width/2,self.y+self.height)		#TOP to BOT
		line(self.x+self.width,self.y,self.x,self.y+self.height)					#RIGHT-UP TO LEFT-BOT
		line(self.x,self.y+self.height/2,self.x+self.width,self.y+self.height/2)	#LEFT to RIGHT
		
		#HOW TO POINT
		color = self.arrow_color
		stroke(color[0],color[1],color[2])
		if type(self.value)!=None:
			line(self.x-5,self.y+self.height/3,self.X-self.arrow_distance,self.y+self.height/3)														#POINTER
			line(self.X-self.arrow_distance,self.y+self.height/3,self.X-self.arrow_distance,self.value.y+2*self.value.height/3)				#MAIN
			line(self.X-self.arrow_distance,self.value.y+2*self.value.height/3,self.value.X-20,self.value.y+2*self.value.height/3)	#POINTED
			line(self.value.X-20,self.value.y+2*self.value.height/3,self.value.X-25,self.value.y+2*self.value.height/3-5)			#ARROW UPSIDE
			line(self.value.X-20,self.value.y+2*self.value.height/3,self.value.X-25,self.value.y+2*self.value.height/3+5)			#ARROW UPSIDE
		"""
		#I was trying to make it look outside but then I noticed if it doesn't point to something, then no arrow required
		else:
			line(self.x-5,self.y+self.height/3,self.X-(Pointer.pointer_count*Pointer.pointer_interval+20),self.y+self.height/3)						#POINTER
			line(self.X-(Pointer.pointer_count*Pointer.pointer_interval+20),self.y+self.height/3,self.X-(Pointer.pointer_count*Pointer.pointer_interval+20)+5,self.y+self.height/3-5)												#ARROW UPSIDE
			line(self.X-(Pointer.pointer_count*Pointer.pointer_interval+20),self.y+self.height/3,self.X-(Pointer.pointer_count*Pointer.pointer_interval+20)+4,self.y+self.height/3+5)												#ARROW UPSIDE
		"""
		textSize(10)
		fill(self.color[0],self.color[1],self.color[2])
		if self.name!="":
			text(self.name+"="+self.value.name,self.x,self.y+self.height+15)
		stroke(0)
		strokeWeight(0)
class List(Variable):

	def __init__(self,value=[],x=50,y=-1,height=0,name="",temp=False):
		if y==-1:
			y=(Variable.variable_count-len(value))*(scale_y+25)+5
		Variable.__init__(self,x-5,y,Variable.max_size,len(value)*(scale_y+25),name,temp)
		Variable.variable_block_height-=self.height-25
		self.value = value
	def display(self):
		#border
		stroke(0)
		fill(0)
		color = COLORS["LIST_BORDER"]
		stroke(color[0],color[1],color[2])
		fill(color[0],color[1],color[2])
		strokeWeight(3)
		line(self.x,self.y,self.x+30,self.y)							#top
		line(self.x,self.y,self.x,self.y+self.height)					#left
		line(self.x,self.y+self.height,self.x+30,self.y+self.height)	#bottom
		current=0
		for i in self.value:
			line(self.x,self.y+current,self.x+30,self.y+current)
			current+=scale_y+25


		textSize(10)
		string="["
		for i in self.value:
			string+=str(i.value)
			string+=","
		string+="]"
		if self.name!="":
			text(str(self.name+"="+string),self.x,self.y+self.height+15)
		else:
			text(str(string),self.x,self.y+self.height+15)


		stroke(0)

