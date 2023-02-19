import pygame, sys, time
import math
import random
from pygame import mixer

# setup display
pygame.init()
WIDTH, HEIGHT = 850, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
OPTION_FONT = pygame.font.SysFont('times new roman', 20)
LETTER_FONT = pygame.font.SysFont('comicsans', 40) # letter in circle
WORD_FONT = pygame.font.SysFont('comicsans', 50)   # letter guess
TITLE_FONT = pygame.font.SysFont('comicsans', 50)   
POINT_FONT = pygame.font.SysFont('times new roman', 30)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)


# game variables
hangman_status = 0
words = ["FERRARI", "BUGATTI", "MERCEDES", "CHEVROLET", "MAZDA", "BMW", "FORD", "AUDI", "TOYOTA", "HONDA", "NISSAN", "LEXUS", "VINFAST"]
word = random.choice(words)
guessed = []

# colors
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)
RED      = (255,   0,   0)
BLUE     = (  0,   0, 255)
GREEN    = (  0, 128,   0)
AQUA     = (  0, 255, 255)
LIME     = (  0, 255,   0)
FUCHISIA = (255,   0, 255)
#GRAY     = (128, 128, 128)# old
GRAY     = (70, 70, 70)    # new
SILVER   = (192, 192, 192)# old
#SILVER   = (220, 220, 220) # new
PURPLE   = (128,   0, 128)
YELLOW   = (255, 255,   0)
NAVYBLUE = (  0,   0, 128)
OLIVE    = (128, 128,   0)


def draw_point(point):
    # draw points table
    pygame.draw.rect(SCREEN, BLACK, (25, 25, 180, 40))
    pygame.draw.rect(SCREEN, SILVER, (27,27,176,36))
    text = POINT_FONT.render("Điểm : " + str(point), 1, BLACK) # str(integer_number) chuyển đổi số nguyên thành kiểu string
    SCREEN.blit(text, (29, 29))

def draw(point):
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, SILVER, (20, 20, WIDTH - 40, HEIGHT - 40))

    # draw_title():
    text = TITLE_FONT.render("HANGMAN or MONEY", 1, BLACK)
    SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 40)) #text.get_width() là lấy chiều dài đoạn text

    text = OPTION_FONT.render("Nhóm 7 - HCMUS", 1, BLACK)
    SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, 80))
    
    image_back = pygame.image.load("back.png") # ảnh có độ rộng 50x50
    SCREEN.blit(image_back, (760, 30))

    image_help = pygame.image.load("question.png") # ảnh có độ rộng 50x50
    SCREEN.blit(image_help, (700, 30))

    draw_point(point)
    
    # draw_word():
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    SCREEN.blit(text, (350, 260)) #(400, 200)

    # draw_buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(SCREEN, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            SCREEN.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    
    SCREEN.blit(images[hangman_status], (130, 140)) #(150, 100)
    pygame.display.update()

def draw_getPoint():
    getPoint = POINT_FONT.render("+ 10", 1, BLACK)
    SCREEN.blit(getPoint, (110, 69))
    pygame.display.update()
    pygame.time.delay(1000)

def display_message(message):
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, SILVER, (20, 20, WIDTH - 40, HEIGHT - 40))
    text = POINT_FONT.render(message, 1, BLACK)
    SCREEN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()

def menu_HELP():
    pygame.draw.rect(SCREEN, BLACK, (420, 80, 410, 140))
    pygame.draw.rect(SCREEN, SILVER, (425, 85, 400, 130))
    help_0 = OPTION_FONT.render("Hướng dẫn", 1, BLACK)
    help_1 = OPTION_FONT.render("-Dùng chuột click chọn ký tự bên dưới", 1, BLACK)
    help_2 = OPTION_FONT.render("-Nếu đoán đúng thì bạn sẽ nhận được 10 điểm", 1, BLACK)
    help_3 = OPTION_FONT.render("-Điểm sẽ được đổi thành xu sau khi thoát game", 1, BLACK)
    help_4 = OPTION_FONT.render("*Gợi ý", 1, BLACK)
    help_5 = OPTION_FONT.render("--Từ cần đoán là tên của một hãng xe hơi", 1, BLACK)
    SCREEN.blit(help_0, (560, 90))
    SCREEN.blit(help_1, (440, 110))
    SCREEN.blit(help_2, (440, 130))
    SCREEN.blit(help_3, (440, 150))
    SCREEN.blit(help_4, (440, 170))
    SCREEN.blit(help_5, (440, 190))
    pygame.display.update()
    

def mini_game_main():
    global hangman_status
    global point
    global guessed
    global won
    global letters
    global words
    global word
    point = 0 # xu ban đầu
    maxPoint = 10000
    FPS = 120
    clock = pygame.time.Clock()
    Done = False

    while not Done:
        clock.tick(FPS)      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
                # draw menu help
                if m_x <= 750 and m_x >= 700 and m_y <= 80 and m_y >= 30:
                    menu_HELP()
                    pygame.time.delay(4000)
                # back to racing game
                if m_x <= 810 and m_x >= 760 and m_y <= 80 and m_y >= 30:
                    Done = True
                    break
                    return point

        draw(point)

        if point > (maxPoint - 10):
            pygame.time.delay(1000)
            display_message("Xin chúc mừng!!! Bạn đã đạt được số tiền lớn nhất")
            pygame.time.delay(3000)
            display_message("Hẹn gặp lại lần sau")
            pygame.time.delay(3000)
            display_message("Trò chơi sẽ kết thúc sau 3")
            pygame.time.delay(1000)
            display_message("Trò chơi sẽ kết thúc sau 2")
            pygame.time.delay(1000)
            display_message("Trò chơi sẽ kết thúc sau 1")
            pygame.time.delay(1000)
            Done = True
            return point
                    
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        # won
        if won:
            point = point + 10
            draw_getPoint()
            mixer.music.load('cash_sound.wav')
            draw_point(point)
            mixer.music.play(1)
            mixer.music.play(1)
            pygame.display.update()
            guessed = []
            hangman_status = 0
            for letter in letters:
                letter[3] = True
            word = random.choice(words)
            won = False
            
        # lose
        if hangman_status == 6:
            guessed = []
            hangman_status = 0
            for letter in letters:
                letter[3] = True
            word = random.choice(words)
            mixer.music.load('lose_sound.wav')
            mixer.music.play(1)
            pygame.time.delay(1000)
            display_message("Bạn đoán sai rồi!!!")
            pygame.time.delay(2000)
        
Done = False
while not Done:
    point = mini_game_main()
    Done = True
pygame.quit()









