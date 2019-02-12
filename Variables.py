from pyprocessing import *
import copy
import random
Small_Variable_width = 30
Variable_width = 200
Variable_height = 30
SCALE=1
MOVE_DURATION=80
SCALE_MULTIPLIER=2**(1/MOVE_DURATION)
global_variables=[]
temporary_variables=[]

COLORS = {"Variable":(155,155,0),
		  "Integer":(255,255,255),
		  "Float":(100,100,255),
		  "TRUE":(0,255,0),
		  "FALSE":(255,0,0),
		  "LIST_BORDER":(200,0,200),
		  "LIST_ELEMENT":(200,0,200),
		  "CHAR":(255,255,100),
		  "CHAR_BG":(100,100,100),
		  "POINTER_BG":(100,100,100),
		  "FUNCTION":(0,0,200)}
def reset_draw_settings():
	"""This is necessary to keep things clean"""
	stroke(0)
	fill(0)
	strokeWeight(1)
	textSize(1)
class Variable:
	"""Var0iables are just for easy handling, there won't be any pure Variable object
	But maybe we can implement void variables, than they can be useful"""
	#STATIC VALUES----------------------------
	#It can be list of all Variables to easy acces or global Variables

	def __init__(self,name="",x=None,y=None,width=Variable_width,height=Variable_height):
		self.name=name
		self.height=height
		self.width=width
		self.x=int(x)
		self.y=int(y)
		self.X=x;self.Y=y #Just for rectangle in move function
		self.namespace=None	#I hope I don't need this but to be able to acces to namespace

		#Drawing
		self.move_frame=0
		self.scale=SCALE
		self.x_speed=0
		self.y_speed=0

	def set_namespace(self,namespace):	#namespace will be a Function objest
		self.namespace=namespace
	def __eq__(self,other):
		return self.value==other.value	
	def __ne__(self,other):
		return self.value!=other.value
	def __repr__(self):
		return self.name + "=" + str(self.value)

	#Drawing part
	def move(self,x,y):
		global MOVE_DURATION
		#divide movement to MOVE_DURATION. So in 10th frame it will be on half of the way
		#Going---------------------
		self.x += self.x_speed
		self.y += self.y_speed
		if self.move_frame==0:
			remaining_x = int(x)-self.x
			remaining_y = int(y)-self.y
			self.x_speed=remaining_x/MOVE_DURATION
			self.y_speed=remaining_y/MOVE_DURATION
			self.move_frame+=1
			return False
		elif self.move_frame<=MOVE_DURATION/2:
			self.scale*=SCALE_MULTIPLIER
			self.move_frame+=1
			return False
		else:
			self.scale/=SCALE_MULTIPLIER
			self.move_frame+=1
			if self.move_frame==MOVE_DURATION:
				self.x=x
				self.y=y
				self.move_frame=0
				self.scale=SCALE
				return True

	def display(self):
		pushMatrix()
		color = COLORS["Variable"]
		fill(color[0],color[1],color[2])
		stroke(color[0],color[1],color[2])
		scale(self.scale)
		rect(self.x,self.y,self.value,self.height)
		if self.name!="":
			textSize(10)
			text(self.name,self.x,self.y+self.height+15)
		popMatrix()
	#I couldn't remember difference between copy and deepcopy so I couldn't comment it
	def deepcopy(self):
		new_copy=copy.deepcopy(self)
		temporary_variables.append(new_copy)
		return new_copy
	def copy(self):
		new_copy=copy.copy(self)
		temporary_variables.append(new_copy)
		return new_copy
	def destroy(self):
		temporary_variables.remove(self)
		del self

'''
class Class(Variable):
	"""Let's not mess with this big guy here for a while"""
	pass
'''

