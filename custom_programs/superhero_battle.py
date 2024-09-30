# Using lists to battle Superheroes
# Page numbers are from the crash course python book
import random
import os
# Every Superhero must have a power ranking of how much damage they can do
os.system('cls')
superheroes = {'Batman': 7, 'Spiderman': 9, 'Hulk': 9, 'Aquaman': 1, 'Ironman': 10}

number_of_superheroes = len(superheroes) #page 44
#print (number_of_superheroes)
# Dictionaries have key/value pairs. P.92
# get a list of the key values, which are the names of the heroes. p.101 (keys)

superhero_names = list(superheroes.keys()) # page 101

print(superhero_names)
superhero_power_levels = list(superheroes.values()) # page 104
print (superhero_power_levels)
your_power_level = 12
your_max_damage = 7
print ('The heroes in the arena are:')
for hero in superhero_names:
    print (hero)
print ('\n')

# Get a random hero to fight from the list using len command
random_number = random.randint(0, number_of_superheroes - 1) 
superhero = superhero_names[random_number]
hero_power = superhero_power_levels[random_number]
print (f'You find yourself in the arena with {superhero}, who has a power level of {hero_power}!')

#print (superhero_names)
choice =''

while True:
    if choice == 'e': # page 72
        print (f"You have left the arena with your life spared, with {superhero} mocking you.")
        break
    choice = input("Do you (e)scape, or (f)ight?: ")
    
    if (choice == 'f'): # page 72

        # We strike hero first
        damage_to_hero = random.randint(0, your_max_damage)
        if damage_to_hero == 0:
            print (f'You barely miss striking {superhero}!')
        else:
            print (f'You stike {superhero}, delivering {damage_to_hero} points of damage.')
        hero_power = hero_power - damage_to_hero

        if hero_power <= 0:
            print (f'You killed {superhero}!')
            break
        

        # Hero fights you
        damage_to_you = random.randint(0, your_max_damage)
        
        if damage_to_you == 0:
            print (f'{superhero} barely misses you!')
        else:
            print (f'{superhero} strikes you, delivering {damage_to_you} points of damage.')
        your_power_level = your_power_level - damage_to_you
        if your_power_level <= 0:
            print (f'You have died.')
            break
        
print ("Hope you had fun playing.")

    

