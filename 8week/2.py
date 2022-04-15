#Imports
import pygame, sys
import random, time

pygame.init()
screen = pygame.display.set_mode((500, 500))#main window
pygame.display.set_caption("Snake")

#Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))

class Snake:
    def __init__(self, x, y):#initializes the attributes of the class
        self.size = 1
        self.elements = [[x,y]]#[x0,y0], [x1,x2], ...
        self.radius = 10
        self.dx = 5#to the right
        self.dy = 0
        self.is_add = False
        self.speed = 25
        self.score = 0
        self.level=1
    
    def draw(self):#for each element draw a circle
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)
    
    def add_to_snake(self):
        self.size +=1
        self.score+=1
        self.elements.append([0,0])#adding x and y position of new tail to the array
        self.is_add = False
        if self.score%5==0:
            self.speed += 5
            self.level+=1 #each 5 food gives new level and increased speed

    def move(self):
        if self.is_add:
            self.add_to_snake()
            
        for i in range(self.size - 1, 0, -1):#elenments of array reversed
            self.elements[i][0] = self.elements[i-1][0]#new tail will have coordinates of last tail
            self.elements[i][1] = self.elements[i-1][1]

        self.elements[0][0] += self.dx#first element is x-coordinate
        self.elements[0][1] += self.dy

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <=foodx + 10 and foody <= y <=foody + 10:#head of snake meets food
            return True
        return False

class Food:
    def __init__(self):
        self.x = random.randint(0,490)#rndom positions of food
        self.y = random.randint(0,490)

    def gen(self):
        self.x = random.randint(0,490)
        self.y = random.randint(0,490)

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 10))#draw food

snake = Snake(100, 100)
food = Food()
running = True
FPS = 30#setting fps
step = 5

clock = pygame.time.Clock()

while running:
    clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -step:#direction of snake
                snake.dx = step
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != step:
                snake.dx = -step
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != step:
                snake.dx = 0
                snake.dy = -step
            if event.key == pygame.K_DOWN and snake.dy != -step:
                snake.dx = 0
                snake.dy = step

    if snake.eat(food.x, food.y):#chaecks
        snake.is_add = True
        food.gen()
        
        #checks on borders
    if snake.elements[0][0] > 490 or snake.elements[0][0] < 10 or snake.elements[0][1] > 490 or snake.elements[0][1] < 10:
        time.sleep(1)        
        screen.fill((255, 0, 0))
        screen.blit(game_over, (90,200))
          
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit() 


    snake.move()
    screen.fill((0, 0, 0))
    #showing on screen
    scores = font_small.render(str(snake.score), True, (225,0,0))
    screen.blit(scores, (10,10))
    lev = font_small.render("Level-"+str(snake.level), True, (255, 255, 255))
    screen.blit(lev, (200,20))
    
    snake.draw()
    food.draw()
    pygame.display.flip()
pygame.quit()
quit()
