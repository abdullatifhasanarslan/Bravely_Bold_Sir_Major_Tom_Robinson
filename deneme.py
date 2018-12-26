from pyprocessing import *
import Variables

#CONSTANTS-----------------------------
WIDTH,HEIGHT = 1100,800
ORIJIN_X,ORIJIN_Y = 0,0
SCALE = 1


#FLOW CONTROLLERS----------------------
FLOW = True
line=[True,False,False,False,False,False,False,False,False,False,False,False,False,False]
action=[True,False,False,False]


"""
a=50
b=100
c=27.4
a+=b
c+=a
c+=c
"""

def setup():
	size(WIDTH,HEIGHT)#resizable=True,fullscreen=True)
	background(0,0,0)

def draw():
	global a,b,c,d,e,f,g,h,j,temp,ORIJIN_X,ORIJIN_Y,SCALE,FLOW

	#FOR DISPLAY----------------------
	background(0,0,0)
	translate(ORIJIN_X,ORIJIN_Y)
	scale(SCALE)
	stroke(255)
	rect(0,0,WIDTH,HEIGHT)
	stroke(0)
	#ALL FLOW GOES FROM HERE----------
	if FLOW:
		if line[0]:
			#a=50	int assignment
			a = Variables.Integer(value=50,name="a")
			line[0]=False;line[1]=True
		elif line[1]:
			#b=100	int assignment
			b = Variables.Integer(value=100,name="b")
			line[1]=False;line[2]=True
		elif line[2]:
			#c=27.4	float assignment
			c = Variables.Float(value=27.4,name="c")
			z = Variables.Integer(value=100,name="z")
			x = Variables.Integer(value=100,name="x")
			y = Variables.Integer(value=100,name="y")
			v = Variables.Integer(value=100,name="v")
			w = Variables.Integer(value=100,name="w")
			q = Variables.Integer(value=100,name="q")
			h = Variables.Integer(value=100,name="h")
			j = Variables.Integer(value=100,name="j")
			k = Variables.Integer(value=100,name="k")
			l=Variables.Char(value="l")
			line[2]=False;line[3]=True
		elif line[3] :
			#a+=b 	int+=int
			if action[0] and a.move(WIDTH/2,HEIGHT/2):
				action[0]=False;action[1]=True
			elif action[1]:
				temp=Variables.Integer(value=b.value,x=b.x,y=b.y,name="copy b")
				action[1]=False;action[2]=True
			elif action[2]:
				if a.value <= Variables.Variable.max_size:
					if temp.move(WIDTH/2+a.value,HEIGHT/2):
						a.value+=temp.value
						temp.destroy()
						action[2]=False;action[3]=True
				else:
					if temp.move(WIDTH/2+Variables.Variable.max_size,HEIGHT/2):
						a.value+=temp.value
						temp.destroy()
						action[2]=False;action[3]=True
			elif action[3] and a.move(a.X,a.Y):
				action[3]=False;action[0]=True
				line[3]=False;line[4]=True
		elif line[4]:
			#c+=a 	float+=int
			if action[0]:
				if a.value <= Variables.Variable.max_size:
					if c.move(WIDTH/2+a.value,HEIGHT/2):
						action[0]=False;action[1]=True
				else:
					if c.move(WIDTH/2+Variables.Variable.max_size,HEIGHT/2):
						action[0]=False;action[1]=True
			elif action[1]:
				temp=Variables.Float(value=float(a.value),x=a.x,y=a.y,name="copy a")
				action[1]=False;action[2]=True
			elif action[2] and temp.move(WIDTH/2,HEIGHT/2):
				c.value+=temp.value
				c.integer=int(c.value)
				c.decimal=c.value%1
				c.x=temp.x
				temp.destroy()
				action[2]=False;action[3]=True
			elif action[3] and c.move(c.X,c.Y):
				action[3]=False;action[0]=True
				line[4]=False;line[5]=True
		elif line[5]:
			#c+=c float+=float<self>
			if action[0]:
				if c.value <= Variables.Variable.max_size:
					if c.move(WIDTH/2+c.value,HEIGHT/2):
						action[0]=False;action[1]=True
				else:
					if c.move(WIDTH/2+Variables.Variable.max_size,HEIGHT/2):
						action[0]=False;action[1]=True
			elif action[1]:
				temp=Variables.Float(value=float(c.value),x=c.x,y=c.y,name="copy c")
				action[1]=False;action[2]=True
			elif action[2] and temp.move(WIDTH/2,HEIGHT/2):
				c.value+=temp.value
				c.integer=int(c.value)
				c.decimal=c.value%1
				c.x=temp.x
				temp.destroy()
				action[2]=False;action[3]=True
			elif action[3] and c.move(c.X,c.Y):
				action[3]=False;action[0]=True
				line[5]=False;line[6]=True
		elif line[6] :
			#d=True
			d = Variables.Bool(value=True,name="d")
			line[6]=False;line[7]=True
		elif line[7]:
			#e=False
			e = Variables.Bool(value=False,name="e")
			line[7]=False;line[8]=True
		elif line[8]:
			#f=None
			f=Variables.Bool(value=None,name="f")
			line[8]=False;line[9]=True
		elif line[9]:
			g=Variables.List(value=[Variables.Char("B"),
				Variables.Char("R"),
				Variables.Char("A"),
				Variables.Char("V"),
				Variables.Char("E"),
				Variables.Char(" "),
				Variables.Char("S"),
				Variables.Char("I"),
				Variables.Char("R"),
				Variables.Char(" "),
				Variables.Char("R"),
				Variables.Char("O"),
				Variables.Char("B"),
				Variables.Char("I"),
				Variables.Char("N")],name="g")
			line[9]=False;line[10]=True
		elif line[10]:
			h=Variables.List(value=[Variables.Integer(value=100,name="z"),
			Variables.Integer(value=100,name="x"),
			Variables.Integer(value=100,name="y"),
			Variables.Integer(value=100,name="v"),
			Variables.Integer(value=100,name="w"),
			Variables.Integer(value=100,name="q"),
			Variables.Integer(value=100,name="h"),
			Variables.Integer(value=100,name="j"),
			Variables.Integer(value=100,name="k")],name="h")
			line[10]=False;line[11]=True
		elif line[11]:
			temp_y=g.value[len(g.value)-1].y
			for i in range(len(g.value)-1,0,-1):
				g.value[i].y=g.value[i-1].y
			g.value[0].y=temp_y

			temp=g.value[0]
			for i in range(1,len(g.value)):
				g.value[i-1]=g.value[i]
			g.value[i]=temp

			#line[11]=False;line[12]=True
		"""
		elif line[11]:
			j=Variables.List(value=[a,b,f,g],name="g")
			line[11]=False;line[12]=True
		elif line[12]:
			a.value = mouse.x-50
		"""
		# elif line[9]:
		# 	#g=None	
		# 	g=Variables.Variable(name="g")
	
	#MOUSE BINDINGS------------------
	"""
	PRESS AND DRAG TO MOVE WORKSPACE
	"""
	if mouse.pressed:
		ORIJIN_X += mouse.x-pmouse.x
		ORIJIN_Y += mouse.y-pmouse.y

	#KEY BINDINGS--------------------
	"""
	F:FLOW
	R:RESET ORIJIN
	A:ZOOM IN
	S:ZOOM OUT
	"""
	if key.char == "f":		
		FLOW = not FLOW
		key.char = " "
	elif key.char == "r":
		ORIJIN_X,ORIJIN_Y=0,0
		key.char = " "
	elif key.char == "a":
		SCALE+=0.1
		key.char = " "
	elif key.char == "s":
		SCALE-=0.1
		key.char = " "
	"""	
	#I changed my mind. No scrolling for now.
	#It requires optimization with screen transformation and new variables
	
	elif key.code == UP or key.code == DOWN:
		e=1
		if Variables.Variable.variable_block_x<mouse.x and mouse.x<Variables.Variable.variable_block_x+Variables.Variable.variable_block_width: 
			if Variables.Variable.variable_block_y<mouse.y and mouse.y<Variables.Variable.variable_block_y+Variables.Variable.variable_block_height: 
				if key.code==UP:
					if 5<Variables.Variable.variable_block_y:
						Variables.Variable.variable_block_y-=e*5
				else:
					if Variables.Variable.variable_block_y+Variables.Variable.variable_block_height<HEIGHT-5:
						Variables.Variable.variable_block_y+=e*5
		key.code = " "
		key.char = " "
	"""	

	#FOR DISPLAY--------------------
	for variable in Variables.Variable.all_variables:
		variable.display()
	Variables.Variable.variableblock()



if __name__ == "__main__":
	run()
