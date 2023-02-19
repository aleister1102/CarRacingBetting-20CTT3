import pygame, sys
from pygame.locals import *
from pygame import* 
import random
import time
import os
import menu
import minigame
WINDOWWIDTH = 850 # Chiều rộng cửa sổ
WINDOWHEIGHT = 600 # Chiều cao cửa sổ
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLACK = (  0,   0,   0)
pygame.init()
click=pygame.mixer.Sound('click.wav')
main_music=pygame.mixer.Sound('main.mp3')    

### Xác định FPS ###
FPS = 60
fpsClock = pygame.time.Clock()
#Tạo Console Game
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Animation')

##Biên trái
#Tỉ lệ gốc là 150/7 giữa 150 và 700
X_Marginleft = (3/14)*WINDOWWIDTH
#Vạch trắng ở biên
WHITELINE=(3/140)*WINDOWWIDTH
#Vạch phân cách
SEPERATOR=(1/140)*WINDOWWIDTH
#Kích thước làn xe
LANE=WINDOWWIDTH/10
#Hằng số căn chỉnh cho xe ra giữa làn
MID=LANE/4.5
#Kích thước xe
CARWIDTH = 50
CARHEIGHT = 80

##Tạo BG
BGSPEED = 5
BG = pygame.image.load('middle.png')
ST=pygame.image.load('status.png')
class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = BGSPEED
        self.img = BG
        self.img=pygame.transform.scale(self.img,(WINDOWWIDTH,WINDOWHEIGHT))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        #Khung thong tin
        self.status_width=int(X_Marginleft)
        self.status_height=int(WINDOWHEIGHT)
        self.status_x=WINDOWWIDTH-X_Marginleft
        self.status_y=0
        self.status_image=ST
        self.status_image=pygame.transform.scale(self.status_image,(self.status_width,self.status_height))
    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y-self.height)))
        DISPLAYSURF.blit(self.status_image,(int(self.status_x),int(self.status_y)))
    def update(self):
        self.y += self.speed
        if self.y > self.height:
            self.y -= self.height
bg = Background()

#Tạo vạch đích
BG1= pygame.image.load('finish.png')
class Final():
    def __init__(self):
        self.height= WINDOWHEIGHT-1
        #Biến số này để làm cho việc xuất hiện surface đích mượt mà hơn
        #Lấy kích thước cửa sổ trừ đi 1 số, việc xuất hiện vạch đích trước đó 1 pixel làm cho animation mượt hơn
        self.smooth=-self.height+1
        #Tỉ lệ gốc của BG là 600 cho chiều cao và 125 cho vạch đích
        #Công thức dưới biểu thị liên hệ giữa vạch đích và bất kỳ kích thước nào của BG
        self.surfaceheight= 200
        self.x=0
        self.y=0       
        self.speed=BGSPEED
        self.img=BG
        self.img=pygame.transform.scale(self.img,(WINDOWWIDTH,WINDOWHEIGHT))
        self.img1=BG1
        self.img1=pygame.transform.scale(self.img1,(WINDOWWIDTH,WINDOWHEIGHT))
        self.surface = pygame.Surface((WINDOWWIDTH,self.surfaceheight),pygame.SRCALPHA, 32)
            #các tham số thuộc pygame.Surface làm cho surface ẩn đi khi vào game
                #Khung thong tin
        self.status_width=int(X_Marginleft)
        self.status_height=int(WINDOWHEIGHT)
        self.status_x=WINDOWWIDTH-X_Marginleft
        self.status_y=0
        self.status_image=ST
        self.status_image=pygame.transform.scale(self.status_image,(self.status_width,self.status_height))
    
    def draw(self):       
        DISPLAYSURF.blit(self.img,(int(self.x),int(self.y)))
        DISPLAYSURF.blit(self.img1, (int(self.x), int(self.y-self.height)))
        DISPLAYSURF.blit(self.surface,(int(self.x),int(self.y-self.height)))
        DISPLAYSURF.blit(self.status_image,(int(self.status_x),int(self.status_y)))
    def update(self):      
        self.y+=self.speed
        if self.y > self.height:
            self.y= 0
        if self.y == 0:
            self.speed=0 
        if self.y-self.height < self.smooth:
            self.y=self.height=0    
fn=Final()

##Tạo xe
#Thông số cho chữ
font_text = pygame.font.SysFont('Rockwell',23)
user1='Trong'
user2='Phat'
user3='Son'
user4='Tuan'
user5='Quan'
TEXT_DISTANCE=75
IMG_DISTANCE=25
#Xe 5
CARIMG5=pygame.image.load('car_5.png')
class Car5():
    def __init__(self):
        self.y = WINDOWHEIGHT 
        self.x = X_Marginleft+WHITELINE+4*(LANE+SEPERATOR)+MID
        self.carwidth=CARWIDTH
        self.carheight=CARHEIGHT
        self.name='car5'
        self.tag='Quan'
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = CARIMG5
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
        ##Tạo chữ đi kèm xe##
        self.text_x=self.x-5
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(self.tag,True,WHITE)
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))
    def update(self):
        self.y -= random.randrange(1,3)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
car5 = Car5()
# Xe 4
CARIMG4=pygame.image.load('car_4.png')
class Car4():
    def __init__(self):
        self.y = WINDOWHEIGHT 
        self.x = X_Marginleft+WHITELINE+3*(LANE+SEPERATOR)+MID
        self.carwidth=CARWIDTH
        self.carheight=CARHEIGHT
        self.surface = CARIMG4
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
        self.name='car4'
        self.tag='Tuan'
        #Tạo chữ đi kèm xe##
        self.text_x=self.x
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(self.tag,True,WHITE)
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))
    def update(self):
        self.y -= random.randrange(1,3)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
