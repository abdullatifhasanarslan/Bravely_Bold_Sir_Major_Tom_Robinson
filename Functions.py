from pyprocessing import *
from Variables import *
import copy

VARIABLE_MARGIN=25


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

class Function:
	def __init__(self,name,function=None,*args,**kwargs,parent=None,x=0,y=0,width=600,height=0):
		#This part for Variable_block and can become an independent class
		self.variable_block_x=15
		self.variable_block_y=5
		self.variable_block_width=240
		self.variable_block_height=15
		
		#Drawing details
		self.name=name
		self.x=x
		self.y=y
		self.width=width
		self.height=height

		self.commands=[]
		self.variables=[]
		self.active=False
		self.active_height=height
		self.active_width=width
		self.passive_height=height
		self.passive_width=width
		self.parent=parent
		self.function=function
	def insert_command(command):
		self.commands.append(command)
	def insert_variable(variable):
		self.variables.append(variable)
		variable.x=(variable_block_width-Variable_width)/2
		variable.y=variable_block_height
		self.variable_block_height+=variable.height+VARIABLE_MARGIN
		self.height = self.variable_block_height+10 #2*variable_block_y up and down margin
		variable.set_namespace(self)
	def activate():
		self.active=True
	def deactivate():
		self.active=False
	def implement():
		self.function()
	def display():

class Command(Function):
	def __init__(self,command_text,function):
		"""function in here is the function which it is in"""
		self.command_text=command_text
		self.function=function
		function.insert_command(self)
class Block_opener(Command):
	def __init__(self,command_text,function):
		Command.__init__(command_text,function)
		self.end=None
	def set_end(end):
		self.end=end
class Block_closer(Command):
	def __init__(self,command_text,function):
		Command.__init__(command_text,function)
		self.start=None
	def set_start(end):
		self.start=start
class Pipe:
	"""Just a virtual class for draw function. Can be used for flow control in future"""
	def __init__(self):
		pass
	def draw(self):
		pass
class Curly_Bracket_Open(Pipe):
	"""Just for example"""
	def __init__(self):
		pass
	def draw(self):
		pass