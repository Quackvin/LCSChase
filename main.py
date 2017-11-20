import pygame
import playerClass
import rules

(width, height) = (300, 300)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

player = playerClass.Player(150, 150)
enemy = playerClass.Enemy(40, 50, player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_r:
                player = playerClass.Player(10, 10)
                enemy = playerClass.Enemy(40, 50)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.setXVel(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.setYVel(0)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.increaseVel(-1, 0)
    if keys[pygame.K_RIGHT]:
        player.increaseVel(1, 0)
    if keys[pygame.K_UP]:
        player.increaseVel(0, -1)
    if keys[pygame.K_DOWN]:
        player.increaseVel(0, 1)



    screen.fill((50, 100, 200))

    player.draw(pygame, screen)
    player.move(width, height)
    enemy.draw(pygame, screen)
    enemy.move(width, height)
    enemy.createFeatureVector()

    pygame.display.flip()

pygame.quit()
