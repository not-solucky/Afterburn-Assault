from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


# importing Assets
from midpointCircle import drawCircle
from midpointLine import drawLine
from jet.jet import JET, JET_COLOR
from jetClass import Jet
from blinkblink import *

from button import Button, Text
from hpbar import HealthBar
# ===============Keyboard Listener================

def keyboard(key, x, y):
    
    global angle
    if key == b"q":
        angle = (angle + 10) % 360

def mouse(button, state, x, y):
    y = 800 - y
    global homepage, levelpage, gamepage, pausepage, gameoverpage, level, delay,animation_loop
    
    if homepage:
        if not delay[0]:
            if play_button.pressed(x, y):
                homepage = False
                levelpage = True
                delay = [True, (animation_loop-90)%100]
            if quitButton.pressed(x, y):
                glutLeaveMainLoop()
    elif levelpage:
        if not delay[0]:
            if level1_button.pressed(x, y):
                level = 1
                levelpage = False
                gamepage = True
            if level2_button.pressed(x, y):
                level = 2
                levelpage = False
                gamepage = True
            if backtoHomeButton.pressed(x, y):
                levelpage = False
                homepage = True
def BACKGROUND():
    for i in range(50):
        DRAWMATRIX.draw(starpos[i], STARBIG, STARCOLOR, 1)
        DRAWMATRIX.draw(starpos2[i], STARBIG, STARCOLOR2, 1)
    
    for i in meteor:
        if i[0][0] < 800:
            drawMeteor(i[0], i[1], i[2])
    
        
    for i in range(800):
        smallStar(starpos3[i], [0.4,0.098,0.819], 1)
        
def HOMEPAGE():
    Text.draw("AFTERBURN", [178, 650], [1,1,1], 7)
    Text.draw("ASSAULT", [228, 580], [1,1,1], 7)
    play_button.draw(True)
    quitButton.draw(True)
    
def LEVELPAGE():
    global animation_loop
    Text.draw("CHOOSE LEVEL", [190, 580], [1,1,0], 5)
    level1_button.draw(True)
    level2_button.draw(True)
    backtoHomeButton.draw()
    Text.draw("HOME", [100, 714], [0,1,1], 4)
    
def GAMEPAGE():
    global animation_loop, level
    player.draw()
    player_healthbar.draw(player.health)
    if level == 1:
        Text.draw("LEVEL 1", [100, 700], [1,1,1], 5)
    elif level == 2:
        Text.draw("LEVEL 2", [100, 700], [1,1,1], 5)

def backgroundAnimation():
    for i in range(50):
        starpos[i][1] = (starpos[i][1] - 2) % 800
        starpos2[i][1] = (starpos2[i][1] - 3) % 800
    for i in range(800):
        starpos3[i][1] = (starpos3[i][1] - 1) % 800
        
    for i in meteor:
        i[0][1] = (i[0][1] - i[2]*1.5) 
        i[0][0] = (i[0][0] - i[2]) 
        if i[0][1] < -17*i[2] or i[0][0] < -17*i[2]:
            i[0][0] = random.randint(0,800)
            i[0][1] = 800
            i[2] = random.randint(1,3)
        
def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    global animation_loop, homepage, levelpage, gamepage, pausepage, gameoverpage
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClearColor(0.074, 0.0627, 0.16, 1.0)
    glLoadIdentity()
    iterate()  
    # draw  
    BACKGROUND()
    
    if homepage:
        HOMEPAGE()
    elif levelpage:
        LEVELPAGE()
    elif gamepage:
        GAMEPAGE()
    elif pausepage:
        pass
    elif gameoverpage:
        pass
    
    glutSwapBuffers()

def game():
    global animation_loop
    if animation_loop % 2 == 0:
        player.health -= 1
        if player.health <= 0:
            player.health = 100
            
def animate(value):
    global animation_loop, delay
    animation_loop = (animation_loop + 1) % 100
    
    backgroundAnimation()
    
    if delay[0]:
        if delay[1] == animation_loop:
            delay = [False, 0]
    if gamepage:
        game()
        

    glutPostRedisplay()
    glutTimerFunc(30, animate, 5)
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Afterburn Assault")
animation_loop = 0
# background
starpos = []
starpos2 = []
starpos3 = []
meteor = []
for i in range(50):
    starpos.append([random.randint(0,800), random.randint(0,800)])
    starpos2.append([random.randint(0,800), random.randint(0,800)])
for i in range(800):
    starpos3.append([random.randint(0,800), random.randint(0,800)])

meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
meteor.append([[random.randint(0,800), 800], [0.4,0.725,0.983], random.randint(1,3)])
# Page Logic
delay = [False, 0]
homepage = True
levelpage = False
gamepage = False
pausepage = False
gameoverpage = False
# Level Logic
level = 1
# ===================
# Button Logic - Homepage
play_button = Button([324,400], [0,1,0], 4, 3, ['PLAY'], [20,20])
quitButton = Button([324,300], [1,0,0], 4, 3, ['EXIT'], [20,20])

# Button Logic - Levelpage
level1_button = Button([282,400], [0,1,0], 4, 3, ['LEVEL 1'], [20,20])
level2_button = Button([282,300], [0,1,0], 4, 3, ['LEVEL 2'], [20,20])
# Universal Button
backtoHomeButton = Button([50,700], [0,1,1], 3, 1, [[0, 35, 0, 35, 35, 165, 35,165, 165, 165],[25, 50, 25, 0, 50, 50,0,0, 50, 0]], [5,5])


player = Jet([100,100], JET, JET_COLOR, 2)
player_healthbar = HealthBar(100,[50,10], [5,760])
glutDisplayFunc(showScreen)
animate(5)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)

glutMainLoop()