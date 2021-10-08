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
SONG_END = pygame.constants.USEREVENT
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
icon = pygame.image.load('./pics/Icon.png')
manon = pygame.image.load('./pics/Man2.png')
manual_off = pygame.image.load('./pics/Man1.png')
auto_on = pygame.image.load('./pics/Auto2.png')
auto_off = pygame.image.load('./pics/Auto1.png')
loop_on = pygame.image.load('./pics/Loop2.png')
loop_off = pygame.image.load('./pics/Loop1.png')
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
change_occurred = 1



class Mouse:
    clicked = False
    scroll = -15
    scrolling = False
    user_action = 5


# the three mode buttons


class big_ones:
    auto = True
    man = False
    loop = False
    recent = 1
    song = "AUTO"
    stored = None
    f = None


# loop for rendering

def textbox(text, x, y, font, sl=False, color=GREEN):
    text_standard = font.render(str(text), False, color)
    text_shadow = font.render(str(text), False, BLACK)
    text_selected = font.render(str(text), False, WHITE)
    screen.blit(text_shadow, (x + 1, y + 1))
    if sl:
        screen.blit(text_selected, (x, y))
    else:
        screen.blit(text_standard, (x, y))


def song_status(text):
    textbox(text, 32, 34, font2, False)


def autoplay():
    pygame.mixer.quit()
    pygame.mixer.init()
    print("a")
    if big_ones.loop:
        tune = pygame.mixer.Sound(big_ones.stored)
        pygame.mixer.Channel(1).set_endevent()
        pygame.mixer.Channel(1).play(tune, 0, 0, 2000)
        pygame.mixer.Channel(1).set_endevent(pygame.constants.USEREVENT)

    elif (Mouse.user_action < 5) and big_ones.auto:
        i = randrange(0, len(songs) - 1)
        big_ones.f = len(songs[i])
        tune = pygame.mixer.Sound(songs[i])
        big_ones.song = songs[i][8:big_ones.f - 4]
        pygame.mixer.Channel(1).set_endevent()
        pygame.mixer.Channel(1).play(tune, 0, 0, 2000)
        pygame.mixer.Channel(1).set_endevent(pygame.constants.USEREVENT)
        Mouse.user_action = 0
        pygame.mixer.Channel(1).set_volume(1.0)


def big_buttons(img1, img2, x, y, n):
    if (n == 1 and big_ones.auto) or (n == 2 and big_ones.man) or (n == 3 and big_ones.loop):
        screen.blit(img2, (x, y))
    else:
        screen.blit(img1, (x, y))
    if ((x + 36) > mouse[0] > x and (y + 25) > mouse[1] > y) and (click[0] == 1) and (not Mouse.clicked):
        Mouse.clicked = True

        if (n == 1) and (not big_ones.auto):
            big_ones.auto = (not big_ones.auto)
            if big_ones.auto:
                if big_ones.recent == 2:
                    big_ones.man = 0
                big_ones.recent = 1
                big_ones.song = "AUTO"
        elif (n == 2) and (not big_ones.man):
            big_ones.man = (not big_ones.man)
            if big_ones.man:
                if big_ones.recent == 1:
                    big_ones.auto = 0
                big_ones.recent = 2
                big_ones.song = "MANUAL"
        elif n == 3:
            big_ones.loop = (not big_ones.loop)
        print(big_ones.recent)
        global change_occurred
        change_occurred += 2