car4 = Car4()
# Xe 3
CARIMG3= pygame.image.load('car_3.png')
class Car3():
    def __init__(self):
        self.y = WINDOWHEIGHT 
        self.x =X_Marginleft+WHITELINE+2*(LANE+SEPERATOR)+MID
        self.carwidth=CARWIDTH
        self.carheight=CARHEIGHT
        self.name='car3'
        self.tag='Son'
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = CARIMG3
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
        #Tạo chữ đi kèm xe##
        self.text_x=self.x
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(self.tag,True,WHITE)
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))
    def update(self):
        self.y -= random.randrange(1,3)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
car3 = Car3()
# Xe 2
CARIMG2= pygame.image.load('car_2.png')
class Car2():
    def __init__(self):
        self.y = WINDOWHEIGHT 
        self.x = X_Marginleft+WHITELINE+LANE+SEPERATOR+MID
        self.carwidth=CARWIDTH
        self.carheight=CARHEIGHT
        self.name='car2'
        self.tag='Phat'
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = CARIMG2
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
        #Tạo chữ đi kèm xe##
        self.text_x=self.x-5
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(self.tag,True,WHITE)
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))

    def update(self):
        self.y -= random.randrange(1,3)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
car2 = Car2()
# Xe 1
CARIMG1_0=pygame.image.load('car_1.png')
class Car1():
    def __init__(self):
        self.y = WINDOWHEIGHT 
        self.x=X_Marginleft+WHITELINE+MID
        self.carwidth = CARWIDTH
        self.carheight = CARHEIGHT
        self.name='car1'
        self.tag='Trong'
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = CARIMG1_0
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
       
        #Tạo chữ đi kèm xe##
        self.text_x=self.x-5
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(self.tag,True,WHITE)
        
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))
    
    def update(self):
        
        self.y -= random.randrange(1,3)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
car1 = Car1()

#Xử lý tạo buff random
BUFFDISTANCE= 2 *WINDOWHEIGHT
#Hằng số để canh giữa buff
#Cụ thể hơn là lấy (CARWIDTH - CARWIDTH/2)   
SCALEBUFF = CARWIDTH/2
BUFFIMG1 = pygame.image.load('buff_speed.png')
BUFFIMG2 = pygame.image.load('buff_teleport.png')
BUFFIMG3 = pygame.image.load('buff_return.png')
BUFFIMG4 = pygame.image.load('buff_x2.png')
BUFFIMG5=pygame.image.load('buff_gold.png')
BUFFSPEED=4
#Xếp hạng lúc đua
def car_rank(Rank,Rank_name):
    
    #print(Rank)
    #print(Rank_name)
    for i in range (4):
        for j in range(0,4-i):
            if Rank[j]>Rank[j+1]:
                Rank[j],Rank[j+1]=Rank[j+1],Rank[j]
                Rank_name[j],Rank_name[j+1]=Rank_name[j+1],Rank_name[j]
class rank1():
    def __init__(self,Rank_name):
        self.width=220
        self.height=60
        self.x=buff.x
        self.y=buff.y+buff.a_height
        self.text_x=buff.x+self.width/8
        self.text_y=self.y+self.height/4
        self.surface=pygame.Surface((self.width,self.height),pygame.SRCALPHA, 32)
        self.font_name='8-BIT WONDER.TTF'
        self.font=pygame.font.Font(self.font_name,30)
        self.order=self.font.render(Rank_name[0],True,WHITE)
        self.font2=pygame.font.Font(self.font_name,20)
        self.rank=self.font2.render('Ranking',True,WHITE)       
    def draw(self):
        DISPLAYSURF.blit(self.surface,(self.x,self.y))
        DISPLAYSURF.blit(self.rank,(self.text_x,self.text_y-20))
        DISPLAYSURF.blit(self.order,(self.text_x,self.text_y))
class rank2():
    def __init__(self,Rank_name):
        self.width=220
        self.height=60
        self.x=buff.x
        self.y=buff.y+buff.a_height+(self.height/1.5)
        self.text_x=buff.x+self.width/8
        self.text_y=self.y+self.height/4
        self.surface=pygame.Surface((self.width,self.height),pygame.SRCALPHA, 32)
        self.font_name='8-BIT WONDER.TTF'
        self.font=pygame.font.Font(self.font_name,30)
        self.order=self.font.render(Rank_name[1],True,WHITE)
        
    def draw(self):
        DISPLAYSURF.blit(self.surface,(self.x,self.y))
        DISPLAYSURF.blit(self.order,(self.text_x,self.text_y))
class rank3():
    def __init__(self,Rank_name):
        self.width=220
        self.height=60
        self.x=buff.x
        self.y=buff.y+buff.a_height+(self.height*2/1.5)
        self.text_x=buff.x+self.width/8
        self.text_y=self.y+self.height/4
        self.surface=pygame.Surface((self.width,self.height),pygame.SRCALPHA, 32)
        self.font_name='8-BIT WONDER.TTF'
        self.font=pygame.font.Font(self.font_name,30)
        self.order=self.font.render(Rank_name[2],True,WHITE)
        
    def draw(self):
        DISPLAYSURF.blit(self.surface,(self.x,self.y))
        DISPLAYSURF.blit(self.order,(self.text_x,self.text_y))
