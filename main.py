import pygame
import playerClass
import rules

(width, height) = (300, 300)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

player = playerClass.Player(10,10)
enemy = playerClass.Enemy(40,50)

ruleset = rules.Ruleset(50,0.9,0.5)
ruleset.initiliseSet()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveH(-10)
            if event.key == pygame.K_RIGHT:
                player.moveH(10)
            if event.key == pygame.K_UP:
                    player.moveV(10)
            if event.key == pygame.K_DOWN:
                player.moveV(-10)

    screen.fill((50,100,200))

    ruleset.actionRules(player, enemy)
    ruleset.GA()
    ruleset.remove()

    if enemy.x<0 or enemy.x > 300:
        enemy.x = 150
        enemy.y = 150
    if enemy.y<0 or enemy.y > 300:
        enemy.x = 150
        enemy.y = 150

    pygame.draw.rect(screen, (255,255,255), (player.x,player.y,10,10))
    pygame.draw.rect(screen, (255,0,0), (enemy.x,enemy.y,10,10))
    pygame.display.flip()


pygame.quit()

