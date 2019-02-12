from pyprocessing import *
import Variables
import Functions
import random

"""
FLOAT=Variables.Float("FLOAT",20.34,0,0)
FLOAT2=Variables.Float("FLOAT2",20.90,0,75)
INTEGER=Variables.Integer("INTEGER",10,0,150)
INTEGER2=Variables.Integer("INTEGER2",10,0,225)
CHAR=Variables.Char("CHAR",'a',0,300)
CHAR2=Variables.Char("CHAR2",'b',500,300)
#BOOL=Variables.Boolean("BOOL",True)
#BOOL2=Variables.Boolean("BOOL2",True)
"""
#x,y=500,500
#test=True
current_function=None
#Just keep here
def setup():
	size(fullscreen=True,resizable=True)

def draw():
	global x,y,test
	background(0)




























	"""
	FLOAT.display()
	FLOAT2.display()
	INTEGER.display()
	INTEGER2.display()
	CHAR.display()
	CHAR2.display()
	if test and FLOAT.move(x,y):
		FLOAT.x=x
		FLOAT.y=y
		test=False
		x,y=random.randint(0,120),random.randint(0,580)
	"""
if __name__== "__main__":
	run()

'''
#Things to test
class Pointer(Variable):
	"""Actually no different than an Array object but it seems like doesn't have acces to all Variables inside"""
	pointer_count=0
	def __init__(self,type_,name,pointed_Variable,x=None,y=None,width=Small_Variable_width,height=Variable_height):
		Variable.__init__(self,name,x,y,width,height)
		self.type_=type_
		self.pointed_Variable=pointed_Variable
		self.size=0
		self.Variable_list=[]
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
		self.size=size.
		self.Variable_list=Variables


'''
