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

x = 50
y = 400
width = 40
height = 60
vel = 10   # velocity 速度

isJump = False

jumpCount = 10  # 跳躍速度

jumpLoop = 0
jumpvel = 20

# pygame main loop
run = True
while run:

    pygame.time.delay(100) 

    # 返回一個list, 其中包含所有鍵盤和滑鼠事件.
        # event.type 可以獲得該事件的類型, 例如按鍵按下，滑鼠移動等等. 如果 event.type 為pygame.QUIT 代表按下了關閉視窗的按鍵 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False  
# -----------------------------------------------------------------------------------
    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.    

    if keys[pygame.K_LEFT] and x - vel > 0:
        x -= vel    

    if keys[pygame.K_RIGHT] and x + vel + width < win_width:
        x += vel   

    if not(isJump): # Checks is user is not jumping
        if keys[pygame.K_UP] and y > vel:  # Same principles apply for the y coordinate
            y -= vel

        if keys[pygame.K_DOWN] and y + height + vel < win_height:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else: # 沒在跳躍的時候

        # 勻速跳動            
        # 利用 jumploop 循環20次，
        # 頭10次 y = y - jumpvel  
        # 後10次 y = y + jumpvel
        # （大 - 小） + 1  


        if False:                   # jumploop = 0
            if jumpLoop <  20:     # 滿足次條件 0 至 19 = 20 次
                if jumpLoop < 10:    #  0 to 9  10次
                    neg = 1
                else:               #剩下10次
                    neg = -1
                y = y - jumpvel * neg
                jumpLoop = jumpLoop + 1

            else:       
                jumpLoop = 0
                isJump = False


        # 拋物線跳動
        # 循環21次,  jumcount = 10 開始 to -10
            #頭10次 y = y - jumcount**2 , 11次 y = y - 0 , 後10次 y = y  jumcount**2

        if False: 
            if jumpCount >= -10:
                y = y - (jumpCount * abs(jumpCount)) * 0.5   #  不想移動太多pixel 乘以0.5
                jumpCount = jumpCount - 1
            else: # This will execute if our jump is finished
                jumpCount = 10
                isJump = False


        if True:                     # jumpcount = 10
            if jumpCount >=  -10:     # 滿足次條件 10 至 -10 = 21 次     10 - x + 1 = 21

                if jumpCount >= 1:    #  10 to 1 = 10 次
                    neg = 1
                elif jumpCount == 0: 
                    neg = 0
                else:  
                    neg = -1

                y = y - jumpCount * jumpCount * neg * 0.5
                jumpCount = jumpCount - 1
            else:
                jumpCount = 10
                isJump = False

    win.fill((255,255,255)) # 白色   # 紅綠藍


    pygame.draw.rect(win, (255,0,0), (x, y, width, height))  
    pygame.display.update() # This updates the screen so we can see our rectangle

pygame.quit()  # If we exit the loop this will execute and close our game