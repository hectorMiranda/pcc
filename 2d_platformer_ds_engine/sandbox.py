import pygame
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the clock for framerate
clock = pygame.time.Clock()

# Game loop flag
running = True

# Player properties
player_pos = [screen_width // 2, screen_height // 2]
player_speed = 5

# Obstacle properties
obstacle_pos = [100, 100]
obstacle_size = 50

# Game data
game_data = {
    'time': [],
    'obstacles_avoided': []
}

start_time = pygame.time.get_ticks()
obstacles_avoided = 0




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Check for collision with the obstacle
    if (player_pos[0] <= obstacle_pos[0] + obstacle_size and
            player_pos[0] + 50 >= obstacle_pos[0] and
            player_pos[1] <= obstacle_pos[1] + obstacle_size and
            player_pos[1] + 50 >= obstacle_pos[1]):
        obstacles_avoided += 1
        # Move the obstacle to a new random position
        obstacle_pos = [np.random.randint(0, screen_width - obstacle_size),
                        np.random.randint(0, screen_height - obstacle_size)]

    # Fill the screen with a color
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (0, 255, 0), (player_pos[0], player_pos[1], 50, 50))

    # Draw the obstacle
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(60)

# Record the game data
end_time = pygame.time.get_ticks()
game_data['time'].append((end_time - start_time) / 1000)
game_data['obstacles_avoided'].append(obstacles_avoided)

# Quit Pygame
pygame.quit()


# Convert the game data to a Pandas DataFrame
df = pd.DataFrame(game_data)

# Print summary statistics
print(df.describe())

# Plot a scatter plot of time vs obstacles avoided
plt.scatter(df['time'], df['obstacles_avoided'])
plt.xlabel('Time (seconds)')
plt.ylabel('Obstacles Avoided')
plt.title('Player Performance')
plt.show()

# Fit a linear regression model
model = LinearRegression()
model.fit(df[['time']], df['obstacles_avoided'])
print(f"Coefficient: {model.coef_[0]}, Intercept: {model.intercept_}")
