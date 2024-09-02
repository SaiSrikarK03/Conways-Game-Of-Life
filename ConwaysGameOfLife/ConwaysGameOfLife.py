import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 40
CELL_SIZE = WIDTH // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Create the grid
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Font for UI text
font = pygame.font.Font(None, 36)

# Flag to toggle the display of pause/resume UI
show_status_ui = True

def draw_grid():
    """Draw the grid lines on the screen."""
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def update_grid(grid):
    """Update the grid based on Conway's Game of Life rules."""
    new_grid = np.copy(grid)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            alive_neighbors = np.sum(grid[max(0, row-1):min(row+2, GRID_SIZE), max(0, col-1):min(col+2, GRID_SIZE)]) - grid[row, col]
            if grid[row, col] == 1:  # Alive cell
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[row, col] = 0  # Cell dies
            else:  # Dead cell
                if alive_neighbors == 3:
                    new_grid[row, col] = 1  # Cell becomes alive
    return new_grid

def draw_status(paused):
    """Draw the status of the game (paused/resumed) on the screen."""
    status_text = "Paused" if paused else "Running"
    text_color = WHITE if paused else (0, 255, 0)
    status_surface = font.render(status_text, True, text_color)
    screen.blit(status_surface, (10, 10))  # Position the text in the top-left corner

def main():
    global show_status_ui
    running = True
    paused = True  # Game starts in paused mode
    clock = pygame.time.Clock()
    
    while running:
        screen.fill(BLACK)
        draw_grid()
        
        # Draw cells
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row, col] == 1:
                    pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Toggle pause/play with space bar
                    paused = not paused
                elif event.key == pygame.K_h:  # Toggle the visibility of the status UI with 'H'
                    show_status_ui = not show_status_ui

        # Only allow painting when the game is paused
        if paused:
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0]:  # Left mouse button is pressed
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE
                grid[row, col] = 1  # Set cell to alive (white)

            if mouse_pressed[2]:  # Right mouse button is pressed
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE
                grid[row, col] = 0  # Set cell to dead (black)

        # Update the grid if the game is running
        if not paused:
            grid[:] = update_grid(grid)

        # Draw the status UI if it's enabled
        if show_status_ui:
            draw_status(paused)

        pygame.display.flip()
        clock.tick(25)  # Limit FPS to 30

if __name__ == "__main__":
    main()
