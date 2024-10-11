# For class demo on 10/2/24:
# Add your power_level display
# Add the type of enemy power, such as "Cape Stun."
# Display all the heroes in the Arena with self.print_heroes()







# Supehero SmackDown
# Same Superhero program using OOP, which stands for Object Oriented Programming
# This makes the code simpler, easier to read, more flexible, and more powerful.
# This will make YOU powerful. You will enter the realm of professional coders.
# This is page 157 from your Python book

import random
import os
os.system('cls')

class Superhero:
    # Every class starts with a capital letter. In Python, this means it's a class and not a function name
    # As an aside:
    # I realized at the beginning I was confusing people by saying to use Camel Case, which the book does not use
    # Underscores seem to be approaching the end of their lifecycle
    # Internal consistency matters above all
    
    def __init__(self, name, power_level, max_damage):
        self.name = name
        self.power_level = power_level
        self.max_damage = max_damage

    def take_damage(self, damage):
        self.power_level -= damage
        if self.power_level <= 0:
            self.power_level = 0
            print(f'{self.name} has been defeated!')
            return True  # Hero dies
        return False # Hero still alive

    def attack(self):
        return random.randint(0, self.max_damage)

class Arena:
    # Think of a method as a function, except this function is part of a class (OOP)
    # __init__ has two underscores, often called "Magic Methods", which is not a joke.
    # They distinguish the Magic Methods from regular methods. This naming convention avoids confusion.

    def __init__(self):
        self.superheroes = [
            Superhero('Batman', 7, 5),
            Superhero('Spiderman', 9, 5),
            Superhero('Hulk', 11, 8),
            Superhero('Aquaman', 3, 2),
            Superhero('Ironman', 10, 6)
        ]
        # self does not represent your character. It's just a convention of OOP.
        # self is a special keyword to refer to the current instance of the class.
        self.your_power_level = 9
        self.your_max_damage = 7
        self.hero = random.choice(self.superheroes)  # Randomly select a superhero to fight
        self.you_die = False
        self.hero_dies = False

    def print_heroes(self):
        # Not currently used, but I may use it in subsequent code
        print('The enemy heroes in the arena are:')
        for hero in self.superheroes:
            print(hero.name)
        print('\n')

    def you_fight(self):
        damage_to_hero = random.randint(0, self.your_max_damage)
        if damage_to_hero == 0:
            print(f'You barely miss striking {self.hero.name}!')
        else:
            print(f'You strike {self.hero.name}, delivering {damage_to_hero} points of damage.')
        self.hero_dies = self.hero.take_damage(damage_to_hero)

    def hero_fights_you(self):
        damage_to_you = self.hero.attack()
        if damage_to_you == 0:
            print(f'{self.hero.name} barely misses you!')
        else:
            print(f'{self.hero.name} strikes you, delivering {damage_to_you} points of damage.')
        self.your_power_level -= damage_to_you
        if self.your_power_level <= 0:
            print(f'You give up the fight and beg for mercy from {self.hero.name}.')
            self.you_die = True

    def start_battle(self):
        
        print(f'You find yourself in the arena with {self.hero.name}, who has a power level of {self.hero.power_level}!')
        while True:
            choice = input("Do you (e)scape, or (f)ight?: ").lower()

            if choice == 'e':
                print(f"You have left the arena with your life spared, with {self.hero.name} smirking at you.")
                break

            elif choice == 'f':
                self.you_fight()
                if self.hero_dies:
                    break
                
                self.hero_fights_you()
                if self.you_die:
                    break
            else:
                print("Invalid choice. Please enter 'e' to escape or 'f' to fight.")

        print("Hope you had fun playing.")

# Main 
# Instantiate the Arena and start the battle
# Instantiate the Arean means creating an instance of the Arena class.
# Classes are like Blueprints, and an instance (or object) is a specific element of that Blueprint(Class)
arena = Arena()
arena.start_battle()