class rank4():
    def __init__(self,Rank_name):
        self.width=220
        self.height=60
        self.x=buff.x
        self.y=buff.y+buff.a_height+(self.height*3/1.5)
        self.text_x=buff.x+self.width/8
        self.text_y=self.y+self.height/4
        self.surface=pygame.Surface((self.width,self.height),pygame.SRCALPHA, 32)
        self.font_name='8-BIT WONDER.TTF'
        self.font=pygame.font.Font(self.font_name,30)
        self.order=self.font.render(Rank_name[3],True,WHITE)
        
    def draw(self):
        DISPLAYSURF.blit(self.surface,(self.x,self.y))
        DISPLAYSURF.blit(self.order,(self.text_x,self.text_y))
class rank5():
    def __init__(self,Rank_name):
        self.width=220
        self.height=60
        self.x=buff.x
        self.y=buff.y+buff.a_height+(self.height*4/1.5)
        self.text_x=buff.x+self.width/8
        self.text_y=self.y+self.height/4
        self.surface=pygame.Surface((self.width,self.height),pygame.SRCALPHA, 32)
        self.font_name='8-BIT WONDER.TTF'
        self.font=pygame.font.Font(self.font_name,30)
        self.order=self.font.render(Rank_name[4],True,WHITE)
        
    def draw(self):
        DISPLAYSURF.blit(self.surface,(self.x,self.y))
        DISPLAYSURF.blit(self.order,(self.text_x,self.text_y))
def Rank_announce(Rank_name):
            Rank1_announce= rank1(Rank_name)
            Rank1_announce.__init__(Rank_name)
            Rank1_announce.draw()
            Rank2_announce= rank2(Rank_name)
            Rank2_announce.__init__(Rank_name)
            Rank2_announce.draw()
            Rank3_announce= rank3(Rank_name)
            Rank3_announce.__init__(Rank_name)
            Rank3_announce.draw()
            Rank4_announce= rank4(Rank_name)
            Rank4_announce.__init__(Rank_name)
            Rank4_announce.draw()
            Rank5_announce= rank5(Rank_name)
            Rank5_announce.__init__(Rank_name)
            Rank5_announce.draw()

#Qua thực nghiệm thì thấy sau khi chuyển cảnh endgame xe bị chậm
#Hàm dưới đây có tác dụng gia tốc một đoạn nhỏ
def Accel(car):
#Nếu nới rộng khoảng xét random ra thì xe chạy sẽ nhanh hơn (Theo trực giác hiển thị)
#Muốn có nhu cầu xét thắng thua chính xác thì cho khoảng của random là (0,1)
    car.y-=random.randrange(1,2)

#Xử lý va chạm vạch đích
def collision(Rank,Rank_name):
    if (end_position(Rank,Rank_name)):
        return True
def end_position(Rank,Rank_name):
    if Rank[4]+CARHEIGHT<fn.y-fn.height+fn.surfaceheight:
        return True

#Xử lý buff
class Buff():
    
    def __init__(self):
        self.width = CARWIDTH/2
        self.height = CARHEIGHT/2
        self.buffimg=BUFFIMG1
        self.buffimg=pygame.transform.scale(self.buffimg,(int (self.width),int (self.height)))
        self.distance = BUFFDISTANCE
        self.speed=BUFFSPEED
        self.array =[]
        self.index = 0
        #Thông số cho bảng thông báo
        self.buff_x=WINDOWWIDTH-X_Marginleft/2-CARWIDTH/2
        self.buff_y=(5/36)*WINDOWHEIGHT-CARHEIGHT/2
        self.x=WINDOWWIDTH-X_Marginleft
        self.y=0
        self.a_width=X_Marginleft
        self.a_height=(5/24)*WINDOWHEIGHT
        self.surface=pygame.Surface((self.a_width,self.a_height),pygame.SRCALPHA, 32)
        self.font_name='8-BIT WONDER.TTF'
        self.font=pygame.font.Font(self.font_name,14)
        self.word = self.font.render('Current Buff ', True, (WHITE))
        self.wordsize=self.word.get_size()
        self.word_x=self.x+20
        self.word_y=self.y+self.a_height/8
        for i in range(5):    
            y=-CARHEIGHT-i*self.distance
            lane = random.randrange(0,5)
            self.array.append([lane,y])
    def draw(self):
        
        for i in range (5):
            x=int(X_Marginleft+WHITELINE+self.array[i][0]*(LANE+SEPERATOR)+SCALEBUFF)
            y=int (self.array[i][1])
            DISPLAYSURF.blit(self.buffimg,(x,y))
            DISPLAYSURF.blit(self.surface,(self.x,self.y))
            DISPLAYSURF.blit(self.word,(self.word_x,self.word_y))
            DISPLAYSURF.blit(self.buffimg, (self.buff_x,self.buff_y))
    def update(self):
        for i in range(5):
            self.array[i][1] += self.speed
        if self.array[0][1] > WINDOWHEIGHT:
            self.array.pop(0)
            y = self.array[3][1] - self.distance
            lane = random.randrange(0, 3)
            self.array.append([lane, y])
buff = Buff()
FLASH=20
def BuffApply(car,buff,player):
    if buff.index == 2:
            car.y-=FLASH
    if buff.index == 3:
            car.y+=FLASH
    if buff.index==4:
        if player.choose==car.name:
            player.bet*=2
    if buff.index==5:
        if player.choose==car.name:
            player.money+=100
    buff.array.pop(0)
    y = buff.array[3][1] - buff.distance
    lane = random.randrange(0, 3)
    buff.array.append([lane, y])
