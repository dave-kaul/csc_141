import random
import os
os.system('cls')  # Clear the screen before playing

# Set variables
superheroes = {'Batman': 7, 'Spiderman': 9, 'Hulk': 11, 'Aquaman': 3, 'Ironman': 10}
hero_max_damage = {'Batman': 5, 'Spiderman': 5, 'Hulk': 8, 'Aquaman': 2, 'Ironman': 6}
# hero_gender = {'Batman': 'male', 'Spiderman': 'male', 'Hulk': 'male', 'Aquaman': 'male', 'Ironman': 'male'}
choice = ''
you_die = False
hero_dies = False
number_of_superheroes = len(superheroes)  # page 44
superhero_power_levels = list(superheroes.values())  # page 104
super_hero_gender = list(superheroes.values()) 
superhero_names = list(superheroes.keys())  # page 101
random_number = random.randint(0, number_of_superheroes - 1)

# Select a random superhero to fight
superhero = superhero_names[random_number]
hero_power = superhero_power_levels[random_number]
hero_damage = hero_max_damage[superhero]
your_power_level = 9
your_max_damage = 7

def print_heroes():
    print('The enemy heroes in the arena are:')
    for hero in superhero_names:
        print(hero)
    print('\n')

def you_fight(hero_power):
    # You strike hero
    damage_to_hero = random.randint(0, your_max_damage)
    if damage_to_hero == 0:
        print(f'You barely miss striking {superhero}!')
    else:
        print(f'You strike {superhero}, delivering {damage_to_hero} points of damage.')
    hero_power = hero_power - damage_to_hero
    if hero_power <= 0:
        print(f'You lay the smackdown on {superhero}!')
        return True, hero_power
    return False, hero_power

def hero_fights_you(your_power_level):
    # Hero fights you
    damage_to_you = random.randint(0, hero_damage)
    if damage_to_you == 0:
        print(f'{superhero} barely misses you!')
    else:
        print(f'{superhero} strikes you, delivering {damage_to_you} points of damage.')
    your_power_level = your_power_level - damage_to_you
    if your_power_level <= 0:
        print(f'You give up the fight and beg for mercy from {superhero}.')
        return True, your_power_level
    return False, your_power_level


# print_heroes()
print(f'You find yourself in the arena with {superhero}, who has a power level of {hero_power}!')
# Main Game Loop
while True == True:
    if choice == 'e':  # page 72
        print(f"You have left the arena with your life spared, with {superhero} smirking at you.")
        break
    choice = input("Do you (e)scape, or (f)ight?: ")

    if choice == 'f':  # page 72
        # You fight the hero
        hero_dies, hero_power = you_fight(hero_power) # This is called Tuple Unpacking. Python is returing 2 values: hero_dies and hero_power as a tuple
        if hero_dies == True:                         # The comma allows us to unpack or split the tuple into separate variables
            break                                     # hero_dies will be returned as True/False and hero_power will be returned as the updated hero_power

        # Hero fights you
        you_die, your_power_level = hero_fights_you(your_power_level)
        if you_die == True:
            break

# Game end
print("Hope you had fun playing.")
