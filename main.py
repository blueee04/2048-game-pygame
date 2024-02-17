import json,sys,time,pygame
from pygame.locals import *
from gamed import *

white = (255,255,255)
black = (0,0,0) 

class buttons():
    def __init__(self, x, y, width, height, colour, text=""):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    def draw(self, win, text, font):
        drawRoundRect(win, self.colour, (self.x, self.y, self.width, self.height))
        if self.text != "":
            text = font.render(self.text, True, (255, 255, 255))
            win.blit(text, (self.x+self.width//2-text.get_width()//2, self.y+self.height//2-text.get_height()//2))
    
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def drawRoundRect(win, colour, rect, rad=10):
    rect = Rect(rect)
    color = pygame.Color(*colour)
    alpha = color.a
    color.a = 0
    pos = rect.topleft
    rect.topleft = 0,0
    rectangle = pygame.Surface(rect.size,SRCALPHA)

    circle = pygame.Surface([rad*2]*2,SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle = pygame.transform.smoothscale(circle,[rad]*2)

    radius = rectangle.blit(circle,(0,0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle,rect.topright)
    rectangle.blit(circle,rect.bottomleft)
    rectangle.fill((0,0,0),rect.inflate(-rad,0))
    rectangle.fill((0,0,0),rect.inflate(0,-rad))

    rectangle.fill((0,0,0),rect.inflate(-rad,-rad))
    rectangle.fill(colour,special_flags=BLEND_RGBA_MIN)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MAX)
    return win.blit(rectangle,pos)

def ShowMenu():
    light_theme = buttons(50, 50, 200, 50, "Light Theme", (255, 255, 255))
    dark_theme = buttons(50, 150, 200, 50, "Dark Theme", (0, 0, 0))
    theme = ""
    theme_selected = False  
    
    _2048 = buttons(50, 250, 200, 50, "2048", (255, 255, 255))
    _1024 = buttons(50, 350, 200, 50, "1024", (255, 255, 255))
    _512 = buttons(50, 450, 200, 50, "512", (255, 255, 255))
    _256 = buttons(50, 550, 200, 50, "256", (255, 255, 255))

    difficulty = 0
    diff_selected = False
    
    # create play button
    play = buttons(tuple(c["colour"]["light"]["2048"]),
                  235, 400, 45, 45, "play")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if light_theme.isOver(pos):
                    theme = "light"
                    theme_selected = True
                if dark_theme.isOver(pos):
                    theme = "dark"
                    theme_selected = True
                if _2048.isOver(pos):
                    difficulty = 2048
                    diff_selected = True
                if _1024.isOver(pos):
                    difficulty = 1024
                    diff_selected = True
                if _512.isOver(pos):
                    difficulty = 512
                    diff_selected = True
                if _256.isOver(pos):
                    difficulty = 256
                    diff_selected = True
                if play.isOver(pos) and theme_selected and diff_selected:
                    return theme, difficulty
        light_theme.draw(screen, font)
        dark_theme.draw(screen, font)
        _2048.draw(screen, font)
        _1024.draw(screen, font)
        _512.draw(screen, font)
        _256.draw(screen, font)
        play.draw(screen, font)
        pygame.display.update()
        import pygame.time

        clock = pygame.time.Clock()
        clock.tick(60)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == K_q):
                # exit if q is pressed 
                pygame.quit()
                sys.exit()

            # check if a button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # select light theme
                if light_theme.isOver(pos):
                    dark_theme.colour = tuple(c["colour"]["dark"]["2048"])
                    light_theme.colour = tuple(c["colour"]["light"]["64"])
                    theme = "light"
                    theme_selected = True

                # select dark theme
                if dark_theme.isOver(pos):
                    dark_theme.colour = tuple(c["colour"]["dark"]["background"])
                    light_theme.colour = tuple(c["colour"]["light"]["2048"])
                    theme = "dark"
                    theme_selected = True
                
                if _2048.isOver(pos):
                    _2048.colour = tuple(c["colour"]["light"]["64"])
                    _1024.colour = tuple(c["colour"]["light"]["2048"])
                    _512.colour = tuple(c["colour"]["light"]["2048"])
                    _256.colour = tuple(c["colour"]["light"]["2048"])
                    difficulty = 2048
                    diff_selected = True
                
                if _1024.isOver(pos):
                    _1024.colour = tuple(c["colour"]["light"]["64"])
                    _2048.colour = tuple(c["colour"]["light"]["2048"])
                    _512.colour = tuple(c["colour"]["light"]["2048"])
                    _256.colour = tuple(c["colour"]["light"]["2048"])
                    difficulty = 1024
                    diff_selected = True
                
                if _512.isOver(pos):
                    _512.colour = tuple(c["colour"]["light"]["64"])
                    _1024.colour = tuple(c["colour"]["light"]["2048"])
                    _2048.colour = tuple(c["colour"]["light"]["2048"])
                    _256.colour = tuple(c["colour"]["light"]["2048"])
                    difficulty = 512
                    diff_selected = True
                
                if _256.isOver(pos):
                    _256.colour = tuple(c["colour"]["light"]["64"])
                    _1024.colour = tuple(c["colour"]["light"]["2048"])
                    _512.colour = tuple(c["colour"]["light"]["2048"])
                    _2048.colour = tuple(c["colour"]["light"]["2048"])
                    difficulty = 256
                    diff_selected = True

                # play game with selected theme
                def playGame(theme, difficulty):
                    # Add the implementation of the playGame function here
                    pass

                if play.isOver(pos):
                    if theme != "" and difficulty != 0:
                        playGame(theme, difficulty)

                # reset theme & diff choice if area outside buttons is clicked
                if not play.isOver(pos) and \
                    not dark_theme.isOver(pos) and \
                    not light_theme.isOver(pos) and \
                    not _2048.isOver(pos) and \
                    not _1024.isOver(pos) and \
                    not _512.isOver(pos) and \
                    not _256.isOver(pos):

                    theme = ""
                    theme_selected = False
                    diff_selected = False

                    light_theme.colour = tuple(c["colour"]["light"]["2048"])
                    dark_theme.colour = tuple(c["colour"]["dark"]["2048"])
                    _2048.colour = tuple(c["colour"]["light"]["2048"])
                    _1024.colour = tuple(c["colour"]["light"]["2048"])
                    _512.colour = tuple(c["colour"]["light"]["2048"])
                    _256.colour = tuple(c["colour"]["light"]["2048"])
                    

            # change colour on hovering over buttons
            if event.type == pygame.MOUSEMOTION:
                if not theme_selected:
                    if light_theme.isOver(pos):
                        light_theme.colour = tuple(c["colour"]["light"]["64"])
                    else:
                        light_theme.colour = tuple(c["colour"]["light"]["2048"])
                    
                    if dark_theme.isOver(pos):
                        dark_theme.colour = tuple(c["colour"]["dark"]["background"])
                    else:
                        dark_theme.colour = tuple(c["colour"]["dark"]["2048"])
                
                if not diff_selected:
                    if _2048.isOver(pos):
                        _2048.colour = tuple(c["colour"]["light"]["64"])
                    else:
                        _2048.colour = tuple(c["colour"]["light"]["2048"])
                    
                    if _1024.isOver(pos):
                        _1024.colour = tuple(c["colour"]["light"]["64"])
                    else:
                        _1024.colour = tuple(c["colour"]["light"]["2048"])
                    
                    if _512.isOver(pos):
                        _512.colour = tuple(c["colour"]["light"]["64"])
                    else:
                        _512.colour = tuple(c["colour"]["light"]["2048"])
                    
                    if _256.isOver(pos):
                        _256.colour = tuple(c["colour"]["light"]["64"])
                    else:
                        _256.colour = tuple(c["colour"]["light"]["2048"])
                
                if play.isOver(pos):
                    play.colour = tuple(c["colour"]["light"]["64"])
                else:
                    play.colour = tuple(c["colour"]["light"]["2048"])


if __name__ == "__main__":
    # load json data
    c = json.load(open("const.json", "r"))

    # set up pygame
    pygame.init()
    # set up screen
    def showMenu():
        # implementation of the showMenu function
        
        screen = pygame.display.set_mode((c["size"], c["size"]))
        pygame.display.set_caption("2048 by Rajit Banerjee")

        # display game icon in window
        icon = pygame.transform.scale(
            pygame.image.load("images/icon.ico"), (32, 32))
        pygame.display.set_icon(icon)

    # set font according to json data specifications
    my_font = pygame.font.SysFont(c["font"], c["fontSize"], bold=True)

    # display the start screen 
    showMenu()