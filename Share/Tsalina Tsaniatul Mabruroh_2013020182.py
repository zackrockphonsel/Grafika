import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math 

px=0.5; py=0.5
ax=0; ay=0
rx=0; ry=0; rz=0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(0.0,600.0,0.0,600.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(0.0,0.0,0.0)
    glBegin(GL_LINE_LOOP)
    
    glVertex2f(20,20)
    glVertex2f(20,130)
    glVertex2f(10.5,130.5)
    glVertex2f(60,180)
    glVertex2f(100,140)
    glVertex2f(200,140)
    glVertex2f(220,120)
    glVertex2f(200,120)
    glVertex2f(200,20)
    glEnd()
    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(20,130)
    glVertex2f(10.5,130.5)
    glVertex2f(60,180)
    glVertex2f(100,140)
    glVertex2f(100.5,130.5)
    glVertex2f(100,130)
    glEnd()
    glFlush()
 
    glBegin(GL_LINE_LOOP)
    glVertex2f(20,20)
    glVertex2f(20,130)
    glVertex2f(100,130)
    glVertex2f(100,20)
    glEnd()
    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(30,20)
    glVertex2f(30,30)
    glVertex2f(90,30)
    glVertex2f(90,20)
    glEnd()
    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(40,30)
    glVertex2f(40,90)
    glVertex2f(80,90)
    glVertex2f(80,30)
    glEnd()
    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(110,60)
    glVertex2f(110,90)
    glVertex2f(140,90)
    glVertex2f(140,60)
    glEnd()
    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(160,60)
    glVertex2f(160,90)
    glVertex2f(190,90)
    glVertex2f(190,60)
    glEnd()
    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(100,120)
    glVertex2f(100,140)
    glVertex2f(200,140)
    glVertex2f(220,120)
    glVertex2f(200,120)
    glEnd()
    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(20,130)
    glVertex2f(60,170)
    glVertex2f(100,130)
    glEnd()
    glFlush()

    glBegin(GL_LINE_LOOP)
    glVertex2f(100,20)
    glVertex2f(100,30)
    glVertex2f(200,30)
    glVertex2f(200,20)
    glEnd()
    glFlush()

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    draw()
    glPushMatrix()
    glTranslatef(ax,ay,1)
    glRotate(10,rx,ry,rz)
    glScalef(px,py,0)
    draw()
    glPopMatrix()
    glFlush()    

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    render()
    glutSwapBuffers()

def button(key,x,y):
    global px, py, ax, ay, rx, ry, rz
    if key == b'a': ax -= 50
    if key == b'b': ax += 50
    if key == b'c': ay -= 50
    if key == b'd': ay += 50 
    if key == b'e': px -= 0.1
    if key == b'f': px += 0.1
    if key == b'g': py -= 0.1
    if key == b'h': py += 0.1 
    
    glutPostRedisplay()    

def main():
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Tsalina Tsaniatul Mabruroh")
        glutDisplayFunc(draw)
        init()
        glutDisplayFunc(display)
        glutKeyboardFunc(button)
        glutMainLoop()

main()