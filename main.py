import pygame
import random
pygame.init()
maxX = 700
maxY = 500
size = (maxX, maxY)
screen = pygame.display.set_mode(size)
RED = (255, 0, 0)
White = (255, 255, 255)
black = (0, 0, 0)
x = 200
y = 250
cx = random.randint(100, 650)
cy = random.randint(100, 450)
done = False
score = 0
clock = pygame.time.Clock()
timer = 20  # Decrease this to count down.
dt = 0
font = pygame.font.Font(None, 40)


def menu():
    start = False
    while not start:
        menuTXT = font.render("Welcome press enter to begin", True, RED)
        screen.blit(menuTXT, (maxX / 2 - 150, maxY / 2))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
        pygame.display.flip()


def shape(x, y):
    pygame.draw.line(screen, RED, [x - 50, y], [x + 50, y], 4)
    pygame.draw.line(screen, RED, [x, y - 50], [x, y + 50], 4)
    pygame.draw.circle(screen, RED, [x, y], 50, 4)


menu()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or timer <= 0:
            print("You got " + str(score) + " points")
            done = True
    keystate = pygame.key.get_pressed()
    if (keystate[pygame.K_DOWN] or keystate[pygame.K_s]):
        pygame.Surface.fill(screen, black)
        if (y < maxY - 10):
            y += 10
    if (keystate[pygame.K_UP] or keystate[pygame.K_w]):
        pygame.Surface.fill(screen, black)
        if (y - 10 > 0):
            y -= 10
    if (keystate[pygame.K_RIGHT] or keystate[pygame.K_d]):
        pygame.Surface.fill(screen, black)
        if (x + 10 < maxX):
            x += 10
    if (keystate[pygame.K_LEFT] or keystate[pygame.K_a]):
        pygame.Surface.fill(screen, black)
        if (x - 10 > 0):
            x -= 10
    if (keystate[pygame.K_SPACE]):
        testx = x >= cx - 30 and x <= cx + 30
        testy = y <= cy + 30 and y >= cy - 30
        if (testx) and (testy):
            score += 1
            cx = random.randint(100, 700)
            cy = random.randint(100, 500)

    timer -= dt
    txt = font.render(str(round(timer, 2)), True, RED)
    scoreTXT = font.render("Score " + str(score), True, RED)
    screen.blit(scoreTXT, (600, 70))
    screen.blit(txt, (70, 70))
    dt = clock.tick(30) / 1000
    pygame.draw.circle(screen, RED, [cx, cy], 50, 2)
    shape(x, y)
    pygame.display.flip()
