import pygame
pygame.init()
#Creating the display
gamescreen=pygame.display.set_mode((1200,500))
pygame.display.set_caption("Arsalaan Yafai")
#game species variables
exit_game=False
game_over=False
#Creating Game Loop

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
        print("You have pressed right arrow key")

pygame.quit()
quit()
