import pygame
import pygame.gfxdraw

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Paint")
pygame.display.set_icon(pygame.image.load("img/icon.png"))
era_icon = pygame.image.load("img/eraser.png").convert_alpha()
era_icon = pygame.transform.scale(era_icon, (34, 34))
rect_icon = pygame.image.load("img/rectangle.png").convert_alpha()
rect_icon = pygame.transform.scale(rect_icon, (35, 30))
trian_icon = pygame.image.load("img/triangle.png").convert_alpha()
trian_icon = pygame.transform.scale(trian_icon, (28, 26)) 


black = (0, 0, 0)# Defining Colors
floralwhite=(255,250,240)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
pink = (255,192,203)
orange = (255,165,0)
yellow = (255,255,0)
violet = (177, 3, 252)
#Defining rect value for colors in colorbox
col1= (822, 81, 30, 34)#left, top, width, height
col2= (856, 81, 34, 34)
col3= (822, 120, 30, 33)
col4= (856, 120, 34, 32)
col5= (822, 156, 30, 33)
col6= (856, 156, 34, 32)
col7= (822, 192, 30, 33)
col8= (856, 192, 34, 32)
col9= (822, 247, 34, 32)
#Rect that highlight which button is selected
buttonselect = (822, 81, 30, 34)

pencolor = black
draw_on = False
last_pos = (0, 0)
radius = 1
screen.fill(floralwhite)
canvas = pygame.Surface((800, 600))
canvas.fill(white)

pygame.display.update()

#Function to draw color box
def color_selection():    
        pygame.gfxdraw.box(screen, col1, black)
        pygame.gfxdraw.box(screen, col2, blue)
        pygame.gfxdraw.box(screen, col3, red)
        pygame.gfxdraw.box(screen, col4, green)
        pygame.gfxdraw.box(screen, col5, pink)
        pygame.gfxdraw.box(screen, col6, orange)
        pygame.gfxdraw.box(screen, col7, yellow)
        pygame.gfxdraw.box(screen, col8, violet)
pygame.mouse.set_cursor(*pygame.cursors.broken_x)#pencil by default

def draw_rect():
    pass


def save():
        name = "image.png"
        pygame.image.save(canvas, name)


done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                    radius -= 1
            if event.key == pygame.K_UP:
                    radius += 1
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                save()
            if event.key == pygame.K_r:# for rectangle
                operation = 1
            if event.key == pygame.K_r:# for triangle
                operation = 2

            
        #Check for mouse clicks
        t = pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(canvas, pencolor, event.pos, radius)
            draw_on = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        if event.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.line(canvas, pencolor, last_pos, event.pos, radius)
            last_pos = event.pos
        if t[0] == 1:     
            mousepos = pygame.mouse.get_pos()
            if 822 < mousepos[0] < 852 and 81 < mousepos[1] < 115:
                pencolor = black       
                buttonselect = col1
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                
            elif 856 < mousepos[0] < 890 and 81 < mousepos[1] < 115:
                pencolor = blue
                buttonselect = col2
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                
            elif 822 < mousepos[0] < 852 and 120 < mousepos[1] < 153:
                pencolor = red
                buttonselect = col3
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                
            elif 856 < mousepos[0] < 890 and 120 < mousepos[1] < 152:
                pencolor = green
                buttonselect = col4
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                
            elif 822 < mousepos[0] < 852 and 156 < mousepos[1] < 189:
                pencolor = pink
                buttonselect = col5
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                
            elif 856 < mousepos[0] < 890 and 156 < mousepos[1] < 188:
                pencolor = orange
                buttonselect = col6
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                
            elif 822 < mousepos[0] < 852 and 192 < mousepos[1] < 225:
                pencolor = yellow
                buttonselect = col7
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                
            elif 856 < mousepos[0] < 890 and 192 < mousepos[1] < 224:
                pencolor = violet
                buttonselect = col8
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            #Eraser
            elif 813 < mousepos[0] < 854 and 247 < mousepos[1] < 285:
                pencolor = white
                buttonselect = col9
                pygame.mouse.set_cursor(*pygame.cursors.diamond)


        

    screen.blit(canvas, (0,0))
    color_selection()
    pygame.gfxdraw.rectangle(screen, buttonselect, white)
    screen.blit(era_icon , ( 822, 247))
    screen.blit(rect_icon , ( 822,290))
    screen.blit(trian_icon , ( 858,290))
    
    
    pygame.display.flip()

pygame.quit()
quit()