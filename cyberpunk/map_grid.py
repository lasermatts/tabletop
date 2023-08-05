import pygame
pygame.init()

# Define constants for your grid size (number of cells in width and height)
GRID_SIZE = 8

# Define constants for your cell size (pixels)
CELL_SIZE = 60

# Create the window for the grid
window_size = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)
window = pygame.display.set_mode(window_size)

class GameObject:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)

    def draw(self, window):
        window.blit(self.image, (self.x * CELL_SIZE, self.y * CELL_SIZE))

# Define a function to draw a grid on the window
def draw_grid():
    for x in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE): 
        for y in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, (255, 255, 255), rect, 1)

def game_loop():
    clock = pygame.time.Clock()
    player = GameObject(0, 0, 'cyber_main_char.png')
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.y -= 1
                elif event.key == pygame.K_DOWN:
                    player.y += 1
                elif event.key == pygame.K_LEFT:
                    player.x -= 1
                elif event.key == pygame.K_RIGHT:
                    player.x += 1

        window.fill((0, 0, 0))
        draw_grid()
        player.draw(window)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()