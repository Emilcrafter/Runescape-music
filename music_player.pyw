import pygame
import glob
from random import randrange

pygame.init()
clock = pygame.time.Clock()
# fonts
font1 = pygame.font.Font('./fonts/RuneScape-Plain-11.ttf', 15)
font2 = pygame.font.Font('./fonts/RuneScape-Plain-12.ttf', 15)
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 152, 31)
# opening all the image files here as well as deciding the window size
size = [236, 262]
SONGEND = pygame.constants.USEREVENT
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
icon = pygame.image.load('./pics/Icon.png')
manon = pygame.image.load('./pics/Man2.png')
manoff = pygame.image.load('./pics/Man1.png')
autoon = pygame.image.load('./pics/Auto2.png')
autooff = pygame.image.load('./pics/Auto1.png')
loopon = pygame.image.load('./pics/Loop2.png')
loopoff = pygame.image.load('./pics/Loop1.png')
background = pygame.image.load('./pics/Background.png')
pillar = pygame.image.load('./pics/Pillar.png')
frame = pygame.image.load('./pics/Frame.png')
cover = pygame.image.load('./pics/Cover.png')
cover2 = pygame.image.load('./pics/Cover2.png')
scrollbar = pygame.image.load('./pics/Scrollbar.png')
scroller = pygame.image.load('./pics/Scroller.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Runescape Music')
# Here's the music list
songs = glob.glob('./songs/*.ogg')


class mous:
    clicked = False
    scroll = -15
    scrolling = False
    useraction = 5

# the three mode buttons


class bigones:
    auto = True
    man = False
    loop = False
    recent = 1
    song = "AUTO"
    stored = None
    f = None
# loop for rendering