def BuffCheck(car, buff):
    carRect = [car.x, car.y, car.carwidth, car.carheight]
    for i in range(5):
        x = int (X_Marginleft+WHITELINE+buff.array[i][0]*(LANE+SEPERATOR)+SCALEBUFF)
        y = int (buff.array[i][1])
        buffRect = [x, y, buff.width, buff.height]
        if buffcollision(carRect, buffRect) == True:
            return True
    return False
def buffcollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False
def BuffControl(buff):
    choose=random.randint(1,5)
    if choose==1:
        buff.buffimg = BUFFIMG1
        buff.index=1
        stop=False
    if choose==2:
        buff.buffimg = BUFFIMG2
        buff.index=2
    if choose==4:
        buff.buffimg=BUFFIMG4
        buff.index=4
    if choose==3:
        buff.buffimg=BUFFIMG3
        buff.index=3
    if choose==5:
        buff.buffimg=BUFFIMG5
        buff.index=5
#Xử lý buff bổ sung
def buff_increase(index,car_increase,car,buff):
    if index!=0:
        #Gọi init ra để khởi tạo lại tọa độ cho xe thay thế
        car_increase.__init__()
        car_increase.draw()
        car_increase.update()
        if (car.update()==False):
            car.draw()
            car.update()
    else:
        car.draw()
        car.update()
def off_buff(buff,car_increase,car):
    #Tọa độ biểu thị xe ăn trọn buff
    if BuffCheck(car_increase,buff)==False:
        buff.array.pop(0)
        y = buff.array[3][1] - buff.distance
        lane = random.randrange(0, 3)
        buff.array.append([lane, y])
class Car1_increase():
    def __init__(self):
        self.y = car1.y 
        self.x=car1.x
        self.carwidth = CARWIDTH
        self.carheight = CARHEIGHT
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = CARIMG1_0
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
       
        #Tạo chữ đi kèm xe##
        self.text_x=self.x-5
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(user1,True,WHITE)
        
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))
    
    def update(self):
        #Tại sao để random(3,6) thì việc buff sau khi ăn không bị mất
        self.y -= random.randrange(8,9)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
        if self.y<car1.y-300:
            return False
car1_increase = Car1_increase()
class Car2_increase():
    def __init__(self):
        self.y = car2.y 
        self.x=car2.x
        self.carwidth = CARWIDTH
        self.carheight = CARHEIGHT
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = CARIMG2
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
       
        #Tạo chữ đi kèm xe##
        self.text_x=self.x-5
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(user2,True,WHITE)
        
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))
    
    def update(self):
        self.y -= random.randrange(8,9)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
        if self.y<car2.y-300:
            return False
car2_increase = Car2_increase()
class Car3_increase():
    def __init__(self):
        self.y = car3.y 
        self.x=car3.x
        self.carwidth = CARWIDTH
        self.carheight = CARHEIGHT
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = CARIMG3
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
       
        #Tạo chữ đi kèm xe##
        self.text_x=self.x-5
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(user3,True,WHITE)
        
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))
    
    def update(self):
        self.y -= random.randrange(8,9)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
        if self.y<car3.y-300:
            return False
car3_increase = Car3_increase()
class Car4_increase():
    def __init__(self):
        self.y = car4.y 
        self.x=car4.x
        self.carwidth = CARWIDTH
        self.carheight = CARHEIGHT
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = CARIMG4
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
       
        #Tạo chữ đi kèm xe##
        self.text_x=self.x-5
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(user4,True,WHITE)
        
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))
    
    def update(self):
        self.y -= random.randrange(8,9)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
        if self.y<car4.y-300:
            return False
car4_increase = Car4_increase()
class Car5_increase():
    def __init__(self):
        self.y = car5.y 
        self.x=car5.x
        self.carwidth = CARWIDTH
        self.carheight = CARHEIGHT
        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = CARIMG5
        self.surface=pygame.transform.scale(self.surface,(self.carwidth,self.carheight))
       
        #Tạo chữ đi kèm xe##
        self.text_x=self.x-5
        self.text_y=self.y + TEXT_DISTANCE
        self.text=font_text.render(user5,True,WHITE)
        
    def draw(self): 
        DISPLAYSURF.blit(self.surface, (self.x,self.y))
        DISPLAYSURF.blit(self.text,(self.text_x,self.text_y))
    
    def update(self):
        self.y -= random.randrange(8,9)
        self.text_y=self.y+TEXT_DISTANCE
        if WINDOWHEIGHT - self.y > WINDOWHEIGHT + 50:
            self.y = WINDOWHEIGHT
        if WINDOWHEIGHT - self.text_y > WINDOWHEIGHT + 50 + TEXT_DISTANCE:
            self.text_y=WINDOWHEIGHT+ TEXT_DISTANCE
        if self.y<car5.y-300:
            return False
car5_increase = Car5_increase()

