import pygame

# Set up the grid
grid_size = 8
square_size = 80
grid_width = grid_size * square_size
grid_height = grid_size * square_size

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Black
black_bishop = pygame.image.load("./assets/images/black_bishop.png")
black_king = pygame.image.load("./assets/images/black_king.png")
black_knight = pygame.image.load("./assets/images/black_knight.png")
black_pawn = pygame.image.load("./assets/images/black_pawn.png")
black_queen = pygame.image.load("./assets/images/black_queen.png")
black_rook = pygame.image.load("./assets/images/black_rook.png")

black_list = [black_rook, black_knight, black_bishop,
              black_queen, black_king, black_bishop, black_knight, black_rook]

# White
white_bishop = pygame.image.load("./assets/images/white_bishop.png")
white_king = pygame.image.load("./assets/images/white_king.png")
white_knight = pygame.image.load("./assets/images/white_knight.png")
white_pawn = pygame.image.load("./assets/images/white_pawn.png")
white_queen = pygame.image.load("./assets/images/white_queen.png")
white_rook = pygame.image.load("./assets/images/white_rook.png")

white_list = [white_rook, white_knight, white_bishop,
              white_queen, white_king, white_bishop, white_knight, white_rook]


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((grid_width, grid_height))
pygame.display.set_caption("Chess")


def pawns_pos():
    x = 0
    for pawns in black_list:
        screen.blit(pawns, (x, 0))
        x += 80

    x = 0
    for pawns in white_list:
        screen.blit(pawns, (x, 560))
        x += 80

    for i in range(8):
        screen.blit(black_pawn, (i * 80, 80))
        screen.blit(white_pawn, (i * 80, 480))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the grid
    for row in range(grid_size):
        for col in range(grid_size):
            x = col * square_size
            y = row * square_size

            # Alternate the colors of the squares
            if (row + col) % 2 == 0:
                color = LIGHT_GRAY
            else:
                color = DARK_GRAY

            pygame.draw.rect(screen, color, (x, y, square_size, square_size))

    # Display the image
    pawns_pos()

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
