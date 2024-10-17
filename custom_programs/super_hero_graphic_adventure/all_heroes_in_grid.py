from pathlib import Path
import pygame
import sys

# Path to your heroes_advanced.txt file
path = Path('heroes_advanced.txt')

# Lists to store hero data
hero_names = []
hero_strengths = []
hero_attack_powers = []
hero_power_locations = []
hero_home_extra_damages = []
hero_main_images = []
hero_location_images = []

# Read the content of the file and split it ainto lines
lines = path.read_text().splitlines()

# Ignore the first line since it just describes the data (skipping header)
lines = lines[3:]

# Loop through each line and store the hero details in lists
for line in lines:
    # Split line into the hero details
    hero_name, hero_strength, hero_attack_power, hero_power_location, hero_home_extra_damage, hero_main_image, hero_location_image = line.split()
    
    # Convert strength and attack power to integers, extra damage to float
    hero_strength = int(hero_strength)
    hero_attack_power = int(hero_attack_power)
    hero_home_extra_damage = float(hero_home_extra_damage)
    
    # Append the data to corresponding lists
    hero_names.append(hero_name)
    hero_strengths.append(hero_strength)
    hero_attack_powers.append(hero_attack_power)
    hero_power_locations.append(hero_power_location)
    hero_home_extra_damages.append(hero_home_extra_damage)
    hero_main_images.append(hero_main_image)
    hero_location_images.append(hero_location_image)


# Initialize Pygame
pygame.init()

# Set up the display
window_width, window_height = (256 * 3), (256 * 3)
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Superhero Gallery')

# Image configuration
image_width, image_height = 256, 256  # Size of each image
padding = 0  # Space between images
images_per_row = 3  # Number of images per row

# Load all hero images
hero_images = []
image_base_path = Path("D:\OneDrive\Albright\CSC141\super_hero_game\images")

for img_file in hero_main_images:
    image_path = image_base_path / img_file  # add the path and the image.jpg
    image = pygame.image.load(str(image_path))
    image = pygame.transform.scale(image, (image_width, image_height))  # Resize image
    hero_images.append(image)
  

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    window.fill((0, 0, 0))  # Black background

    # Display images in rows of 3
    for i, image in enumerate(hero_images): # Enumerate goes thtough list while incrementing i
        if image:
            row = i // images_per_row # Calculate the row number in a layout. // is integer division
            col = i % images_per_row #Modulo operator
            x = col * (image_width + padding) + padding
            y = row * (image_height + padding) + padding
            window.blit(image, (x, y)) # Short for Block Transfer and puts the image on the screen

    # Update the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()
