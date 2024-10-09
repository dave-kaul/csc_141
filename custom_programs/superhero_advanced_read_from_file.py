from pathlib import Path

path = Path('heroes.txt')  # Path to your file

# Lists to store hero data
hero_names = []
hero_strengths = []
hero_attack_powers = []
hero_power_locations = []
hero_home_extra_damages = []

# Read the content of the file and split it into lines
lines = path.read_text().splitlines()

# Ignore the first line since it just desscribes the data
lines = lines[1:]

# Loop through each line and store the hero details in lists
for line in lines:
    # Split line into respective hero details
    hero_name, hero_strength, hero_attack_power, hero_power_location, hero_home_extra_damage = line.split()
    
    # Convert strength and attack power to integers, extra damage to a float number since an int number is not specific enough
    hero_strength = int(hero_strength)
    hero_attack_power = int(hero_attack_power)
    hero_home_extra_damage = float(hero_home_extra_damage)
    
    # Append the data to corresponding lists
    hero_names.append(hero_name)
    hero_strengths.append(hero_strength)
    hero_attack_powers.append(hero_attack_power)
    hero_power_locations.append(hero_power_location)
    hero_home_extra_damages.append(hero_home_extra_damage)

# Now all variables are in separate lists, and you can print them out
print("Hero Names:", hero_names)
print("Hero Strengths:", hero_strengths)
print("Hero Attack Powers:", hero_attack_powers)
print("Hero Power Locations:", hero_power_locations)
print("Hero Home Extra Damages:", hero_home_extra_damages)
