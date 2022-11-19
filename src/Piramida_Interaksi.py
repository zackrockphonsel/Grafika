import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

#Piramida Tranformation 2D

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-300,300.0,-300,300.0)

def drawPiramide():
    #glClear(GL_COLOR_BUFFER_BIT)
    glColor(0.0,0.0,0.0)

    #segitiga bawah
    glColor(0.0,1.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(10,10)
    glVertex2i(50,10)
    glVertex2i(30,30)
    glEnd()
    glFlush()
    
    #segitiga kanan
    glColor(0.0,1.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(50,10)
    glVertex2i(30,50)
    glVertex2i(30,30)
    glEnd()
    glFlush()

    #segitiga kiri
    glColor(0.0,1.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(10,10)
    glVertex2i(30,30)
    glVertex2i(30,50)
    glEnd()
    glFlush()

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)

    # translatation one
    drawPiramide()
    glPushMatrix()
    glTranslatef(ax,ay,1)
    glRotate(10,rx,ry,rz)
    glScalef(px,py,0)
    drawPiramide()
    glPopMatrix()

    glFlush()

def Tampil():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    render()
    glutSwapBuffers()
    
#ukuran object
px=0.5; py=0.5
ax=0; ay=0
rx=0; ry=0; rz=0

def myKeyboard(key,x,y):
    global px, py, ax, ay, rx, ry, rz
    if key == b'a': ax -= 50 #keyboard 'a' untuk bergeser ke kiri
    if key == b'b': ax += 50 #keyboard 'b' untuk bergeser ke kanan
    if key == b'c': ay -= 50 #keyboard 'c' untuk bergeser ke bawah
    if key == b'd': ay += 50 #keyboard 'd' untuk bergeser ke atas
    if key == b'e': px -= 0.1 #keyboard 'e' untuk berputar ke kiri (x)
    if key == b'f': px += 0.1 #keyboard 'f' untuk berputar ke kanan (x)
    if key == b'g': py -= 0.1 #keyboard 'g' untuk berputar ke bawah (y)
    if key == b'h': py += 0.1 #keyboard 'h' untuk berputar ke atas (y)
    
    glutPostRedisplay()    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(10,10)
    glutCreateWindow("Piramide") #nama window
    glutDisplayFunc(Tampil)
    glutKeyboardFunc(myKeyboard)
    init()
    glutMainLoop()

main()
