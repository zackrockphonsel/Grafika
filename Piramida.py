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
    glColor(0.0,1.0,0.0)
    glBegin(GL_TRIANGELS)
    glVertex2i(10,10)
    glVertex2i(50,10)
    glVertex2i(30,30)
    glEnd()
    glFlush()
    
    #segitiga kanan
    glColor(0.0,1.0,0.0)
    glBegin(GL_TRIANGELS)
    glVertex2i(50,10)
    glVertex2i(30,50)
    glVertex2i(30,30)
    glEnd()
    glFlush()

    #segitiga kiri
    glColor(0.0,1.0,0.0)
    glBegin(GL_TRIANGELS)
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
    glTranslate(210, 210, 0)
    glRotatef(45.0, 0.0, 0.0, 1.0)
    glScalef(0.5, 0.5, 0.5)
    drawPiramide()
    glPopMatrix()

    # translatation two
    drawPiramide()
    glPushMatrix()
    glTranslate(560, 540, 0)
    glRotatef(190.0, 0.0, 0.0, 1.0)
    glScalef(0.25, 0.25, 0.25)
    drawPiramide()
    glPopMatrix()

    # translatation three
    drawPiramide()
    glPushMatrix()
    glTranslate(530, 575, 0)
    glRotatef(260.0, 0.0, 0.0, 1.0)
    glScalef(0.15, 0.15, 0.15)
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
