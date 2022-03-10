import pygame
import random
#Initialization
pygame.init()
#Displaying Screen
screen=pygame.display.set_mode((620,620))
#Adding Caption
pygame.display.set_caption('Tic-Tac-Toe')
#Adding background
screen.fill((0,0,0))
#Creating row of buttons
first=pygame.draw.rect(screen,(170,170,170),[5,5,200,200])
second=pygame.draw.rect(screen,(170,170,170),[210,5,200,200])
third=pygame.draw.rect(screen,(170,170,170),[415,5,200,200])
#Creating second row of buttons
fourth=pygame.draw.rect(screen,(170,170,170),[5,210,200,200])
fifth=pygame.draw.rect(screen,(170,170,170),[210,210,200,200])
sixth=pygame.draw.rect(screen,(170,170,170),[415,210,200,200])
#Creating third row of buttons
seventh=pygame.draw.rect(screen,(170,170,170),[5,415,200,200])
eighth=pygame.draw.rect(screen,(170,170,170),[210,415,200,200])
ninth=pygame.draw.rect(screen,(170,170,170),[415,415,200,200])
#Board
board=[[0,0,0],[0,0,0],[0,0,0]]
#Corner buttons list
corner=[[0,0],[0,2],[2,0],[2,2]]
#Non-Corner buttons list
non_corner=[[0,1],[1,0],[1,2],[2,1]]
#Creating font
over_font=pygame.font.Font('freesansbold.ttf',32)
#Function returns the pos,where the player likely to win in next move
def win_in_next(playerId):
    row=0
    col=0
    d1=0
    d2=0
    for i in range(3):
        row=0
        col=0
        for j in range(3):
            #Checking for similar rows
            if board[i][j]==playerId:
                row+=1
            elif board[i][j]==0:
                x_r=j
            else:
                row=0
                x_r=-1
            #Checking for similar columns
            if board[j][i]==playerId:
                col+=1
            elif board[j][i]==0:
                x_c=j
            else:
                col=0
                x_c=-1
            #Checking for negative slope diagonal
            if i==j and board[i][j]==playerId:
                d1+=1
            elif i==j and  board[i][j]==0:
                x_di=i
                x_dj=j
            #Checking for positive slope diagonal
            if i+j==2 and board[i][j]==playerId:
                d2+=1
            elif i+j==2 and board[i][j]==0:
                x_di_2=i
                x_dj_2=j
        if row==2:
            row=0
            if x_r!=-1:
                return i,x_r
        if col==2:
            col=0
            if x_c!=-1:
                return x_c,i
    if d1==2:
        d1=0
        try:
            return x_di,x_dj
        except:
            pass
    if d2==2:
        d2=0
        try:
            return x_di_2,x_dj_2
        except:
            pass
    return -1,-1
#randomly select the corner and non-corner buttons
def mark_board():
    i=2
    j=2
    if board[1][1]==0:
        return 1,1
    elif len(corner)!=0:
        index=random.randint(0,len(corner)-1)
        while board[corner[index][0]][corner[index][1]]!=0:
            index=random.randint(0,len(corner)-1)
        i=corner[index][0]
        j=corner[index][1]
        #deletes the specified index from a list
        corner.pop(index)
        return i,j
    else:
        index=random.randint(0,len(non_corner)-1)
        while board[non_corner[index][0]][non_corner[index][1]]!=0:
            index=random.randint(0,len(non_corner)-1)
        i=non_corner[index][0]
        j=non_corner[index][1]
        non_corner.pop(index)
        return i,j
#Gameover function
def gameover():
    over=over_font.render("COMPUTER WINS!!",True,(0,0,255))
    screen.blit(over,(150,300))
#Draw game function
def draw_game():
    draw=over_font.render("DRAW GAME",True,(0,0,255))
    screen.blit(draw,(150,300))

