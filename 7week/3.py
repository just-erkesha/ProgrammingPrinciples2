import pygame#access the PyGame framework.
pygame.init()#initializes all the modules required for PyGame

clock = pygame.time.Clock()
display = pygame.display.set_mode((800,600))

pygame.display.update()
open = True
x=400
y=300
xSpeed=0
ySpeed=0

while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ySpeed=-20
            elif event.key == pygame.K_DOWN:
                ySpeed=20
            elif event.key == pygame.K_LEFT:
                xSpeed=-20
            elif event.key == pygame.K_RIGHT:
                xSpeed=20
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ySpeed=0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xSpeed=0

    display.fill((255, 255, 255))

    if x > 775:
        xSpeed=0
        x-=1
    elif x < 25:
        xSpeed=0
        x+=1
    else: x+=xSpeed


    if y > 575:
        ySpeed=0
        y-=1
    elif y <= 25:
        ySpeed=0
        y+=1
    else: y+=ySpeed

    pygame.draw.circle(display, (255, 0, 0), (x, y), 25)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
