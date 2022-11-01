import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


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

initTrans = 0.0
def animTrans() : #animasi translasi
    global initTrans #definisi var global
    glPushMatrix()
    glTranslate(0, initTrans, 0) # sumbu x,y,z
    drawPiramide()
    initTrans = initTrans + 1
    glPushMatrix()
    glFlush()

def timer() : #fungsi Timer
    glutPostRedisplay() #mengaktifkan display secara berkala (looping)
    glutTimerFunc(10, timer, 5) #mengaktifkan timer function
    glFlush()

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    animTrans()
    glFlush()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(10,10)
    glutCreateWindow("Piramide") #nama window
    glutDisplayFunc(render)
    glutTimerFunc(10, timer, 5)
    init()
    glutMainLoop()

main()