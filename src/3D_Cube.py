import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

#3D Object

anglePyramide = 0.0 #variable
refreshmills = 15 #variable

def initGL():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

def drawPiramide():
    global anglePyramide
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(1.5, 0.0, -7.0)
    glRotatef(anglePyramide, 1.0, 1.0, 1.0)
    glBegin(GL_QUADS)

    #hijau
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    #hijau
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    #merah
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    #merah
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    #biru
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    #biru
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glEnd()
    glutSwapBuffers()
    anglePyramide -= 0.15

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(refreshmills, timer, 0)

def reshape(width, height):
    if height == 0 :
        height = 1
    aspect = width / height

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, aspect, 0.1, 100.0)

def main():
    glutInit(sys.argv) #inisiasi GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500,500) #ukuran window
    glutInitWindowPosition(10,10) #posisi window
    glutCreateWindow("3D_Cube") #nama window
    glutDisplayFunc(drawPiramide)
    glutReshapeFunc(reshape)
    initGL()
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

main()