# 導入pygame 模組
import pygame

# 調用pygame 初始化
pygame.init()

# 創造一個windows
# 參數是tuple （height，width）

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width,win_height))

# 幫windows 起個名字。
pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

# 'pics/R1.png'
# 9 副图片  0 - 8
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')

char = pygame.image.load('standing.png')

x = 50
y = 400
width = 64
height = 64
vel = 10   # velocity 速度

isJump = False

jumpCount = 10  # 跳躍速度

jumpLoop = 0
jumpvel = 20

left = False
right = False
walkCount = 0


def redrawGameWindow_1():

  win.blit(bg,(0,0))
  win.blit(char, (x,y))
  pygame.display.update() 

def redrawGameWindow_2():
  global walkCount

  if walkCount >= 9:
      walkCount = 0

  win.blit(bg,(0,0))
  win.blit(char, (x,y))
  print(walkCount)
  walkCount = walkCount+ 1

  pygame.display.update() 

def redrawGameWindow_3():

    # 想辦法讓walkCount 由 0 to 8.
    # 提示當 walkcount == 9的時候, 將她歸0.
  
    global walkCount
    win.blit(bg, (0,0)) 

    if walkCount  == len(walkRight) :  # 9 滿足此條件    
        walkCount = 0

    if left:  
        win.blit(walkLeft[walkCount], (x,y))  
        walkCount += 1                           
    elif right:
        win.blit(walkRight[walkCount], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))  # standing 
    pygame.display.update() 

  

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))  # This will draw our background image at (0,0)

    if walkCount == len(walkRight) * 3:   # 最多去到 0 to 26. , 27 / 3 = 9
        walkCount = 0

    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))  # We integer divide walkCounr by 3 to ensure each
        walkCount += 1                           # image is shown 3 times every animation
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))  # If the character is standing still
    pygame.display.update() 
    

# pygame main loop
run = True
while run:

    clock.tick(27)

    # 返回一個list, 其中包含所有鍵盤和滑鼠事件.
        # event.type 可以獲得該事件的類型, 例如按鍵按下，滑鼠移動等等. 如果 event.type 為pygame.QUIT 代表按下了關閉視窗的按鍵 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False  
# -----------------------------------------------------------------------------------
    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.    

    if keys[pygame.K_LEFT] and x - vel > 0:
        x -= vel
        left = True
        right = False    

    elif keys[pygame.K_RIGHT] and x + vel + width < win_width:
        x += vel
        left = False
        right = True   
    else: # not moving
        left = False
        right = False
        walkCount = 0

    if not(isJump): # Checks is user is not jumping

        if keys[pygame.K_SPACE]:
            isJump = True
    else: # 沒在跳躍的時候

        # 拋物線跳動
        # 循環21次,  jumcount = 10 開始 to -10
            #頭10次 y = y - jumcount**2 , 11次 y = y - 0 , 後10次 y = y  jumcount**2

        if True: 
            if jumpCount >= -10:
                y = y - (jumpCount * abs(jumpCount)) * 0.5   #  不想移動太多pixel 乘以0.5
                jumpCount = jumpCount - 1
            else: # This will execute if our jump is finished
                jumpCount = 10
                isJump = False


    redrawGameWindow()


pygame.quit()  # If we exit the loop this will execute and close our game