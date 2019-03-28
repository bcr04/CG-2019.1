from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 
 
#cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
cores = ((0.4, 0.4, 0.4),(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (0.0, 1.0, 1.0),(1.0, 0.0, 1.0), (1.0, 1.0, 0.0), (1.0, 1.0, 1.0), (0.0, 0.0, 0.0), (0.5, 0.0, 0.0), (0.0, 0.5, 0.0), (0.0, 0.0, 0.5),(0.0, 0.5, 0.5), (0.5, 0.0, 0.5), (0.5, 0.5, 0.0), (0.8, 0.8, 0.8))

# http://www.nongnu.org/pyformex/doc-1.0/ref/opengl.colors.html
#    darkgrey = (0.4, 0.4, 0.4) -> 0.133
#         red = (1.0, 0.0, 0.0) -> 0.213
#       green = (0.0, 1.0, 0.0) -> 0.715
#        blue = (0.0, 0.0, 1.0) -> 0.072
#        cyan = (0.0, 1.0, 1.0) -> 0.787
#     magenta = (1.0, 0.0, 1.0) -> 0.285
#      yellow = (1.0, 1.0, 0.0) -> 0.928
#       white = (1.0, 1.0, 1.0) -> 1.000
#       black = (0.0, 0.0, 0.0) -> 0.000
#     darkred = (0.5, 0.0, 0.0) -> 0.046
#   darkgreen = (0.0, 0.5, 0.0) -> 0.153
#    darkblue = (0.0, 0.0, 0.5) -> 0.015
#    darkcyan = (0.0, 0.5, 0.5) -> 0.169
# darkmagenta = (0.5, 0.0, 0.5) -> 0.061
#  darkyellow = (0.5, 0.5, 0.0) -> 0.199
#   lightgrey = (0.8, 0.8, 0.8) -> 0.604

def prismaPoligono(rBase, nBase ,altura):
    
# pode gerar a aprox. de um cilindro, conforme nLadosBase aumenta
    nLadosBase = nBase
    height = altura
    radius = rBase
    
# desenhar a base
    glBegin(GL_POLYGON)
    for vertice in range(0, nLadosBase):  
        # Escolhe a cor
        glColor3fv(cores[vertice%len(cores)])   
        # divide em nLadosBase para desenhar os triangulos que compoem a base
        glVertex3fv([math.cos(2* math.pi * vertice/nLadosBase) * radius, -1 , math.sin(2 * math.pi * vertice/nLadosBase) * radius])
    glEnd()
    
# desenhar acima da base
    glBegin(GL_TRIANGLE_STRIP)        
    for vertice in range(0, nLadosBase+1):   # nLadosBase+1 para fechar a tampa
        glColor3fv(cores[vertice%len(cores)])         
        glVertex3fv([math.cos(2* math.pi * vertice/nLadosBase) * radius, height, math.sin(2 * math.pi * vertice/nLadosBase) * radius])    
        glVertex3fv([math.cos(2* math.pi * vertice/nLadosBase) * radius, -1 , math.sin(2 * math.pi * vertice/nLadosBase) * radius])
    glEnd()

# desenhar tampa
    glBegin(GL_POLYGON)
    i=0
    for vertice in range(0, nLadosBase):     
        i+=1
        glColor3fv(cores[vertice%len(cores)])   
        #glColor3fv(cores[current_color[i]])       
        glVertex3fv([math.cos(2* math.pi * vertice/nLadosBase) * radius, height, math.sin(2 * math.pi * vertice/nLadosBase) * radius])
    glEnd()
                

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    prismaPoligono(1, 100, 1)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PRISMANBASE")
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(40,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
