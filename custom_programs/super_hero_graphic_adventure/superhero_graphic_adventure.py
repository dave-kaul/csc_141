from pathlib import Path
import pygame
import random
import sys
import os
os.system('cls')
# Changer the current working directory
#new_path = "'D:\OneDrive\Albright\CSC141\super_hero_game\images'"
#os.chdir(new_path)

path = Path('heroes_advanced.txt')  # Path to your file

# Lists to store hero data
hero_names = []
hero_strengths = []
hero_attack_powers = []
hero_power_locations = []
hero_home_extra_damages = []
hero_main_images = []
hero_location_images = []

# Read the content of the file and split it into lines
lines = path.read_text().splitlines()

# Ignore the first line since it just describes the data
lines = lines[3:]

# Loop through each line and store the hero details in lists
for line in lines:
    # Split line into respective hero details
    hero_name, hero_strength, hero_attack_power, hero_location, hero_home_extra_damage, hero_main_image, hero_location_image = line.split()
    
    # Convert strength and attack power to integers, extra damage to a float number since an int number is not specific enough
    hero_strength = int(hero_strength)
    hero_attack_power = int(hero_attack_power)
    hero_home_extra_damage = float(hero_home_extra_damage)
    
    # Append the data to corresponding lists
    hero_names.append(hero_name)
    hero_strengths.append(hero_strength)
    hero_attack_powers.append(hero_attack_power)
    hero_power_locations.append(hero_location)
    hero_home_extra_damages.append(hero_home_extra_damage)
    hero_main_images.append(hero_main_image)
    hero_location_images.append(hero_location_image)


num_heroes = len(hero_names)
random_hero_number = random.randint(0,num_heroes-1)

hero_pic = hero_main_images [random_hero_number]
hero_location_image = hero_location_images [random_hero_number]
hero_name = hero_names [ random_hero_number ]
hero_location = hero_power_locations [ random_hero_number ]



# Initialize Pygame
pygame.init()

# Set up the display
window_width, window_height = 1200, 600  # Adjusted for two images
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(f'You fight {hero_name} in the {hero_location}!')

# Load the images using hard paths
superhero_image_path = os.path.join('D:\OneDrive\Albright\CSC141\super_hero_game\images', hero_pic)  # Replace with your superhero image filename
location_image_path = os.path.join('D:\OneDrive\Albright\CSC141\super_hero_game\images', hero_location_image)    # Replace with the other image filename

superhero_image = pygame.image.load(superhero_image_path)
location_image = pygame.image.load(location_image_path)

# Scale images to fit side by side (optional)
superhero_image = pygame.transform.scale(superhero_image, (window_width // 2, window_height))
location_image = pygame.transform.scale(location_image, (window_width // 2, window_height))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    window.fill((0, 0, 0))  # Black background

    # Display the two images side by side
    window.blit(superhero_image, (0, 0))               # Position the first image on the left
    window.blit(location_image, (window_width // 2, 0))   # Position the second image on the right

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