done = False
while not done:
    clock.tick(60)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (click[0] == 0):
        mous.clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5 and (mous.scroll < (len(songs)* 15) - 210 ):
                mous.scroll += 45
            elif event.button == 4 and (mous.scroll >= 15):
                mous.scroll -= 45
            elif mous.scroll > (len(songs)*15 - 210):
                mous.scroll = (len(songs) * 15 - 210)
            
        if event.type == SONGEND:
            autoplay()
    screen.blit(background, (0, 0))
    screen.blit(pillar, (0, 0))
    screen.blit(pillar, (210, 0))
    screen.blit(frame, (25, 53))
    screen.blit(scrollbar, (189, 59))
    def textbox(text, x, y, font, sl = False, Color = GREEN):
        textst = font.render(str(text), False, (Color))
        textsh = font.render(str(text), False, (BLACK))
        textsl = font.render(str(text), False, (WHITE))
        screen.blit(textsh, (x + 1, y + 1))
        if sl:
            screen.blit(textsl, (x, y))
        else:
            screen.blit(textst, (x, y))
    def songstatus(text):
           textbox(text, 32, 34, font2, False)
        # 87,8 auto, 129,8 manual 171,8 loop

    def bigbuttons(img1, img2, x, y, n):

        if ((n == 1 and bigones.auto) or (n == 2 and bigones.man) or (n == 3 and bigones.loop)):
            screen.blit(img2, (x, y))
        else:
            screen.blit(img1, (x, y))
        if ((x+36) > mouse[0] > x and (y+25) > mouse[1] > y) and (click[0] == 1) and (not mous.clicked):
            mous.clicked = True
            
            if (n == 1) and (not bigones.auto):
                bigones.auto = (not bigones.auto)
                if bigones.auto:
                    if (bigones.recent == 2):
                        bigones.man = 0
                    bigones.recent = 1
                    bigones.song = "AUTO"
            elif (n == 2) and (not bigones.man):
                bigones.man = (not bigones.man)
                if bigones.man:
                    if (bigones.recent == 1):
                        bigones.auto = 0
                    bigones.recent = 2
                    bigones.song = "MANUAL"
            elif n == 3:
                bigones.loop = (not bigones.loop)
            print(bigones.recent)

    def smallbuttons():
        for i in range (0, len(songs) - 1):
            # print(songs[i])
            mous.useraction = 0
            a = mous.scroll
            b = (153 > mouse[0] > 37)
            c = (62 + (15 * i) - a)
            d = (62 + (15 * (i - 1)) - a)
            e = (c > mouse[1] > d)
            bigones.f = len(songs[i])
            # 37, 61
            if (b and e) and (39 < d < 240):
                textbox(str(songs[i][8:bigones.f-4]), 37, d, font2, True)
                if click[0] and not mous.clicked:
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    tune = pygame.mixer.Sound(songs[i])
                    chan = pygame.mixer.Channel(1)
                    mous.useraction = True
                    
                    
                    if pygame.mixer.get_busy():
                        tune.get_length()
                        chan.fadeout(2000)
                        chan.play(tune, 0, 0, 2000)
                        bigones.stored = songs[i]
                        bigones.song = songs[i][8:bigones.f-4]
                        chan.set_endevent(pygame.constants.USEREVENT)
                    else:
                        chan.play(tune, 0, 0, 2000)
                        bigones.stored = songs[i]
                        bigones.song = songs[i][8:bigones.f-4]
                        chan.set_endevent(pygame.constants.USEREVENT)
                    chan.set_volume(1.0)
                    bigones.man = True
                    bigones.auto = False
                    bigones.recent = 2
            elif (39 < d < 240):
                textbox(str(songs[i][8:bigones.f-4]), 37, d, font2, False)
            # 191, 74 146
    textbox('Playing:', 32, 17, font2, False, GOLD)
    #textst = font2.render(str('Playing:'), False, (GOLD))
    #textsh = font2.render(str('Playing:'), False, (BLACK))
    #screen.blit(textsh, (33, 18))
    #screen.blit(textst, (32, 17))
    def scrollbox():
        a = 71 + (mous.scroll/15 + 15) * 146 / (len(songs))
        screen.blit(scroller, (190, a))
        # 14, 152
        if click[0] and (71 + 154 > mouse[1] > 71) and (191 < mouse[0] < 205):
            mous.scrolling = True
            mous.clicked = True
            
        if mous.scroll > (len(songs) * 15 - 10):
                mous.scroll = (len(songs) * 15 - 10)
                
        if (mous.clicked) and (mous.scrolling):
            
            if mouse[1] <= 71:
                    mous.scroll = -15
            elif mouse[1] >= 212:
                    mous.scroll = (len(songs) * 15 - 212)
            elif 227 >= a+9 >= 61:
                    mous.scroll = ((mouse[1] - 71)* 15 * (len(songs)-1) / 146)
            elif (a + 10) > 227:
                mous.scroll = (len(songs) * 15 - 212)
            else:
                mous.scrolling = False
        if (click[0] and (74 > mouse[1] > 60) and (191 < mouse[0] < 205) and (mous.scroll > -15)):
            mous.scroll -= 8
            
        if (click[0] and (242 > mouse[1] > 228) and (191 < mouse[0] < 205) and (mous.scroll < len(songs) * 15 - 212)):
            mous.scroll += 8
            
    if mous.useraction < 6:
        mous.useraction += 1
    def autoplay():
        pygame.mixer.quit()
        pygame.mixer.init()
        print("a")
        if bigones.loop:
            tune = pygame.mixer.Sound(bigones.stored)
            pygame.mixer.Channel(1).set_endevent()
            pygame.mixer.Channel(1).play(tune, 0, 0, 2000)
            pygame.mixer.Channel(1).set_endevent(pygame.constants.USEREVENT)
            
        elif  (mous.useraction < 5)and (bigones.auto):
            i = randrange(0, len(songs)-1)
            bigones.f = len(songs[i])
            tune = pygame.mixer.Sound(songs[i])
            bigones.song = songs[i][8:bigones.f-4]
            pygame.mixer.Channel(1).set_endevent()
            pygame.mixer.Channel(1).play(tune, 0, 0, 2000)
            pygame.mixer.Channel(1).set_endevent(pygame.constants.USEREVENT)
            mous.useraction = 0
            pygame.mixer.Channel(1).set_volume(1.0)
            
    scrollbox()
    # print(mous.scroll / len(songs))
    smallbuttons()
    screen.blit(cover, (26, 33))
    screen.blit(cover2, (31, 242))
    #96, 251
    songstatus(bigones.song)
    textbox((str(len(songs))) + " / " + (str(len(songs))), 96, 251, font1, False, GOLD)
    bigbuttons(autooff, autoon, 87, 8, 1)
    bigbuttons(manoff, manon, 129, 8, 2)
    bigbuttons(loopoff, loopon, 171, 8, 3)

    pygame.display.flip()
    
pygame.quit()