def small_buttons():
    global change_occurred
    for i in range(0, len(songs) - 1):
        # print(songs[i])
        Mouse.user_action = 0
        a = Mouse.scroll
        b = (153 > mouse[0] > 37)
        c = (62 + (15 * i) - a)
        d = (62 + (15 * (i - 1)) - a)
        e = (c > mouse[1] > d)
        big_ones.f = len(songs[i])
        # 37, 61
        if (b and e) and (39 < d < 240):
            textbox(str(songs[i][8:big_ones.f - 4]), 37, d, font2, True)
            change_occurred += 1
            if click[0] and not Mouse.clicked:
                pygame.mixer.quit()
                pygame.mixer.init()
                tune = pygame.mixer.Sound(songs[i])
                music_channel = pygame.mixer.Channel(1)
                Mouse.user_action = True

                if pygame.mixer.get_busy():
                    tune.get_length()
                    music_channel.fadeout(2000)
                    music_channel.play(tune, 0, 0, 2000)
                    big_ones.stored = songs[i]
                    big_ones.song = songs[i][8:big_ones.f - 4]
                    music_channel.set_endevent(pygame.constants.USEREVENT)
                else:
                    music_channel.play(tune, 0, 0, 2000)
                    big_ones.stored = songs[i]
                    big_ones.song = songs[i][8:big_ones.f - 4]
                    music_channel.set_endevent(pygame.constants.USEREVENT)
                music_channel.set_volume(1.0)
                big_ones.man = True
                big_ones.auto = False
                big_ones.recent = 2
        elif 39 < d < 240:
            textbox(str(songs[i][8:big_ones.f - 4]), 37, d, font2, False)


update_counter = 0


def scroll_box():
    a = 71 + (Mouse.scroll / 15 + 15) * 146 / (len(songs))
    screen.blit(scroller, (190, a))
    # 14, 152
    if click[0] and (71 + 154 > mouse[1] > 71) and (191 < mouse[0] < 205):
        Mouse.scrolling = True
        Mouse.clicked = True

    if Mouse.scroll > (len(songs) * 15 - 10):
        Mouse.scroll = (len(songs) * 15 - 10)

    if Mouse.clicked and Mouse.scrolling:

        if mouse[1] <= 71:
            Mouse.scroll = -15
        elif mouse[1] >= 212:
            Mouse.scroll = (len(songs) * 15 - 212)
        elif 227 >= a + 9 >= 61:
            Mouse.scroll = ((mouse[1] - 71) * 15 * (len(songs) - 1) / 146)
        elif (a + 10) > 227:
            Mouse.scroll = (len(songs) * 15 - 212)
        else:
            Mouse.scrolling = False
    if click[0] and (74 > mouse[1] > 60) and (191 < mouse[0] < 205) and (Mouse.scroll > -15):
        Mouse.scroll -= 8

    if click[0] and (242 > mouse[1] > 228) and (191 < mouse[0] < 205) and (Mouse.scroll < len(songs) * 15 - 212):
        Mouse.scroll += 8

    if Mouse.user_action < 6:
        Mouse.user_action += 1


done = False
while not done:
    clock.tick(60)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    if click[0] == 0:
        Mouse.clicked = False
    for event in pygame.event.get():
        change_occurred += 1
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5 and (Mouse.scroll < (len(songs) * 15) - 210):
                Mouse.scroll += 45
            elif event.button == 4 and (Mouse.scroll >= 15):
                Mouse.scroll -= 45
            elif Mouse.scroll > (len(songs) * 15 - 210):
                Mouse.scroll = (len(songs) * 15 - 210)

        if event.type == SONG_END:
            autoplay()
    if change_occurred > 0:
        print("updated" + str(change_occurred))
        screen.blit(background, (0, 0))
        screen.blit(pillar, (0, 0))
        screen.blit(pillar, (210, 0))
        screen.blit(frame, (25, 53))
        screen.blit(scrollbar, (189, 59))

        textbox('Playing:', 32, 17, font2, False, GOLD)

        scroll_box()
        small_buttons()
        screen.blit(cover, (26, 33))
        screen.blit(cover2, (31, 242))
        # 96, 251
        song_status(big_ones.song)
        textbox((str(len(songs))) + " / " + (str(len(songs))), 96, 251, font1, False, GOLD)
        big_buttons(auto_off, auto_on, 87, 8, 1)
        big_buttons(manual_off, manon, 129, 8, 2)
        big_buttons(loop_off, loop_on, 171, 8, 3)

        pygame.display.flip()
        change_occurred -= 1

pygame.quit()
