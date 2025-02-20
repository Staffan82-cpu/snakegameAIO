import pygame
from ui import account_screen, welcome_screen

# Run Account Creation & Login
pygame.init()
username = account_screen()
if username:
    start_game = welcome_screen(username)

    if start_game:
        from game import run_snake_game
        run_snake_game()
