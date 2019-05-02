from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
c1 = 1
c2 = 0
c3 = 0
cores = ( (c2,c3,c1),(c1,c2,c3),(c3,c1,c2))
def funcao():
    PI = 3.1415926538
    t0 = -(PI/2)
    phi = 0
    r=9
    cont = PI/20
    j=0
    def s(u,v):
        return ((r * math.cos(u)) * math.cos(v), r * math.sin(u), (r*math.cos(u)) * math.sin(v))
    for i in range(0,20):

        glBegin(GL_TRIANGLE_STRIP)
        phi=0
        for i in range(0,100):
            glColor3fv(cores[j])
            j+=1
            if j== len(cores)-1:
                j=0
            glVertex3fv(s(t0,phi))
           # glVertex3fv(s(t0+cont,phi))
            phi += cont
            #r+=0.01
        glEnd()
        t0 += cont


def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(2, 1, 3, 0)
    funcao()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(5, timer, 1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(65,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-20)
glRotatef(45,1,1,1)
glutTimerFunc(5,timer,1)
glutMainLoop()
