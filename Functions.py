from pyprocessing import *
from Variables import *
import copy

scale_x = 620
scale_y = 30
WIDTH,HEIGHT = 900,800
SCALE=1
variable_size=30

COLORS = {"VARIABLE":(155,155,0),
		  "INTEGER":(255,255,255),
		  "FLOAT":(100,100,255),
		  "TRUE":(0,255,0),
		  "FALSE":(255,0,0),
		  "LIST_BORDER":(200,0,200),
		  "LIST_ELEMENT":(200,0,200),
		  "CHAR":(255,255,100),
		  "CHAR_BG":(50,50,50),
		  "FUNCTION":(0,0,200)}

action=[True,False,False,False,False,False]

deneme=1
inputs=[]
#Functions---------------------------------------
class Function:	
	ORIGINAL=False
	function_count = 0
	all_functions = []
	max_size = 500

	#Function height can also change. This is not enogh. Also functions should get wider depending on content
	#Functions will have their own variable blocks. So this is just for prototyping. All code should remade
	"""
	function_block_x=285
	function_block_y=5
	function_block_width=15
	function_block_height=265
	"""
	def __init__(self,input_number=0,output_number=0,x=-1,y=25,width=620,height=225,function=None,name="",temp=False):
		self.name = str(name)
		self.X, self.Y = int(x), int(y)
		self.x, self.y = int(x), int(y)
		self.width, self.height = int(width), int(height)
		self.input_number,self.output_number=input_number,output_number
		self.function=function
		Function.all_functions.append(self)
		"""
		if not temp:
			Function.function_block_width+=self.width+25
			Function.function_count+=1
		"""

		#For later use
		self.input_places=[]
		self.output_places=[]
		seperation=(self.height-self.input_number*variable_size)//(self.input_number+1)	
		k=seperation
		for i in range(self.input_number):
			self.input_places.append(k)
			k+=seperation+scale_y

		seperation=(self.height-self.output_number*variable_size)//(self.output_number+1)	
		k=seperation
		for i in range(self.output_number):
			self.output_places.append(k)
			k+=seperation+scale_y

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
	"""
	def functionblock():
		noFill()
		stroke(255)
		rect(Function.function_block_x,Function.function_block_y,Function.function_block_width,Function.function_block_height)
		stroke(0)
	"""
	def display(self):		
		stroke(0)
		fill(0)
		color = COLORS["FUNCTION"]
		strokeWeight(4)
		stroke(color[0],color[1],color[2])
		fill(color[0],color[1],color[2])
		line(self.x,self.y,self.x+self.width,self.y)									#TOP
		line(self.x,self.y+self.height,self.x+self.width,self.y+self.height)			#BOT
		rect(self.x+self.width/3,self.y,self.width/3,self.height)						#MID

		seperation=(self.height-self.input_number*variable_size)//(self.input_number+1)	#LEFT
		y=self.y
		x=self.x
		for i in range(self.input_number+1):
			line(x,y,x+20,y)						#top
			line(x,y,x,y+seperation)				#left
			line(x,y+seperation,x+20,y+seperation)	#bot
			y+=seperation+variable_size
		
		seperation=(self.height-self.output_number*variable_size)//(self.output_number+1)	#LEFT
		x=self.x+self.width
		y=self.y
		for i in range(self.output_number+1):												#RIGHT
			line(x,y,x-20,y)						#top
			line(x,y,x,y+seperation)				#right
			line(x,y+seperation,x-20,y+seperation)	#bot
			y+=seperation+variable_size													
		
		if self.name!="":
			textSize(10)
			text(self.name,self.x,self.y-15)

		fill(0)	#This is necessary because it effects whole program
		strokeWeight(2)

	def implement(self,*args):
		global deneme,inputs,return_value
		global WIDTH,HEIGHT
		if action[0]:
			deneme=Function(input_number=self.input_number,output_number=self.output_number,function=self.function,x=self.x,y=self.y,width=self.width,height=self.height,name=self.name,temp=True)
			inputs=[variable.deepcopy() for variable in args]
			action[0]=False;action[1]=True
		elif action[1]:
			action[1]=False;action[2]=True
		elif action[2] and all([inputs[i].move(deneme.x,deneme.y+deneme.input_places[i]) for i in range(len(inputs))]):
			action[2]=False;action[3]=True
		elif action[3]:
			if all([inputs[i].move(deneme.x+200,deneme.y+deneme.input_places[i]) for i in range(len(inputs))]):
				result = deneme.function(*inputs)
				if type(result) == None:
					action[3]=False;action[4]=True
				elif type(result) == type(0):
					return_value=Integer(value=result,x=deneme.x+200,y=deneme.y+deneme.output_places[0],temp=True)
				elif type(result) == type(5.2):
					return_value=Float(value=result,x=deneme.x+200,y=deneme.y+deneme.output_places[0],temp=True)
				for variable in range(len(inputs)):
					inputs[variable].destroy()
				action[3]=False;action[4]=True
		elif action[4] and return_value.move(deneme.x+deneme.width,deneme.y+deneme.output_places[0]):
			action[4]=False;action[5]=True
		elif action[5] and deneme.move(self.X,self.Y):
			action[0]=True;action[5]=False
			return return_value
		return False
	def deepcopy(self):
		new_copy=copy.deepcopy(self)
		Function.all_functions.append(new_copy)
		return new_copy
	def copy(self):
		new_copy=copy.copy(self)
		Function.all_functions.append(new_copy)
		return new_copy
	def destroy(self):
		Function.all_functions.remove(self)		
		"""
		Function.function_count-=1
		Function.function_block_width-=self.width+25
		"""
		del self
		

class Add(Function):
	
	def __init__(self,input_number=2,output_number=1,x=-1,y=25,width=scale_x,height=225,name="",temp=False):
		if x==-1:
			x=Function.function_count*(scale_x+25)+300
		def add(x,y):
			return x+y
		Function.__init__(self,x=x,y=y,input_number=input_number,output_number=output_number,function=add,name="ADDER",temp=temp)

class Assign(Function):
	def __init__(self,input_number=2,output_number=0,x=-1,y=25,width=scale_x,height=225,name="",temp=True):
		if x==-1:
			x=Function.function_count*(scale_x+25)+300
		def assign(x,y):
			x.value=y.value
		Function.__init__(self,x=x,y=y,input_number=input_number,output_number=output_number,function=assign,name="Assign",temp=temp)

	def display(self):
		stroke(0)
		fill(0)
		return
	def implement(self,*args):
		global deneme,right_side,return_value
		global WIDTH,HEIGHT
		if action[0]:
			right_side=args[1].deepcopy()
			action[0]=False;action[1]=True
		elif action[1] and right_side.move(right_side.X+300,right_side.Y):
			action[1]=False;action[2]=True
		elif action[2] and right_side.move(args[0].X+300,args[0].Y):
			action[2]=False;action[3]=True
		elif action[3] and right_side.move(args[0].X,args[0].Y):
			self.function(*args)
			right_side.destroy()
			action[3]=False;action[0]=True
			return True
		return False