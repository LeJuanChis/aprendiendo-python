import pygame 
import random

class snake:
    def __init__(self, window):
        self.x = 0
        self.y = 0
        self.window = window
        self.dif = 0
    
    def draw(self):
        pygame.draw.rect(self.window, (0, 255, 255), (self.x, self.y, 10, 10))

    def move(self):
        '''0 = abajo, 1 = arriba, 2= derecha, 3 = izquierda'''
        if self.dif == 0:
            self.x += 10   
        elif self.dif == 1:
            self.x -= 10
        elif self.dif == 2:
            self.y += 10
        elif self.dif == 3:
            self.y -= 10    


class food:
    def __init__(self, window):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10
        self.window = window
    
    def draw(self):
        pygame.draw.rect(self.window, (0, 0, 255), (self.x, self.y, 10, 10)) 

    def new(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10                   

def refresh(window):
    window.fill((0,0,0))
    food.draw()
    for i in range(len(snake)):
        snake[i].draw()
    

def follow_snake():
    for i in range(len(snake) -1):
        snake[len(snake) - i -1].x = snake[len(snake) - i -2].x
        snake[len(snake) - i -1].y = snake[len(snake) - i -2].y


def main():
    global snake, food
    
    window = pygame.display.set_mode((600, 600))
    window.fill((0,0,0))

    food = food(window)
    snake = [snake(window)]
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake[0].dif = 0
                elif event.key == pygame.K_LEFT:
                    snake[0].dif = 1
                elif event.key == pygame.K_DOWN:
                    snake[0].dif = 2    
                elif event.key == pygame.K_UP:
                    snake[0].dif = 3            
        snake[0].move()        
        refresh(window)    

        follow_snake() 

        pygame.display.update()
        pygame.time.delay(100)

        if snake[0].x == food.x and snake[0].y == food.y:
            food.new()
            snake.append(snake(window))
         

main()