AVA1=pygame.image.load('car_trong.png')
AVA1=pygame.transform.scale(AVA1,(int(X_Marginleft/1.5),50))
AVA2=pygame.image.load('car_phat.png')
AVA2=pygame.transform.scale(AVA2,(int(X_Marginleft/1.5),50))
AVA3=pygame.image.load('car_son.png')
AVA3=pygame.transform.scale(AVA3,(int(X_Marginleft/1.5),50))
AVA4=pygame.image.load('car_tuan.png')
AVA4=pygame.transform.scale(AVA4,(int(X_Marginleft/1.5),50))
AVA5=pygame.image.load('car_quan.png')
AVA5=pygame.transform.scale(AVA5,(int(X_Marginleft/1.5),50))
CURRCAR0=pygame.image.load('buff.png')
CURRCAR1=pygame.image.load('car_1.png')
CURRCAR2=pygame.image.load('car_2.png')
CURRCAR3=pygame.image.load('car_3.png')
CURRCAR4=pygame.image.load('car_4.png')
CURRCAR5=pygame.image.load('car_5.png')
CURRCAR1=pygame.transform.scale(CURRCAR1,(int(X_Marginleft/2),100))
CURRCAR2=pygame.transform.scale(CURRCAR2,(int(X_Marginleft/2),100))
CURRCAR3=pygame.transform.scale(CURRCAR3,(int(X_Marginleft/2),100))
CURRCAR4=pygame.transform.scale(CURRCAR4,(int(X_Marginleft/2),100))
CURRCAR5=pygame.transform.scale(CURRCAR5,(int(X_Marginleft/2),100))

#Dữ liệu người chơi
class Player():
    def __init__(self):
        #Xe dat cuoc
        self.choose=''
        #so tien cuoc
        self.bet=0
        #Duong dan
        self.path=''
        #Ten xe
        self.name =''
        #So tien hien co
        self.money=0
        #So bua hien co
        self.buff=0
        self.buff_use=0
        self.buff_use_index=0
        #Avatar
        self.ava_height=250
        self.ava_width=X_Marginleft
        self.ava_img=AVA1
        self.ava_x=WINDOWWIDTH-X_Marginleft+20
        self.ava_y=WINDOWHEIGHT-self.ava_height+5
        
        #Current Car
        self.curr_car_height=300
        self.curr_car_width=self.ava_width
        self.curr_car_img=CURRCAR0
        self.curr_car_x=self.ava_x
        self.curr_car_y=self.ava_y+90
        self.font_name='8-BIT WONDER.TTF'
        self.font_name2='Font2.TTF'
        self.font=pygame.font.Font(self.font_name,14)
        self.font2=pygame.font.Font(self.font_name2,19)
        self.word = self.font.render('Chosen Car ', True, (WHITE))
        self.wordsize=self.word.get_size()
        self.word_x=self.ava_x
        self.word_y=self.ava_y+70
        #Bet and Money
        self.font_name='8-BIT WONDER.TTF'
        self.font=pygame.font.Font(self.font_name,14)
        self.bet_word_curr = self.font.render('Bet', True, (WHITE))
        self.betsize=self.word.get_size()
        self.betword_x=self.ava_x+10
        self.betword_y=self.ava_y+200
        #Money
        self.moneyword_x=self.betword_x+50
        self.moneyword_y=self.betword_y
        self.money_word_curr=self.font.render('Money',True,(WHITE))
        #Name
        self.name_x=self.betword_x
        self.name_y=self.moneyword_y-20
        #Buff used
        self.buff_use_img_x=779
        self.buff_use_img_y=440
        self.buff_use_width=60
        self.buff_use_height=80
        self.buff_use_img=pygame.image.load('buff.png')
        self.buff_use_img=pygame.transform.scale(self.buff_use_img,(self.buff_use_width,self.buff_use_height))
    def bet888_play(self,Rank_name,path):
        if self.choose=='car1':
            if Rank_name[0]=='car1':
                self.money+=self.bet
            else:
                self.money-=self.bet
                if self.money<0:
                    self.money=0
        if self.choose=='car2':
            if Rank_name[0]=='car2':
                self.money+=self.bet
            else:
                self.money-=self.bet
                if self.money<0:
                    self.money=0

        if self.choose=='car3':
            if Rank_name[0]=='car3':
                self.money+=self.bet
            else:
                self.money-=self.bet
                if self.money<0:
                    self.money=0

        if self.choose=='car4':
            if Rank_name[0]=='car4':
                self.money+=self.bet
            else:
                self.money-=self.bet
                if self.money<0:
                    self.money=0

        if self.choose=='car5':
            if Rank_name[0]=='car5':
                self.money+=self.bet
            else:
                self.money-=self.bet
                if self.money<0:
                    self.money=0

        with open(path,'r+',encoding='utf-8') as f:
            data=f.readlines()
            print(data)
            data[2]=str(self.money)+'\n'
            data[3]=str(self.buff)+'\n'
            
        with open(path,'r+',encoding='utf-8') as f:
            for line in data:
                if line.strip('\n') !='\n':
                    f.write(line)
            print(self.money)
            print(data)
    def avatar(self,car1,car2,car3,car4,car5):
        x,y=pygame.mouse.get_pos()
        if x>car1.x and x<car1.x+CARWIDTH and y>car1.y and y>car1.y+CARHEIGHT:
            self.ava_img=AVA1
            DISPLAYSURF.blit(self.ava_img,(self.ava_x,self.ava_y))
        if x>car2.x and x<car2.x+CARWIDTH and y>car2.y and y>car2.y+CARHEIGHT:
            self.ava_img=AVA2
            DISPLAYSURF.blit(self.ava_img,(self.ava_x,self.ava_y))
        if x>car3.x and x<car3.x+CARWIDTH and y>car3.y and y>car3.y+CARHEIGHT:
            self.ava_img=AVA3
            DISPLAYSURF.blit(self.ava_img,(self.ava_x,self.ava_y))
        if x>car4.x and x<car4.x+CARWIDTH and y>car4.y and y>car4.y+CARHEIGHT:
            self.ava_img=AVA4
            DISPLAYSURF.blit(self.ava_img,(self.ava_x,self.ava_y))
        if x>car5.x and x<car5.x+CARWIDTH and y>car5.y and y>car5.y+CARHEIGHT:
            self.ava_img=AVA5
            DISPLAYSURF.blit(self.ava_img,(self.ava_x,self.ava_y))
    def current_car(self):
        if self.choose=='car1':
            self.curr_car_img=CURRCAR1
        if self.choose=='car2':
            self.curr_car_img=CURRCAR2
        if self.choose=='car3':
            self.curr_car_img=CURRCAR3
        if self.choose=='car4':
            self.curr_car_img=CURRCAR4
        if self.choose=='car5':
            self.curr_car_img=CURRCAR5
        DISPLAYSURF.blit(self.curr_car_img,(self.curr_car_x,self.curr_car_y))
        DISPLAYSURF.blit(self.word,(self.word_x,self.word_y))
    def current_money(self,money):
        self.money_word=self.font.render(str(money),True,WHITE)
        DISPLAYSURF.blit(self.money_word_curr,(self.moneyword_x,self.moneyword_y))
        DISPLAYSURF.blit(self.money_word,(self.moneyword_x,self.moneyword_y+20))
    def current_bet(self,bet):
        self.bet_word=self.font.render(str(bet),True,WHITE)
        DISPLAYSURF.blit(self.bet_word_curr,(self.betword_x,self.betword_y))
        DISPLAYSURF.blit(self.bet_word,(self.betword_x,self.betword_y+20))
    def current_name(self,name):
        self.name_word=self.font2.render(name,True,(WHITE))
        DISPLAYSURF.blit(self.name_word,(self.name_x,self.name_y))
    def recrent_buff(self):
        DISPLAYSURF.blit(self.buff_use_img,(self.buff_use_img_x,self.buff_use_img_y))

