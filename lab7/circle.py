import pygame
pygame.init()
W, H=500, 500
screen=pygame.display.set_mode((W, H))
x=W//2
y=H//2
WHITE=(255, 255, 255)
RED=(255, 0, 0)
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>30: y-=20
    if pressed[pygame.K_DOWN] and y<470: y+=20
    if pressed[pygame.K_LEFT] and x>30: x-=20
    if pressed[pygame.K_RIGHT] and x<470: x+=20
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 25)

    pygame.display.update()
    clock.tick(60)