flag=0
running=True
while running:
    #loops through all events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            #Checks whether left mouse button is pressed
            if pygame.mouse.get_pressed()[0]:
                #returns the positions of mouse pointer
                pos=pygame.mouse.get_pos()
                flag+=1
                #Checks the position of mouse pointer in a particular button
                if first.collidepoint(pos):
                    id1=-1
                    pygame.draw.circle(screen,(0,255,0),[100,100],50)
                    board[0][0]=1
                    for i in range(len(corner)):
                        if corner[i]==[0,0]:
                            id1=i
                    if id1!=-1:
                        corner.pop(id1)
                elif second.collidepoint(pos):
                    id1=-1
                    pygame.draw.circle(screen,(0,255,0),[300,100],50)
                    board[0][1]=1
                    for i in range(len(non_corner)):
                        if non_corner[i]==[0,1]:
                            id1=i
                    if id1!=-1:
                        non_corner.pop(id1)
                elif third.collidepoint(pos):
                    id1=-1
                    pygame.draw.circle(screen,(0,255,0),[500,100],50)
                    board[0][2]=1
                    for i in range(len(corner)):
                        if corner[i]==[0,2]:
                            id1=i
                    if id1!=-1:
                        corner.pop(id1)
                elif fourth.collidepoint(pos):
                    id1=-1
                    pygame.draw.circle(screen,(0,255,0),[100,300],50)
                    board[1][0]=1
                    for i in range(len(non_corner)):
                        if non_corner[i]==[1,0]:
                            id1=i
                    if id1!=-1:
                        non_corner.pop(id1)
                elif fifth.collidepoint(pos):
                    pygame.draw.circle(screen,(0,255,0),[300,300],50)
                    board[1][1]=1
                elif sixth.collidepoint(pos):
                    id1=-1
                    pygame.draw.circle(screen,(0,255,0),[500,300],50)
                    board[1][2]=1
                    for i in range(len(non_corner)):
                        if non_corner[i]==[1,2]:
                            id1=i
                    if id1!=-1:
                        non_corner.pop(id1)
                elif seventh.collidepoint(pos):
                    id1=-1
                    pygame.draw.circle(screen,(0,255,0),[100,500],50)
                    board[2][0]=1
                    for i in range(len(corner)):
                        if corner[i]==[2,0]:
                            id1=i
                    if id1!=-1:
                        corner.pop(id1)
                elif eighth.collidepoint(pos):
                    id1=-1
                    pygame.draw.circle(screen,(0,255,0),[300,500],50)
                    board[2][1]=1
                    for i in range(len(non_corner)):
                        if non_corner[i]==[2,1]:
                            id1=i
                    if id1!=-1:
                        non_corner.pop(id1)
                elif ninth.collidepoint(pos):
                    id1=-1
                    pygame.draw.circle(screen,(0,255,0),[500,500],50)
                    board[2][2]=1
                    for i in range(len(corner)):
                        if corner[i]==[2,2]:
                            id1=i
                    if id1!=-1:
                        corner.pop(id1)
                if flag==9:
                    draw_game()
                    running=False
        if event.type==pygame.MOUSEBUTTONUP:
            flag+=1
            pos_x,pos_y=win_in_next(2)
            if pos_x!=-1 and pos_y!=-1:
                pygame.draw.rect(screen,(255,0,0),[pos_y*200+50,pos_x*200+50,100,100])
                board[pos_x][pos_y]=2
                gameover()
                break
            else:
                pos_x,pos_y=win_in_next(1)
                if pos_x!=-1 and pos_y!=-1:
                    id10=-1
                    id11=-1
                    pygame.draw.rect(screen,(255,0,0),[pos_y*200+50,pos_x*200+50,100,100])
                    board[pos_x][pos_y]=2
                    for i in range(len(corner)):
                        if corner[i]==[pos_x,pos_y]:
                            id10=i
                    if id10!=-1:
                        corner.pop(id10)
                    for i in range(len(non_corner)):
                        if non_corner[i]==[pos_x,pos_y]:
                            id11=i
                    if id11!=-1:
                        non_corner.pop(id11)
                else:
                    pos_x,pos_y=mark_board()
                    pygame.draw.rect(screen,(255,0,0),[pos_y*200+50,pos_x*200+50,100,100])
                    board[pos_x][pos_y]=2
    pygame.display.update()