player=Player()

#Xử lý banner thắng thua
class Win_Lose():
    def __init__(self):
        self.x=int(X_Marginleft+WHITELINE)
        self.y=WINDOWHEIGHT
        self.width=int(WINDOWWIDTH-2*(X_Marginleft+WHITELINE))
        self.height= int(CARHEIGHT*2)
        self.win=pygame.image.load('win.png')
        self.win=pygame.transform.scale(self.win,(self.width,self.height))
        self.lose=pygame.image.load('lose.png')
        self.lose=pygame.transform.scale(self.lose,(self.width,self.height))
        self.img=pygame.image.load('middle.png')
        self.img=pygame.transform.scale(self.img,(WINDOWWIDTH,WINDOWHEIGHT))

    def draw(self,status):
        if status==1:
            DISPLAYSURF.fill(WHITE)
            DISPLAYSURF.blit(self.img,(0,0))
            DISPLAYSURF.blit(self.win,(self.x,self.y))
        if status==2:
            DISPLAYSURF.blit(self.img,(0,0))
            DISPLAYSURF.blit(self.lose,(self.x,self.y))
    def update(self):
            self.y-=10
            if self.y<WINDOWHEIGHT/2+self.height:
                return 
win_lose=Win_Lose() 
def checkwin(Rank_name,player):
    if Rank_name[0]==player.choose:
        return 1
    if Rank_name[0]!=player.choose:
        return 2
def Result(Rank_name,player):
    running=1;
    if (checkwin(Rank_name,player)==1):
                while running:
                    win_lose.draw(1)
                    win_lose.update()
                    if win_lose.y<WINDOWHEIGHT-win_lose.height:
                        time.sleep(1)
                        running=0
                    pygame.display.update()
                    fpsClock.tick(FPS)  
    if (checkwin(Rank_name,player)==2):
                while running:
                    win_lose.draw(2)
                    win_lose.update()
                    if win_lose.y<WINDOWHEIGHT-win_lose.height:
                        time.sleep(1)
                        running=0
                    pygame.display.update()
                    fpsClock.tick(FPS)  

#Xử lý buff khi được sử dụng
def buff_use(car,player,car_increase,buff):
    if player.buff<=0:
        return
    random_b=random.randint(1,5)
    
    if random_b!=1:
        BuffApplyv2(car,random_b,player)
        player.buff-=1
        player.buff_use_index=random_b
    else:
        buff_increase(1,car_increase,car,buff)
        player.buff-=1
        player.buff_use_index=1
def BuffApplyv2(car,index,player):
    print(player.buff)
    if index == 2:
            car.y-=FLASH
            print('Da su dung Flash')
    if index == 3:
            car.y+=FLASH
            print('Da su dung Back Flash')
    if index==4:
        if player.choose==car.name:
            player.bet*=2
            print('Da su dung x2 bet')
    if index==5:
        if player.choose==car.name:
            player.money+=100
            print('Da su dung plus money')

#Xử lý random làn xe
BASE=WHITELINE+X_Marginleft+MID
def lanecar1(car1,car2,car3,car4,car5):
    lane=random.randint(0,4)
    car1.x=BASE+lane*(LANE+SEPERATOR)
    car1.text_x=car1.x-5
    lanecar2(lane,car2,car3,car4,car5)
