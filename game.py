import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE, BLACK, GREEN, RED, BLUE = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255)

# Font for displaying text
FONT = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=WHITE):
    """Function to draw text on the screen."""
    render = FONT.render(text, True, color)
    screen.blit(render, (x, y))

def run_snake_game():
    """Main function for running the Snake game."""
    
    # Snake setup
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)

    # Food setup
    food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, 
            random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    # Game variables
    score = 0
    level = 1
    foods_eaten = 0
    speed = 10

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        # Handle events (Key press, quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)

        # Move Snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Check collision with walls or itself
        if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            running = False  # Game Over

        snake.insert(0, new_head)

        # Check if food is eaten
        if new_head == food:
            score += 10
            foods_eaten += 1

            # Generate new food
            food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, 
                    random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

            # Level up every 10 foods eaten
            if foods_eaten == 10:
                foods_eaten = 0
                level += 1
                speed += 2  # Increase speed each level
                if level > 10:
                    running = False  # End game if max level is reached
        else:
            snake.pop()  # Remove tail if no food eaten

        # Draw Snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

        # Draw Food
        pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

        # Draw Score & Level
        draw_text(f"Score: {score}", 10, 10)
        draw_text(f"Level: {level}", 500, 10)

        pygame.display.flip()
        clock.tick(speed)  # Increase game speed with level

    game_over_screen(score)

def game_over_screen(final_score):
    """Show the Game Over screen after losing."""
    while True:
        screen.fill(BLACK)
        draw_text("GAME OVER", 230, 150, RED)
        draw_text(f"Final Score: {final_score}", 220, 200)
        draw_text("Press R to Restart or Q to Quit", 140, 250)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run_snake_game()  # Restart Game
                elif event.key == pygame.K_q:
                    return  # Quit to main menu
