import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player Selection")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
FONT = pygame.font.Font(None, 76)

def draw_menu():
    WINDOW.fill(WHITE)
    text = FONT.render("Select number of players (2-4):", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    WINDOW.blit(text, text_rect)

    # Display options
    options = ["2", "3", "4"]
    option_y = HEIGHT // 2 + 50
    for option in options:
        option_text = FONT.render(option, True, BLACK)
        option_rect = option_text.get_rect(center=(WIDTH // 2, option_y))
        WINDOW.blit(option_text, option_rect)
        option_y += 50

    pygame.display.flip()

def main():
    # Main game loop
    running = True
    while running:
        draw_menu()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    print("Starting game with 2 players")
                    # Call a function to start the game with 2 players
                elif event.key == pygame.K_3:
                    print("Starting game with 3 players")
                    # Call a function to start the game with 3 players
                elif event.key == pygame.K_4:
                    print("Starting game with 4 players")
                    # Call a function to start the game with 4 players

if __name__ == "__main__":
    main()
    pygame.display.update()