def lanecar2(lane,car2,car3,car4,car5):
    lane2=random.randint(0,4)
    while lane2==lane:
        lane2=random.randint(0,4)
    car2.x=BASE+lane2*(LANE+SEPERATOR)
    car2.text_x=car2.x-5
    lanecar3(lane,lane2,car3,car4,car5)
def lanecar3(lane,lane2,car3,car4,car5):
    lane3=random.randint(0,4)
    while lane3==lane or lane3==lane2:
        lane3=random.randint(0,4)
    car3.x=BASE+lane3*(LANE+SEPERATOR)
    car3.text_x=car3.x-5
    lanecar4(lane,lane2,lane3,car4,car5)
def lanecar4(lane,lane2,lane3,car4,car5):
    lane4=random.randint(0,4)
    while lane4==lane or lane4==lane2 or lane4==lane3:
        lane4=random.randint(0,4)
    car4.x=BASE+lane4*(LANE+SEPERATOR)
    car4.text_x=car4.x-5
    lanecar5(lane,lane2,lane3,lane4,car5)
def lanecar5(lane,lane2,lane3,lane4,car5):
    lane5=random.randint(0,4)
    while lane5==lane or lane5==lane2 or lane5==lane3 or lane5==lane4:
        lane5=random.randint(0,4)
    car5.x=BASE+lane5*(LANE+SEPERATOR)
    car5.text_x=car5.x-5

buffimg=pygame.image.load('buff.png')
#xử lý hiển thị thông tin buff lúc chơi
def buff_displayv2(index):
    if index==1:
        player.buff_use_img=BUFFIMG1
    if index==2:
        player.buff_use_img=BUFFIMG2
    if index==3:
        player.buff_use_img=BUFFIMG3
    if index==4:
        player.buff_use_img=BUFFIMG4
    if index==5:
        player.buff_use_img=BUFFIMG5
    
    DISPLAYSURF.blit(buffimg,(0,0))

#xử lý âm thanh
def sound(Rank_name,plyer):
    if checkwin(Rank_name,player)==1:
        pygame.mixer.Channel(1).stop()
        pygame.mixer

def Endgame():        
    running=1
    while running:
            fn.draw()
            fn.update()
            Accel(car1)
            car1.draw()
            car1.update() 
            Accel(car2)
            car2.draw()
            car2.update()
            Accel(car3)
            car3.draw()
            car3.update()
            Accel(car4)
            car4.draw()
            car4.update()
            Accel(car5)
            car5.draw()
            car5.update()
            
            player.current_car()
            player.current_money(player.money)
            player.current_bet(player.bet)
            player.current_name(player.name)
            player.recrent_buff()
            Rank = [car1.y,car2.y,car3.y,car4.y,car5.y]
            global Rank_name
            Rank_name = ['car1','car2','car3','car4','car5']
            car_rank(Rank,Rank_name)
            Rank_announce(Rank_name)
            player.avatar(car1,car2,car3,car4,car5)
            #Buff và skill apply
            #Tạo nút buff
            buff_use_x=784
            buff_use_x2=829
            buff_use_y=458
            buff_use_y2=507
            #Tạo nút skill
            skill_use_x=770
            skill_use_y=487
            skill_use_x2=831
            skill_use_y2=507

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                x,y=pygame.mouse.get_pos()
                if (x>buff_use_x and y>buff_use_y and x<buff_use_x2 and y<buff_use_y2):
                    if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1):
                        print(player.buff_use)
                        if player.buff_use <1:
                            print('Buff is used')
                            if car1.name==player.choose:
                                car=car1
                                car_increase=car1_increase
                            if car2.name==player.choose:
                                car=car2
                                car_increase=car2_increase
                            if car3.name==player.choose:
                                car=car3
                                car_increase=car3_increase
                            if car4.name==player.choose:
                                car=car4
                                car_increase=car4_increase
                            if car5.name==player.choose:
                                car=car5
                                car_increase=car5_increase
                            buff_use(car,player,car_increase,buff)
                            player.buff_use+=1
                            buff_displayv2(player.buff_use_index)
            
            if (collision(Rank,Rank_name)):
                player.bet888_play(Rank_name,player.path)
                print(Rank_name)
                running=0
                return 

            pygame.display.update()
            fpsClock.tick(FPS)  
    pygame.display.update()
    fpsClock.tick(FPS)  
