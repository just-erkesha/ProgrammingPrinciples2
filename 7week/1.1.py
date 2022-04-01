import pygame 
from datetime import datetime 
pygame.init() 
 
size = (1200, 1000) 
 
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Clock") 
 
done = False 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    screen.fill((255, 255, 255)) 
    date = datetime.today() 
    hours = int(date.strftime("%I")) 
    minutes = int(date.strftime("%M")) 
    clock = pygame.image.load(r'/Applications/docs/lessons/PP2/7week/clock.png') 
    left = pygame.image.load(r'/Applications/docs/lessons/PP2/7week/1hand.png') 
    left_copy = pygame.transform.rotate(left, minutes * (-6)) 
    right = pygame.image.load(r'/Applications/docs/lessons/PP2/7week/2hand.png') 
    right_copy = pygame.transform.rotate(right, hours * (-30)) 
    screen.blit(clock, (0, 0)) 
    screen.blit(left_copy, (705 - int(left_copy.get_width() / 2), 525 - int(left_copy.get_height() / 2))) 
    screen.blit(right_copy, (705 - int(right_copy.get_width() / 2), 525 - int(right_copy.get_height() / 2))) 
 
    pygame.display.flip() 
pygame.quit()