import pygame
import time
import random
pygame.init()

dis_width=1000
dis_height=600
dis= pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game by DinhSang")

game_over=False

green=(0,255,0)
black=(0,0,0)
white=(255,255,255)
blue=(100,100,255)
red=(255,0,0)

snake_block=20
snake_speed=10

clock=pygame.time.Clock()


font_style=pygame.font.SysFont(None,40)
score_font=pygame.font.SysFont(None,35)

def Your_score(score,x,y):
    value=score_font.render("Your Score : " + str(score),True,green)
    dis.blit(value,[x,y])

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,blue,[x[0],x[1],snake_block,snake_block])

def our_snake1(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/6,dis_height/2.5])

def gameLoop():

    U=0
    L=0
    D=0
    R=0

    game_over=False
    game_close =False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list=[]

    length_of_snake=1

    foodx=round(random.randrange(0,dis_width-snake_block)/20.0)*20.0
    foody=round(random.randrange(0,dis_height-snake_block)/20.0)*20.0

    snake_List_rock=[]

    for i in range(25) :
        snake_rock = []
        x=round(random.randrange(0,dis_width-snake_block)/20.0)*20.0
        y=round(random.randrange(0,dis_height-snake_block)/20.0)*20.0
        #if x==foodx and y==foody : i-=1
        #elif x==dis_width / 2 and y== dis_height / 2 : i-=1
        #else :
        snake_rock.append(x)
        snake_rock.append(y)
            #for j in snake_List_rock[:-1]:
                #if j==snake_rock :
                    #i-=1
                    #break
                #else :
        snake_List_rock.append(snake_rock)
    #our_snake1(snake_block,snake_List_rock)
    while not game_over :
        while game_close :
            dis.fill(white)
            message("You lost ! press C to continue or press Q to quit !",red)
            Your_score(length_of_snake-1,dis_width/3,dis_height/3)
            pygame.display.update()

            for event in pygame.event.get() :
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q :
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        gameLoop()

        for event in pygame.event.get() :
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN :
                if event.key==pygame.K_LEFT:
                    if R==1 :
                        x1_change=snake_block
                        y1_change=0
                        U=0
                        D=0
                        R=1
                        L=0
                    else:
                        x1_change=-snake_block
                        y1_change=0
                        L=1
                        U=0
                        D=0
                        R=0
                if event.key==pygame.K_RIGHT:
                    if L==1:
                        x1_change=-snake_block
                        y1_change=0
                        L=1
                        U=0
                        D=0
                        R=0
                    else :
                        x1_change=snake_block
                        y1_change=0
                        R=1
                        L=0
                        D=0
                        U=0
                if event.key==pygame.K_UP:
                    if D==1 :
                        y1_change=snake_block
                        x1_change=0
                        D=1
                        L=0
                        R=0
                        U=0
                    else :
                        y1_change=-snake_block
                        x1_change=0
                        U=1
                        D=0
                        L=0
                        R=0
                if event.key==pygame.K_DOWN:
                    if U==1 :
                        y1_change=-snake_block
                        x1_change=0
                        U=1
                        D=0
                        L=0
                        R=0
                    else :
                        y1_change=snake_block
                        x1_change=0
                        D=1
                        U=0
                        L=0
                        R=0
        if x1<0 or x1>=dis_width or y1<0 or y1>=dis_height:
            game_close=True

        x1+=x1_change
        y1+=y1_change
        dis.fill(white)
        our_snake1(snake_block,snake_List_rock)
        pygame.draw.rect(dis,red,[foodx,foody,snake_block,snake_block])
        pygame.draw.rect(dis,blue,[x1,y1,snake_block,snake_block])

        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del(snake_list[0])
        for x in snake_List_rock[:-1]:
            if x==snake_head :
                game_close=True
        for x in snake_list[:-1]:
            if x==snake_head :
                game_close=True
        our_snake(snake_block,snake_list)
        Your_score(length_of_snake-1,0,0)

        pygame.display.update()

        if x1==foodx and y1== foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            length_of_snake+=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

