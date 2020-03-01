import pygame, sys, random, math, pyautogui, time
from pygame.locals import *
from pygame import mixer

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
COLOR = (0, 0, 0)
moveLeft = moveRight = moveUp = moveDown = False
enemyYchange = 40
FPS = 144

# Initialize pygame
pygame.init()
print(pygame.display.get_init)

# FPS
mainClock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 1, 32)

# Background
background = pygame.image.load('back.png')

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title
pygame.display.set_caption('P1 by Mike-97(_Mike_97)')

# Player
PlayerImg = pygame.image.load('girl.png')
playerX = (WINDOWWIDTH / 2 - 16)
playerY = (WINDOWHEIGHT - 40)
i = 0

# Enemy
EnemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load('sci-fi.png'))
    enemyX.append(random.randint(0, WINDOWWIDTH - 32))
    enemyY.append(10)
    enemyX_change.append(1)

# Star ready you cant see star on the screen
# fire the star is currently moving
StarImg = pygame.image.load('kill.png') #kill
starX = playerX
starY = playerY
bullet_state = 'ready'

score_value = 0
font = pygame.font.Font('digital-7.ttf', 24)
textX = 10
textY = 10

# Game over text
g_o_font = pygame.font.Font('digital-7.ttf', 24)

# Def
def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text(x, y):
    over_text = font.render('GAME OVER!', True, (255, 255, 255))
    screen.blit(over_text, (x, y))

def terminate():
    pygame.quit()
    sys.exit()

def player(playerX, playerY):
    screen.blit(PlayerImg, (playerX, playerY))

def enemy(enemyX, enemyY, i):
    screen.blit(EnemyImg[i], (enemyX, enemyY))

def star(starX, starY):
    global bullet_state # we have acces to 'ready'
    bullet_state = 'fire'
    screen.blit(StarImg, (starX, starY - 40))

def isColission(enemyX, enemyY, starX, starY):
    distance = math.sqrt((math.pow(enemyX-starX,2))+(math.pow(enemyY-starY,2)))
    if distance < 27:
        return True
    else:
        return False

pygame.mouse.set_visible(False)
k = 1

# Main Loop
while True:
    screen.fill(COLOR)
    screen.blit(background, (0, 0))
    k += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                moveLeft = True
                moveRight = False
            if event.key == K_d or event.key == K_RIGHT:
                moveLeft = False
                moveRight = True
            if event.key == K_SPACE:
                if bullet_state is "ready":
                    star_s = mixer.Sound('laser.wav')
                    star_s.play()
                    starX = playerX
                    star(starX, starY)
            if event.key == K_ESCAPE:
                terminate()

        if event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                moveLeft = False
            if event.key == K_d or event.key == K_RIGHT:
                moveRight = False

        if event.type == MOUSEBUTTONDOWN:
            if bullet_state is "ready":
                star_s = mixer.Sound('laser.wav')
                star_s.play()
                starX = playerX
                star(starX, starY)

        if event.type == MOUSEMOTION:
            # If the mouse moves, move the player where to the cursor.
            playerX = event.pos[0]
            playerY = WINDOWHEIGHT - 40

    if moveLeft and playerX > 0:
        playerX -= 3
    if moveRight and playerX < WINDOWWIDTH - 32:
        playerX += 3

    # Enemy movement
    for i in range(num_of_enemies):

        if enemyY[i] > WINDOWHEIGHT - 64 or score_value == 20:
            for j in range(num_of_enemies):
                enemyY[j] = 5
            game_over_text(textX, textY + 32)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:                                                                                           # z movement 0.35 należy dać <= 0 ponieważ może wyjść 0.40 - > 0.05 - > -0.30 i nie zmiani kierunku
            enemyX_change[i] = 1
            enemyY[i] += enemyYchange
        if enemyX[i] >= WINDOWWIDTH - 32:
            enemyX_change[i] = -1
            enemyY[i] += enemyYchange

        # Collision
        collision = isColission(enemyX[i], enemyY[i], starX, starY)
        if collision:
            star_s = mixer.Sound('explosion.wav')
            star_s.play(1)
            starY = playerY
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(2, WINDOWWIDTH - 34)
            enemyY[i] = 10

        enemy(enemyX[i], enemyY[i], i)


    #Star movement
    if starY <= 0:
            starY = playerY
            bullet_state = 'ready'

    if bullet_state is 'fire':
        star(starX, starY)
        starY -= 5


    #pygame.draw.line(screen, (255, 0, 0), (playerX + 16, 0), (playerX + 16, WINDOWHEIGHT-32), 1)
    show_score(textX, textY)
    player(playerX, playerY)
    mainClock.tick(FPS)
    pygame.display.update()

















#Icons made by <a href="https://www.flaticon.com/authors/eucalyp" title="Eucalyp">Eucalyp</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# Icons made by <a href="https://www.flaticon.com/authors/eucalyp" title="Eucalyp">Eucalyp</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
#<a href="https://www.freepik.com/free-photos-vectors/background">Background photo created by freepik - www.freepik.com</a>