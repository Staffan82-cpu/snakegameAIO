import pygame
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Login")

# Colors
WHITE, BLACK, GREEN = (255, 255, 255), (0, 0, 0), (0, 255, 0)

# Font
FONT = pygame.font.Font(None, 36)

# File to store user credentials
USER_DATA_FILE = "users.txt"

def save_user(username, password):
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username},{password}\n")

def check_user(username, password):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            stored_user, stored_pass = line.strip().split(",")
            if stored_user == username and stored_pass == password:
                return True
    return False

def draw_text(text, x, y, color=WHITE):
    render = FONT.render(text, True, color)
    screen.blit(render, (x, y))

def account_screen():
    username, password = "", ""
    input_active = "username"  # Track input field
    while True:
        screen.fill(BLACK)
        draw_text("Enter Username:", 50, 50)
        draw_text(username, 50, 80, GREEN)
        draw_text("Enter Password:", 50, 150)
        draw_text("*" * len(password), 50, 180, GREEN)
        draw_text("Press ENTER to Submit", 50, 250)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if check_user(username, password) or username.strip() and password.strip():
                        save_user(username, password)
                        return username  # Login Success
                elif event.key == pygame.K_BACKSPACE:
                    if input_active == "username":
                        username = username[:-1]
                    else:
                        password = password[:-1]
                elif event.key == pygame.K_TAB:
                    input_active = "password" if input_active == "username" else "username"
                else:
                    if input_active == "username":
                        username += event.unicode
                    else:
                        password += event.unicode

def welcome_screen(username):
    while True:
        screen.fill(BLACK)
        draw_text(f"Welcome, {username}!", 200, 100, GREEN)
        draw_text("Press SPACE to Start Game", 150, 200)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True  # Start Game
