import pygame
import sys
from random import uniform # this one is from mr gpt

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Stock class
class Stock:
    def __init__(self, name, initial_price):
        self.name = name
        self.starting_price = initial_price
        self.current_price = initial_price
        self.quantity = 0

stocks = [
    Stock("SUS", 50),
    Stock("AMO", 30),
    Stock("GUS", 100),
    Stock("KMS", 10),
    # TODO: add more stocks
]

# Create Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stock Trading Simulator")

# ^
# |
# from the wonderful and exuberant mr gpt-3.5
# |
# v

# Clock for controlling FPS
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update logic (simulate stock market, etc.)
    for stock in stocks:
        stock.current_price += uniform(-1, 1)  # Adjust the range as needed
        stock.current_price = max(1, stock.current_price)  # Ensure price doesn't go below 1
        # Add more logic here based on the current price of the stock

    # Drawing
    screen.fill(WHITE)

    # Display stocks
    for i, stock in enumerate(stocks):
        stock_color = GREEN if stock.current_price >= stock.starting_price else RED
        pygame.draw.rect(screen, stock_color, (50 + i * 200, 50, 150, 100))  # Stock button
        stock_text = font.render(f"{stock.name}", True, WHITE)
        screen.blit(stock_text, (70 + i * 200, 70))

        # Display stock name and price below the button
        pygame.draw.rect(screen, stock_color, (50 + i * 200, 160, 150, 40))
        stock_info_text = font.render(f"${stock.current_price:.2f}", True, WHITE)
        screen.blit(stock_info_text, (70 + i * 200, 170))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(2)

# Quit Pygame
pygame.quit()
sys.exit()