class Number(Variable):
	"""A meeting point for Char,Float,Double,Integer"""
	def __init__(self,name,value=None,x=None,y=None,width=Variable_width,height=Variable_height):
		Variable.__init__(self,name,x,y,width,height)
		self.int_value=value
	def __lt__(self,other):
		return self.int_value<other.int_value
	def __gt__(self,other):
		return self.int_value>other.int_value
	def __le__(self,other):
		return self.int_value<=other.int_value
	def __ge__(self,other):
		return self.int_value>=other.int_value
	def __add__(self,other):
		return self.int_value+other.int_value
	def __sub__(self,other):
		return self.int_value-other.int_value
	def __mul__(self,other):
		return self.int_value*other.int_value
	#ERROR HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	#TypeError: unsupported operand type(s) for /: 'Float' and 'Float'
	def __div__(self,other):
		return self.int_value/other.int_value
	#ERROR HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	def __floordiv__(self,other):
		return self.int_value//other.int_value
	def __mod__(self,other):
		return self.int_value%other.int_value

class Float(Number):
	def __init__(self,name,value,x=None,y=None,width=Variable_width,height=Variable_height):
		Number.__init__(self,name,value//1,x,y,width,height)
		self.float_value=value%1
		self.value=value

	def display(self):
		
		pushMatrix()
		color = COLORS["Float"]
		fill(color[0],color[1],color[2])
		stroke(color[0],color[1],color[2])
		scale(self.scale)
		rect(self.x,self.y,self.int_value,self.height)	#integer
		rect(self.x+self.int_value,self.y+self.height,10,-int(self.float_value*self.height))	#floating part
		if self.name!="":
			textSize(10)
			text(self.name+"="+str(self.value),self.x,self.y+self.height+15)
		popMatrix()
		

	def __lt__(self,other):
		if type(other)==Float:
			return self.value<other.value	
		else:
			return self.value<other.int_value
	def __gt__(self,other):		
		if type(other)==Float:
			return self.value>other.value	
		else:
			return self.value>other.int_value
	def __le__(self,other):		
		if type(other)==Float:
			return self.value<=other.value	
		else:
			return self.value<=other.int_value
	def __ge__(self,other):
		if type(other)==Float:
			return self.value>=other.value	
		else:
			return self.value>=other.int_value
	def __add__(self,other):
		if type(other)==Float:
			return self.value+other.value	
		else:
			return self.value+other.int_value
	def __sub__(self,other):
		if type(other)==Float:
			return self.value-other.value	
		else:
			return self.value-other.int_value
	def __mul__(self,other):
		if type(other)==Float:
			return self.value*other.value	
		else:
			return self.value*other.int_value
	#ERROR HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	#TypeError: unsupported operand type(s) for /: 'Float' and 'Float'
	#def __div__(self,other):
	#	if type(other)==Float:
	#		return self.value/other.value	
	#	else:
	#		return self.value/other.int_value
	#ERROR HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	def __floordiv__(self,other):
		if type(other)==Float:
			return self.value//other.value	
		else:
			return self.value//other.int_value
	def __mod__(self,other):
		if type(other)==Float:
			return self.value%other.value	
		else:
			return self.value%other.int_value



class Double(Float):
	def __init__(self,name,value,x=None,y=None,width=Variable_width,height=Variable_height):
		Float.__init__(self,name,value,x,y,width,height)


class Integer(Number):
	def __init__(self,name,value,x=None,y=None,width=Variable_width,height=Variable_height):
		Number.__init__(self,name,value,x,y,width,height)
		self.value=self.int_value
	def display(self):
		pushMatrix()
		color = COLORS["Integer"]
		fill(color[0],color[1],color[2])
		stroke(color[0],color[1],color[2])
		scale(self.scale)
		rect(self.x,self.y,self.value,self.height)
		if self.name!="":
			textSize(10)
			text(self.name+"="+str(self.value),self.x,self.y+self.height+15)
		popMatrix()
	
"""	


CONTINUE HERE




CONTINUE HERE




CONTINUE HERE


"""

class Char(Number):
	char_size=30
	def __init__(self,name,value,x=None,y=None,width=Small_Variable_width,height=Variable_height):
		Number.__init__(self,name,ord(value),x,y,width,height)
		self.char_value=value
		self.value=self.int_value
	def __repr__(self):
		return self.name+"="+self.char_value+"("+str(self.value)+")"

	def display(self):
		pushMatrix()
		color = COLORS["CHAR_BG"]
		fill(color[0],color[1],color[2])
		stroke(color[0],color[1],color[2])
		scale(self.scale)
		rect(self.x,self.y,Char.char_size,self.height)
		
		
		
		color = COLORS["CHAR"]
		fill(color[0],color[1],color[2])
		stroke(color[0],color[1],color[2])
		textSize(12)		#SIZE SHOULD BE ABLE TO BE SELECTED
		
		text(str(self.value),self.x+5,int(self.y+Variable_height/2+5))
		textSize(10)
		if self.name!="":
			text(self.name+"="+str(self.value),self.x,self.y+self.height+15)
		popMatrix()
class Pointer(Variable):
	"""Actually no different than an Array object but it seems like doesn't have acces to all Variables inside"""
	pointer_count=0
	def __init__(self,type_,name,pointed_Variable,x=None,y=None,width=Small_Variable_width,height=Variable_height):
		Variable.__init__(self,name,x,y,width,height)
		self.type_=type_
		self.pointed_Variable=pointed_Variable
		self.size=0
		self.Variable_list=[]
		self.arrow_color=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

	def display(self):
		pushMatrix()
		scale(self.scale)
		color = COLORS["POINTER_BG"]
		fill(color[0],color[1],color[2])
		stroke(color[0],color[1],color[2])
		rect(self.x,self.y,self.width,self.height)
		
		
		
		color = COLORS["POINTER"]
		fill(color[0],color[1],color[2])
		stroke(color[0],color[1],color[2])
		#STAR
		line(self.x,self.y,self.x+self.width,self.y+self.height)					#LEFT-UP TO RIGHT-BOT
		line(self.x+self.width/2,self.y,self.x+self.width/2,self.y+self.height)		#TOP to BOT
		line(self.x+self.width,self.y,self.x,self.y+self.height)					#RIGHT-UP TO LEFT-BOT
		line(self.x,self.y+self.height/2,self.x+self.width,self.y+self.height/2)	#LEFT to RIGHT
		
		#HOW TO POINT
		if type(self.value)!=None:
			color=self.arrow_color
			fill(color[0],color[1],color[2])
			stroke(color[0],color[1],color[2])
			line(self.x-5,self.y+self.height/3,self.pointed_Variable.x+self.pointed_Variable.width/2,self.pointed_Variable.y+self.pointed_Variable.height/2) #pointer side

		textSize(10)
		if self.name!="":
			text(self.name+"="+self.pointed_Variable.name,self.x,self.y+self.height+15)
		
		popMatrix()
	def __getitem__(self,key):
		return self.Variable_list[key]
	def __setitem__(self,key,value):
		self.Variable_list[key]=value

class Array(Pointer):

	def __init__(self,type_,name,Variables=[],x=None,y=None,width=Variable_width,height=Variable_height):
		size=len(Variables)
		if size == 0:
			Pointer.__init__(self,type_,name,None,x,y,width,height,)
		else:
			Pointer.__init__(self,type_,name,Variables[0],x,y,width,height)
		self.size=size
		self.Variable_list=Variables

class Boolean(Variable):
	"""Probably will look like a lever"""
	def __init__(self,name,value,x=None,y=None,width=Small_Variable_width,height=Variable_height): #Boolean size should be smaller than other variables
		#Placing factor depends on namespace and bool won't be used for start
		Variable.__init__(self,name,x,y,width,height)
		self.value=value
	def inverse(self):
		return not self.value
	def invert(self):
		self.value=not self.value
	def __and__(self,other):
		return self.value and other.value
	def __or__(self,other):
		return self.value or other.value
