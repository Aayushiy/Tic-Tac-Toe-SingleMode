import pygame
from sys import exit
from grid import Grid


win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic Tac Toe")


grid= Grid()

player = "X"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                print(pos[0]//200,pos[1]//200) # amazing trick
                grid.get_mouse(pos[0]//200,pos[1]//200,player)
                if grid.switch_player:
                    if player=="X":
                        player="O"
                    else:
                        player="X"
                grid.print_grid()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False

    win.fill((0,0,0))

    grid.draw(win)
    
    
    pygame.display.flip()

