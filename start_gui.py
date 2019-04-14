from __future__ import print_function
import sys, math, time
from Tkinter import Tk, YES, BOTH
from Tkinter import *
from OpenGL import GL, GLU
from pyopengltk import OpenGLFrame
from drawing_algo import *

def play():
	class AppOgl(OpenGLFrame):
		def initgl(self):
			GL.glViewport( 0, 0, self.width, self.height)
			GL.glClearColor(0.0,0.0,0.0,0.0)
			GL.glColor3f(1.0,0.0, 0.0)
			GL.glPointSize(2.0)
			GL.glMatrixMode(GL.GL_PROJECTION)
			GL.glLoadIdentity()
			GLU.gluOrtho2D (0.0, 200.0, 0.0, 150.0)
		def redraw(self):
			GL.glClear(GL.GL_COLOR_BUFFER_BIT)
			GL.glBegin(GL.GL_POINTS)
			if (variable.get() == 'DDA Line Algorithm'):
				coor = map(int, ent.get().split(","))
				for p in pointDDA(coor[0],coor[1],coor[2],coor[3]):
        				GL.glVertex2f(p[0],p[1])
			elif (variable.get() == 'Bresenham Line Algorithm'):
				coor = map(int, ent.get().split(","))
				for p in pointbres(coor[0],coor[1],coor[2],coor[3]):
        				GL.glVertex2f(p[0],p[1])
			elif (variable.get() == 'Mid-point Circle Algorithm'):
				coor = map(int, ent.get().split(","))
				for p in circleMidpoint(coor[0],coor[1],coor[2]):
        				GL.glVertex2f(p[0],p[1])
			elif (variable.get() == 'Mid-point Ellipse Algorithm'):
				coor = map(int, ent.get().split(","))
				for p in ellipseMidpoint(coor[0],coor[1],coor[2],coor[3]):
        				GL.glVertex2f(p[0],p[1])
			else:
				pass
			GL.glEnd()
			GL.glFlush()
	app = AppOgl(root, width=500, height=400)
	app.grid(row=1,column=0)
	app.mainloop()
	
if __name__ == '__main__':
	OPTIONS = ['Choose a Algorithm', 'DDA Line Algorithm','Bresenham Line Algorithm','Mid-point Circle Algorithm','Mid-point Ellipse Algorithm' ]
	root = Tk()
	root.title("Assignment")
	variable = StringVar(root)
	variable.set(OPTIONS[0])
	w = OptionMenu(root, variable, *OPTIONS)
	w.grid(row=0, column=0)
	lab = Label(root, text="Coordinate", anchor='w')
	ent = Entry(root)
	ent.insert(0,"0")
	lab.grid(row=0, column=1)
	ent.grid(row=0, column=2)
	button = Button(root, text="Start", command=play)
	button.grid(row=0, column=3)
	root.mainloop()
