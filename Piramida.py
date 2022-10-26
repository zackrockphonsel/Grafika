import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(0.0,500.0,0.0,500.0)

def drawPiramide():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(0.0,0.0,0.0)

    #segitiga bawah
    #glColor(0.0,1.0,0.0)
    glBegin(GL_TRIANGELS)
    glVertex2i(10,10)
    glVertex2i(50,10)
    glVertex2i(30,30)
    glEnd()
    glFlush()
    
    #segitiga kanan
    #glColor(0.0,1.0,0.0)
    glBegin(GL_TRIANGELS)
    glVertex2i(50,10)
    glVertex2i(30,50)
    glVertex2i(30,30)
    glEnd()
    glFlush()

    #segitiga kiri
    #glColor(0.0,1.0,0.0)
    glBegin(GL_TRIANGELS)
    glVertex2i(10,10)
    glVertex2i(30,30)
    glVertex2i(30,50)
    glEnd()
    glFlush()

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    drawPiramide()
    glPushMatrix()
    glTranslate(210, 210, 0) #proses translasi
    glRotate(50, 0, 0, 1) #proses rotasi
    glScalef(0.5, 0.5, 0) #proses skala
    drawPiramide()
    glPopMatrix()
    glFlush()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(10,10)
    glutCreateWindow("Piramide") #nama window
    glutDisplayFunc(render)
    init()
    glutMainLoop()

main()