import pygame
import random

pygame.init()

display = pygame.display.set_mode((1000, 700), pygame.RESIZABLE)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

run = True
up = False
left = False
down = False
right = False
speed = 10
count_of_tails = 1

apples = list()
tails = list()

player = [[pygame.Rect(500, 350, 30, 30), (0,255,0)]]

blocks = [[pygame.Rect(-10, 0, 11, 700), (255,225,255)], [pygame.Rect(0, -10, 1000, 11), (255,225,255)],
          [pygame.Rect(999, 0, 11, 700), (255,225,255)], [pygame.Rect(0, 699, 1000, 11), (255,225,255)]]

while run:
    movement = [0,0]

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_KP8] and not down:
        up = True; down = False; left = False; right = False

    if keys[pygame.K_KP4] and not right:
        left = True; right = False; up = False; down = False

    if keys[pygame.K_KP6] and not left:
        right = True; left = False; up = False; down = False

    if keys[pygame.K_KP2] and not up:
        down = True; up = False; left = False; right = False

    if up:
        movement[1] -= speed

    if down:
        movement[1] += speed

    if left:
        movement[0] -= speed

    if right:
        movement[0] += speed

    for i in player:
        if i[0].x < 0:
            i[0].x = 970
        elif i[0].x > 970:
            i[0].x = 0
        else:
            i[0].x += movement[0]

        if i[0].y < 0:
            i[0].y = 670
        elif i[0].y > 670:
            i[0].y = 0
        else:
            i[0].y += movement[1]

    display.fill((0,0,0))

    tails.insert(0, [pygame.Rect(player[0][0].x, player[0][0].y, 30, 30), (0,255,0)])

    if apples != []:
        if player[0][0].colliderect(apples[0][0]):
            count_of_tails += 3
            apples.remove(apples[0])

    if apples == []:
        apples.append([pygame.Rect(random.randint(0, 970), random.randint(0, 670), 30, 30), (255,0,0)])

    for block in blocks:
        pygame.draw.rect(display, block[1], block[0])

    for play in player:
        pygame.draw.rect(display, play[1], play[0])

    for apple in apples:
        pygame.draw.rect(display, apple[1], apple[0])

    for ad in tails:
        pygame.draw.rect(display, ad[1], ad[0])

    if len(tails) > count_of_tails:
        tails.pop()

    for delete in range(5, len(tails)):
        if len(tails) > 6 and len(tails) > delete:
            if player[0][0].colliderect(tails[delete][0]):
                for move in range(delete, len(tails)-1):
                    tails.remove(tails[-1])
                    count_of_tails -= 1

    clock.tick(999)
    pygame.time.delay(30)
    pygame.display.update()
