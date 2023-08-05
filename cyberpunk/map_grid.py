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

# Add menu selection for background
backgrounds = ['media/background_assets/cyber_street.png', 'media/background_assets/cyber_skyscraper.png', 'media/background_assets/cyber_desert.png']
for i, name in enumerate(backgrounds):
    print(f"{i+1}. {name.split('/')[-1]}")  # Print the name without the path
choice = int(input("Enter the number of the background you want to use: "))
original_background = pygame.image.load(backgrounds[choice - 1])
background = pygame.transform.scale(original_background, window_size)

def game_loop():
    clock = pygame.time.Clock()
    player = GameObject(0, 0, 'media/character_assets/cyber_main_char.png')
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.y > 0:
                       player.y -= 1
                elif event.key == pygame.K_DOWN and player.y < GRID_SIZE - 1:
                        player.y += 1
                elif event.key == pygame.K_LEFT and player.x > 0:
                       player.x -= 1
                elif event.key == pygame.K_RIGHT and player.x < GRID_SIZE - 1:
                        player.x += 1

        window.blit(background, (0, 0))
        draw_grid()
        player.draw(window)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
