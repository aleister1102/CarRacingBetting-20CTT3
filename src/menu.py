import pygame, sys
from pygame.locals import *
import time
import Racing_Game
import data
import minigame
WINDOWWIDTH = 850 # Chiều rộng cửa sổ
WINDOWHEIGHT = 600 # Chiều cao cửa sổ
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLACK = (  0,   0,   0)
AVA1=pygame.image.load('car_trong.png')
AVA2=pygame.image.load('car_phat.png')
AVA3=pygame.image.load('car_son.png')
AVA4=pygame.image.load('car_tuan.png')
AVA5=pygame.image.load('car_quan.png')
DISTANCE=94

pygame.init()
DISPLAYSURF = pygame.display.set_mode(size=(WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Betting Racing Game - Team S3V3N')

click=pygame.mixer.Sound('click.wav')
main_music=pygame.mixer.Sound('main.mp3')    


#Mainmenu
def Main_Menu ():
    Main_Menu = True
    main_menu = pygame.image.load('menu_main.png')
    main_music.play()
    main_music.set_volume(0.8)
    while Main_Menu:
        pygame.display.get_window_size()
        DISPLAYSURF.blit(main_menu,(0,0))
        
        font_name='Font2.TTF'
        font=pygame.font.Font(font_name,14)
        #Ghi tên người chơi
        name=font.render(str(Racing_Game.player.name),True,(BLACK))
        name_x=765
        name_y=8
        DISPLAYSURF.blit(name,(name_x,name_y))
        #Ghi buff hiện có
        buff=font.render(str(Racing_Game.player.buff),True,(BLACK))
        buff_x=765
        buff_y=103
        DISPLAYSURF.blit(buff,(buff_x,buff_y))
        #Ghi tiền hiện có
        money=font.render(str(Racing_Game.player.money),True,(BLACK))
        money_x=765
        money_y=60
        DISPLAYSURF.blit(money,(money_x,money_y))
        
        x,y = pygame.mouse.get_pos()
        #print(x,y)
        event = pygame.event.wait()
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Tạo nút playgame
        play_x=350
        play_x2=500
        play_y=280
        play_y2=320
        if (x>play_x and y > play_y and x < play_x2 and y < play_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                if Racing_Game.player.name!='':
                    # Toan roi rac da cuu tui cho nay :<
                    print('Tien hien co la: ',Racing_Game.player.money)
                    print('Tien dat cuoc la: ',Racing_Game.player.bet)
                    Racing_Game.player.choose=''
                    Racing_Game.player.bet=0
                    while (Racing_Game.player.choose=='' and Racing_Game.player.bet==0):
                            betting()

        #Tạo nút setting
        setting_x=play_x
        setting_x2=play_x2
        setting_y=364
        setting_y2=400
        if (x>setting_x and y > setting_y and x < setting_x2 and y < setting_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                setting_menu()
        #Tạo nút quit
        quit_x=play_x
        quit_x2=play_x2
        quit_y=514
        quit_y2=552
        if (x>quit_x and y > quit_y and x < quit_x2 and y < quit_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                pygame.quit()
                sys.exit()
        #Tạo nút mini game
        minigame_x=0
        minigame_y=0
        minigame_x2=50
        minigame_y2=50
        if (x>minigame_x and y > minigame_y and x < minigame_x2 and y < minigame_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
               click.play()
               if Racing_Game.player.money<500 and Racing_Game.player.name!='':
                    minigame.mini_game_main()
               else: print('Tien lon hon 500 hoac chua dang nhap')

        #Tạo nút store
        store_x=0
        store_y=60
        store_x2=50
        store_y2=store_y+50
        if (x>store_x and y > store_y and x < store_x2 and y < store_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                store()
        #Tạo nút login
        login_x=744
        login_y=133
        login_x2=850
        login_y2=170
        if (x>login_x and y > login_y and x < login_x2 and y < login_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('login')
                print('Tien hien co la: ',Racing_Game.player.money)
                print('Chua co tai khoan duoc load')
                data.run_login()
        #Tạo nút help
        help_x=0
        help_y=120
        help_x2=50
        help_y2=help_y+50
        if (x>help_x and y > help_y and x < help_x2 and y < help_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('help')
                help()
        #Tạo nút about
        about_x=play_x
        about_x2=play_x2
        about_y=440
        about_y2=480
        if (x>about_x and y > about_y and x < about_x2 and y < about_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
               click.play()
               about()

        pygame.display.update()

#SettingMenu
def setting_menu():
    running =1
    setting_width=WINDOWWIDTH
    setting_height=WINDOWHEIGHT
    setting_x=0
    setting_y=0
    while running:
        setting_display=pygame.image.load('menu_setting.png')
        setting_display=pygame.transform.scale(setting_display,(setting_width,setting_height))
        DISPLAYSURF.blit(setting_display,(setting_x,setting_y))
        x,y = pygame.mouse.get_pos()
        #print(x,y)
        event = pygame.event.wait()
        #Dấu chấm hỏi
        if (x>230 and y>170 and x<270 and y<230):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                help()
        #Dấu thoát
        if (x>570 and y>170 and x<630 and y<230):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                running=0
        #Dấu tắt âm
        if (x>300 and y>250 and x<350 and y<300):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mute()
                

        #Dấu low
        if (x>390 and y>260 and x<435 and y<290):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                volume(1)
        #Dấu avg
        if (x>450 and y>260 and x<500 and y<290):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                volume(2)
        #Dấu high
        if (x>510 and y>260 and x<560 and y<290):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                volume(3)
        #Button Màn hình
        if (x>300 and y>335 and x<350 and y<400):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                #DISPLAYSURF=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #Small
        if (x>370 and y>355 and x<430 and y<385):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                screen(1)
        #Mid
        if (x>445 and y>355 and x<495 and y<385):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                screen(2)
        #Big
        if (x>500 and y>355 and x<550 and y<385):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                screen(3)

        if event.type == QUIT:
            click.play()
            running =0
            DISPLAYSURF.fill(WHITE)
            return
        pygame.display.update()
def help():
    print ('HELP')
def mute():
    main_music.stop()
    #1 Biểu thị cho đã tắt âm của game
    return 1
def unmute():
    main_music.play()
def volume(index):
    if index==1:
        main_music.stop()
        main_music.play()
        main_music.set_volume(0.1)
    if index==2:
        main_music.stop()
        main_music.play()
        main_music.set_volume(0.5)
    if index==3:
        main_music.stop()
        main_music.play()
        main_music.set_volume(1.5)
def full_screen():
    pass
def screen(index):
    if index==1:
        WINDOWWIDTH=480
        WINDOWHEIGHT=680
        DISPLAYSURF = pygame.display.set_mode(size=(WINDOWWIDTH, WINDOWHEIGHT))
    if index==2:
        WINDOWWIDTH=600
        WINDOWHEIGHT=850
        DISPLAYSURF = pygame.display.set_mode(size=(WINDOWWIDTH, WINDOWHEIGHT))
    if index==3:
        WINDOWWIDTH=770
        WINDOWHEIGHT=1020
        DISPLAYSURF = pygame.display.set_mode(size=(WINDOWWIDTH, WINDOWHEIGHT))

#Betting
#Nut 100
x_100=int(225)
y_100=int(400)
x2=int(387)
y2=int(434)
#Nut 50
x_50=int(405)
x2_50=int(478)
#Nut 10
x_10=int(578)
x2_10=int(654)
def betting():
    running =1
    betting_width=WINDOWWIDTH
    betting_height=WINDOWHEIGHT
    betting_x=0
    betting_y=0
    while running:
        betting_display=pygame.image.load('menu_betting.png')
        betting_display=pygame.transform.scale(betting_display,(betting_width,betting_height))
        DISPLAYSURF.blit(betting_display,(betting_x,betting_y))
        x,y = pygame.mouse.get_pos()
        #print(x,y)
        event = pygame.event.wait()
        w=WINDOWWIDTH
        h=WINDOWHEIGHT
        if event.type == QUIT:
                print('Thoat')
                Racing_Game.player.choose='.'
                Racing_Game.player.bet=1
                running=0
                return 0
        #Cac nut dat cuoc
        if(x>x_100 and y>y_100 and x<x2 and y<y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
                click.play()
                print('100')
                Racing_Game.player.bet+=100
                
        if (x>x_50 and y>y_100 and x<x2_50 and y<y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
                click.play()
                print('50')
                Racing_Game.player.bet+=50
        if (x>x_10 and y>y_100 and x<x2_10 and y<y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
                click.play()
                print('10')
                Racing_Game.player.bet+=10
        
        #Xe1
        car1_x=int (11*w/50)
        car1_x2=int (49*w/170)
        car1_y=int(61*h/120)
        car1_y2=int(83*h/150)
        if (x>car1_x and y>car1_x2 and x<car1_x2 and y<car1_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('car1')
                Racing_Game.player.choose='car1'
        #Xe2
        car2_x=int (287*w/850)
        car2_x2=int (174*w/425)
        car2_y=int(61*h/120)
        car2_y2=int(83*h/150)
        if (x>car2_x and y>car2_y and x<car2_x2 and y<car2_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('car2')
                Racing_Game.player.choose='car2'
        #Xe3
        car3_x=int (196*w/425)
        car3_x2=int (9*w/17)
        car3_y=int(61*h/120)
        car3_y2=int(83*h/150)
        if (x>car3_x and y>car3_y and x<car3_x2 and y<car3_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('car3')
                Racing_Game.player.choose='car3'
        #Xe4
        car4_x=int (249*w/425)
        car4_x2=int (279*w/425)
        car4_y=int(61*h/120)
        car4_y2=int(83*h/150)
        if (x>car4_x and y>car4_y and x<car4_x2 and y<car4_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('car4')
                Racing_Game.player.choose='car4'
        #Xe5
        car5_x=int (12*w/17)
        car5_x2=int (331*w/425)
        car5_y=int(61*h/120)
        car5_y2=int(83*h/150)
        if (x>car5_x and y>car5_y and x<car5_x2 and y<car5_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('car5')
                Racing_Game.player.choose='car5'
        #Nut help
        help_x=int(120)
        help_y=int(110)
        help_x2=int(173)
        help_y2=int(160)
        if (x>help_x and y>help_y and x<help_x2 and y<help_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                help()
        #Nut thoat
        exit_x=int(661)
        exit_x2=int(712)
        if (x>exit_x and y>help_y and x<exit_x2 and y<help_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('Thoat')
                Racing_Game.player.choose='.'
                Racing_Game.player.bet=1
                running=0
                return 0
                    
        #Nut choi game
        play_x=267
        play_x2=596
        play_y=458
        play_y2=503
        if(x>play_x and y>play_y and x<play_x2 and y<play_y2):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button==1):
                        if (Racing_Game.player.bet!=0 and Racing_Game.player.choose!=''):
                            
                            click.play()
                            print('Tien hien co la: ',Racing_Game.player.money)
                            print('Tien dat cuoc la: ',Racing_Game.player.bet)
                            if Racing_Game.player.money==0:
                                minigame.mini_game_main()
                            if Racing_Game.player.money<Racing_Game.player.bet:
                                #Cần hiển thị một cách tường minh
                                print('Không đủ tiền, mời nhập lại hoặc chơi mini game')
                                return                     
                            main_music.stop()
                            Racing_Game.Play()
                            

                    
        pygame.display.update()

def ranking(Rank_name):
    running =1
    betting_width=WINDOWWIDTH
    betting_height=WINDOWHEIGHT
    betting_x=0
    betting_y=0
    DISPLAYSURF.fill(WHITE)
    while running:
        betting_display=pygame.image.load('ranking.png')
        betting_display=pygame.transform.scale(betting_display,(betting_width,betting_height))
        DISPLAYSURF.blit(Racing_Game.bg.img,(0,0))
        DISPLAYSURF.blit(betting_display,(betting_x,betting_y))
        x,y = pygame.mouse.get_pos()
        #print(x,y)
        x0=345
        y0=125

        for i in range(5):
            if Rank_name[i]=='car1':
                y1=y0+(i*DISTANCE)
                DISPLAYSURF.blit(AVA1,(x0,y1))
            if Rank_name[i]=='car2':
                y2=y0+(i*DISTANCE)
                DISPLAYSURF.blit(AVA2,(x0,y2))
            if Rank_name[i]=='car3':
                y3=y0+(i*DISTANCE)
                DISPLAYSURF.blit(AVA3,(x0,y3))
            if Rank_name[i]=='car4':
                y4=y0+(i*DISTANCE)
                DISPLAYSURF.blit(AVA4,(x0,y4))
            if Rank_name[i]=='car5':
                y5=y0+(i*DISTANCE)
                DISPLAYSURF.blit(AVA5,(x0,y5))
        pygame.display.update() 
        event = pygame.event.wait()
        if event.type == QUIT:
            running =0
        #help
        if (x>230 and y>170 and x<270 and y<230):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                help()
        
        #Tao nut cua hang
        store_x=114
        store_x2=180
        store_y=510
        store_y2=564
        if (x>106 and y > 510 and x < 180 and y < 564):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                store()
        #Tao nut quay ve
        back_x=666
        back_x2=726
        if (x>back_x and y > 510 and x < back_x2 and y < 564):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                Racing_Game.player.bet=0
                Racing_Game.player.choose='.'
                running=0
                return 0
PRICE=100
def store():
    running =1
    store_width=WINDOWWIDTH
    store_height=WINDOWHEIGHT
    store_x=0
    store_y=0
    while running:
        store_display=pygame.image.load('menu_store.png')
        store_display=pygame.transform.scale(store_display,(store_width,store_height))
        DISPLAYSURF.blit(store_display,(store_x,store_y))
        
        font_name='8-BIT WONDER.TTF'
        font=pygame.font.Font(font_name,13)
        
        #Ghi buff hiện có
        buff=font.render(str(Racing_Game.player.buff),True,(WHITE))
        buff_x=500
        buff_y=216
        DISPLAYSURF.blit(buff,(buff_x,buff_y))
        #Ghi tiền hiện có
        money=font.render(str(Racing_Game.player.money),True,(WHITE))
        money_x=340
        money_y=216
        DISPLAYSURF.blit(money,(money_x,money_y))
        
        x,y = pygame.mouse.get_pos()
        event = pygame.event.wait()
        if event.type == QUIT:
            running =0
        buff_temp=0
        if (x>377 and y>446 and x<503 and y<476):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('bought')
                if Racing_Game.player.money>=150:
                    buff_temp+=1
                    if  buff_temp!=0 and Racing_Game.player!=0:
                        Racing_Game.player.money-=buff_temp*PRICE
                        Racing_Game.player.buff+=buff_temp
                        with open(Racing_Game.player.path,'r+',encoding='utf-8') as f:
                            data=f.readlines()
                            data[3]=str(Racing_Game.player.buff)+'\n'
                        with open(Racing_Game.player.path,'r+',encoding='utf-8') as f:
                            for line in data:
                                if line.strip('\n') !='\n':
                                    f.write(line)
        help_x=243
        help_y=119
        help_x2=274
        help_y2=156
        #help
        if (x>help_x and y>help_y and x<help_x2 and y<help_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                help()
        
        #Nút thoát
        exit_x=int(575)
        exit_x2=int(615)
        exit_y=int(116)
        exit_y2=int(154)
        if (x>exit_x and y>exit_y and x<exit_x2 and y<exit_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('Thoat')
                running=0
                return 0
        #print(x,y)    
        pygame.display.update()

def result_player(cond,player):
    running =1
    betting_width=WINDOWWIDTH
    betting_height=WINDOWHEIGHT
    betting_x=0
    betting_y=0
    while running:
        if cond==1:
            betting_display=pygame.image.load('result_win.png')
            betting_display=pygame.transform.scale(betting_display,(betting_width,betting_height))
            DISPLAYSURF.blit(betting_display,(betting_x,betting_y))
        if cond==2:
            betting_display=pygame.image.load('result_lose.png')
            betting_display=pygame.transform.scale(betting_display,(betting_width,betting_height))
            DISPLAYSURF.blit(betting_display,(betting_x,betting_y))

        x,y = pygame.mouse.get_pos()
        print(x,y)
        event=pygame.event.wait()
        # Nút quit
        if (x> 670 and y>130 and x<706 and y<166):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                return
        #Play again
        if (x> 189 and y>463 and x<380 and y<495):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                betting()         
        #Play mini game
        if (x> 475 and y>462 and x<666 and y<496):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                if Racing_Game.player.money<500:
                    minigame.mini_game_main()
                else: 
                   print('Tien lon hon 500')
                   return
        #Dấu chấm hỏi
        if (x>132 and y>170 and x<132 and y<170):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                help()
            
        #Hiển thị 
        money_result_x=424
        money_result_y=300
        font_name='8-BIT WONDER.TTF'
        font=pygame.font.Font(font_name,20)
        money_word=font.render(str(Racing_Game.player.money),True,WHITE)
        DISPLAYSURF.blit(money_word,(money_result_x,money_result_y))
        #Car
        car_result_x=408
        car_result_y=360
        Racing_Game.player.ava_img=pygame.transform.scale(Racing_Game.player.ava_img,(140,80))
        DISPLAYSURF.blit(Racing_Game.player.ava_img,(car_result_x,car_result_y))        
        pygame.display.update()

def about():
    running =1
    about_width=WINDOWWIDTH
    about_height=WINDOWHEIGHT
    about_x=0
    about_y=0
    while running:
        about_display=pygame.image.load('about.png')
        about_display=pygame.transform.scale(about_display,(about_width,about_height))
        DISPLAYSURF.blit(about_display,(about_x,about_y))
        x,y = pygame.mouse.get_pos()
        #print(x,y)
        event = pygame.event.wait()
        w=WINDOWWIDTH
        h=WINDOWHEIGHT
        if event.type == QUIT:
                print('Thoat')
                Racing_Game.player.choose='.'
                Racing_Game.player.bet=1
                running=0
                return 0
        #Nut quay lai
        exit_x=int(724)
        exit_x2=int(771)
        exit_y=int(531)
        exit_y2=int(541)
        if (x>exit_x and y>exit_y and x<exit_x2 and y<exit_y2):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                click.play()
                print('Thoat')
                running=0
                return 0
        print(x,y)    

        pygame.display.update()    
if __name__=='__main__':
        
        pygame.init()
        #if Racing_Game.player.name=='exit':
        #    pygame.quit()
        #    sys.exit()
        Main_Menu()