def Gameplay():
    #Đếm ngược
    #Nếu ta để t= WINDOWHEIGHT (chiều cao của console),
    #Trùng hợp ta sẽ vẽ được xấp xỉ 4-6 BG mà ko bị giật
    t=WINDOWHEIGHT/5
    
    
    while t>0:
        t-=1
        DISPLAYSURF.fill(BLACK)
        bg.draw()
        bg.update()
        
        car1.draw()
        car1.update() 
        car2.draw()
        car2.update()
        car3.draw()
        car3.update()
        car4.draw()
        car4.update()
        car5.draw()
        car5.update()
        buff.draw()
        buff.update()
        
        player.current_car()
        player.current_money(player.money)
        player.current_bet(player.bet)
        player.current_name(player.name)
        player.recrent_buff()
        Rank = [car1.y,car2.y,car3.y,car4.y,car5.y]
        Rank_name = ['car1','car2','car3','car4','car5']
        car_rank(Rank,Rank_name)
        Rank_announce(Rank_name)
        player.avatar(car1,car2,car3,car4,car5)

        if BuffCheck(car1,buff):
            if buff.index==1:
                print('Xe 1 co buff tang toc')
                buff_increase(1,car1_increase,car1,buff)
                off_buff(buff,car1_increase,car1)
            if buff.index==2:
                print('Xe 1 co buff toc bien')
                BuffApply(car1,buff,player)
            if buff.index==4:
                print('Xe 1 co buff nhan doi so tien cuoc')
                BuffApply(car1,buff,player)
            if buff.index==3:
                print('Xe 1 co buff dich chuyen lui')
                BuffApply(car1,buff,player)
            if buff.index==5:
                print('Xe 1 co buff cong them tien')
                BuffApply(car1,buff,player)
        if BuffCheck(car2,buff):
            if buff.index==1:
                print('Xe 2 co buff tang toc')
                buff_increase(2,car2_increase,car2,buff)
                off_buff(buff,car2_increase,car2)

            if buff.index==2:
                print('Xe 2 co buff toc bien')
                BuffApply(car2,buff,player)
            if buff.index==4:
                print('Xe 2 co buff nhan doi so tien cuoc')
                BuffApply(car2,buff,player)
            if buff.index==3:
                print('Xe 2 co buff dich chuyen lui')
                BuffApply(car2,buff,player)
            if buff.index==5:
                print('Xe 2 co buff cong them tien')
                BuffApply(car2,buff,player)
        if BuffCheck(car3,buff):
            if buff.index==1:
                print('Xe 3 co buff tang toc')
                buff_increase(3,car3_increase,car3,buff)
                off_buff(buff,car3_increase,car3)

            if buff.index==2:
                print('Xe 3 co buff toc bien')
                BuffApply(car3,buff,player)
            if buff.index==4:
                print('Xe 3 co buff nhan doi so tien cuoc')
                BuffApply(car3,buff,player)
            if buff.index==3:
                print('Xe 3 co buff dich chuyen lui')
                BuffApply(car3,buff,player)
            if buff.index==5:
                print('Xe 3 co buff cong them tien')
                BuffApply(car3,buff,player)
        if BuffCheck(car4,buff):
            if buff.index==1:
                print('Xe 4 co buff tang toc')
                buff_increase(4,car4_increase,car4,buff)
                off_buff(buff,car4_increase,car4)

            if buff.index==2:
                print('Xe 4 co buff toc bien')
                BuffApply(car4,buff,player)
            if buff.index==4:
                print('Xe 4 co buff nhan doi so tien cuoc')
                BuffApply(car4,buff,player)
            if buff.index==3:
                print('Xe 4 co buff dich chuyen lui')
                BuffApply(car4,buff,player)
            if buff.index==5:
                print('Xe 4 co buff cong them tien')
                BuffApply(car4,buff,player)
        if BuffCheck(car5,buff):
            if buff.index==1:
                print('Xe 5 co buff tang toc')
                buff_increase(5,car5_increase,car5,buff)
                off_buff(buff,car5_increase,car5)

            if buff.index==2:
                print('Xe 5 co buff toc bien')
                BuffApply(car5,buff,player)
            if buff.index==4:
                print('Xe 5 co buff nhan doi so tien cuoc')
                BuffApply(car5,buff,player)
            if buff.index==3:
                print('Xe 5 co buff dich chuyen lui')
                BuffApply(car5,buff,player)
            if buff.index==5:
                print('Xe 5 co buff cong them tien')
                BuffApply(car5,buff,player)
        #Buff và skill apply
        #Tạo nút buff
        buff_use_x=784
        buff_use_x2=829
        buff_use_y=458
        buff_use_y2=507
        #Tạo nút skill
        skill_use_x=770
        skill_use_y=487
        skill_use_x2=831
        skill_use_y2=507
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            x,y=pygame.mouse.get_pos()
            if (x>buff_use_x and y>buff_use_y and x<buff_use_x2 and y<buff_use_y2):
                if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1):
                    if player.buff_use <1:
                        click.play()
                        print('Buff is used')
                        if car1.name==player.choose:
                            car=car1
                            car_increase=car1_increase
                        if car2.name==player.choose:
                            car=car2
                            car_increase=car2_increase
                        if car3.name==player.choose:
                            car=car3
                            car_increase=car3_increase
                        if car4.name==player.choose:
                            car=car4
                            car_increase=car4_increase
                        if car5.name==player.choose:
                            car=car5
                            car_increase=car5_increase
                        buff_use(car,player,car_increase,buff)
                        player.buff_use+=1
                        buff_displayv2(player.buff_use_index)


            #print(x,y)
        
        pygame.display.update()
        fpsClock.tick(FPS)
def Play():
        playing_music = pygame.mixer.Channel(1)
        win_music=pygame.mixer.Sound('win.wav')
        lose_music=pygame.mixer.Sound('lose.wav')
        playing_music.play(pygame.mixer.Sound('Racing.mp3'))
        main_music
        #Cần có init để khôi phục game khi chơi tiếp
        car1.__init__()
        car2.__init__()
        car3.__init__()
        car4.__init__()
        car5.__init__()
        win_lose.__init__()
        buff.__init__()
        fn.__init__()
        running =1
        while running:
            t=4
            lanecar1(car1,car2,car3,car4,car5)
            while t>0:
                BuffControl(buff)
                Gameplay()
                t-=1
            Endgame()
            playing_music.stop()
            if checkwin(Rank_name,player)==1:
                
                win_music.play()
            else:
                
                lose_music.play()

            Result(Rank_name,player)
            running =menu.ranking(Rank_name)
            menu.result_player(checkwin(Rank_name,player),player)
            pygame.display.update()
            
            fpsClock.tick(FPS)
