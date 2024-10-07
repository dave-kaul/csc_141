# Open the file and read the content
with open('heroes.txt', 'r') as file:
    lines = file.readlines()

# Iterate over each line and print the hero details
for line in lines:
    # Split the line into hero's name, strength, and attack power
    hero_name, hero_strength, hero_attack_power = line.split()
    
    # Print the hero's details using f-string
    print(f'{hero_name} has {hero_strength} Strength and {hero_attack_power} Attack Power.')
