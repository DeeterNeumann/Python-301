# Create at least two child classes for your Opponent()` class:
# - a weak opponent
# - a final boss
# Think about what these two child classes should have in common and where they should differ.
# Implement at least an .attack() method in your Opponent() class, that both of the child classes
# override in different ways.
# Override the __init__() method of at least one of your two child classes so that it adds another attribute to your child 
# class that the parent class doesn't have.

import random
import time

class Hero:
    """Models the Hero of the RPG game"""

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, opponent):
        
        hero_roll = random.randint(1, 12) * self.level
        opp_roll = random.randint(1, 12) * opponent.level

        print(f"\nYou rolled a {hero_roll}...")
        print(f"{opponent.name} rolls a {opp_roll}...")

        if hero_roll >= opp_roll:
            self.level += 10
            print(f"You have defeated {opponent.name} and your level has increased to {self.level}.\n")
            return True
        else: # if hero_roll < opp_roll:
            print(f"You have faught valiantly but {opponent.name} has struck you down.")
            return False

class Opponent:
    """Models the opponents in the RPG game"""
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.retreat = False

    def attack(self, hero):
        
        opp_roll = random.randint(1, 12) * self.level
        hero_roll = random.randint(1, 12) * hero.level

        print(f"\nThe opponent rolled a {opp_roll}...")
        print(f"You rolled a {hero_roll}...")

        if opp_roll >= hero_roll:
            print(f"{self.name} unexpectedly attacked and defeated you.\n")
            return True
        else: # if hero_roll < opp_roll:
            print(f"You overcame the attack by {self.name} and defeated them.")
            return False

class WeakOne(Opponent):
    """Models the weak opponent in the RPG Game"""

    def __init__(self, name, level):
        super().__init__(name, level)
        # if rolled number is less than X, weak opponent will retreat

    def attack(self, hero):
        
        weak_opp_roll = random.randint(1, 12) * self.level
        hero_roll = random.randint(1, 12) * hero.level

        print(f"\nThe opponent rolled a {weak_opp_roll}...")
        print(f"You rolled a {hero_roll}...")
        
        self.retreat = False

        if weak_opp_roll <= 100:
            self.retreat = True
            print(f"{self.name} has retreated back into the forest")
            return False
            
        if weak_opp_roll >= hero_roll:
            print(f"{self.name} unexpectedly attacked and defeated you.\n")
            return True
        else: # if hero_roll < opp_roll:
            print(f"You overcame the attack by {self.name} and defeated them.")
            return False


class FinalBoss(Opponent):
    """Models the Final Boss in the RPG Game"""

    def __init__(self, name, level, hp = 100):
        super().__init__(name, level)
        self.hp = hp

    def attack(self, hero):
        
        weak_opp_roll = random.randint(1, 12) * self.level
        hero_roll = random.randint(1, 12) * hero.level

        print(f"\nThe opponent rolled a {weak_opp_roll}...")
        print(f"You rolled a {hero_roll}...")

        if weak_opp_roll >= hero_roll:
            print(f"{self.name} unexpectedly attacked and defeated you.\n")
            return True
        else: # if hero_roll < opp_roll:
            print(f"You overcame the attack by {self.name} and defeated them.")
            return False


def main():
    welcome()
    game_play()

def welcome():
    print("""
----------------------------------------------
        Welcome to Fierce Forest
        - Battle for the Woods -
----------------------------------------------
""")
    
# Assign level based on order that are randomly selected?

def game_play():
    
    lives = 3
    
    # opponents = [WeakOne("Shadowfang", 10), Opponent("Thornclaw", 20), Opponent("Nightwolf", 30), Opponent("Bloodstag", 40)]

    opponents = [WeakOne("Shadowfang", 10)]
    
    boss = FinalBoss("Ragebear", 100)

    boss_alive = True

    hero = Hero("Ironthorn", 5)

# create dictionary for retrieving info for specific instance

    while len(opponents) > 0 and lives >=0:
        current_opponent: Opponent = random.choice(opponents)
        if current_opponent.name == "Shadowfang":
            print(f"\nOut from the ravene, {current_opponent.name} (at level {current_opponent.level}) emerges, hungry for its next meal.\n")
        elif current_opponent.name == "Thornclaw":
            print(f"\nDown from the trees swoops {current_opponent.name} (at level {current_opponent.level}), nearly taking off your head.\n")
        elif current_opponent.name == "Nightwolf":
            print(f"\nThrough the thick bramble, {current_opponent.name} (at level {current_opponent.level}) slipped out of its den with its fangs showing.")
        elif current_opponent.name == "Bloodstag":
            print(f"\n{current_opponent.name} (at level {current_opponent.level}) charges down the hill, antlers lowered to strike.")
        elif current_opponent.name == "Ragebear":
            print(f"\n{current_opponent.name} (at level {current_opponent.level}) crashes through the trees, snapping branches, headed straight at you.")

        move = input("Do you wish to [a]ttack, [r]unaway, or [l]ookaround?: ")

        while move not in ["a", "r", "l", "q"]:
            print("Please enter one of the following letters [a, r, l] to play.")
            print("To exit the game, enter [q] to quit.")
            move = input("Do you wish to [a]ttack, [r]unaway, or [l]ookaround?")
                
        # if move == "a" and current_opponent.name == "Shadowfang":
        #     if hero.attack(current_opponent):
        #         opponents.remove(current_opponent)
        #         print(f"Beware, {len(opponents) + 1} creatures continue to lurk in the Forest")
        #     else:
        #         print(f"{hero.name} succumbs to the vicious attack by {current_opponent.name}.")
        #         lives -= 1
        #         if lives > -1:
        #             print(f"{hero.name} - you have {lives} lives remaining.")
        #         elif lives == -1:
        #             break
        #         time.sleep(3)
        #         print(f"{hero.name} recovers from the defeat and is ready to further explore the forest.\n")

        if move == "a":
            if hero.attack(current_opponent) or not current_opponent.attack(hero):
                if current_opponent.retreat:
                    print(f"Your opponent, {current_opponent.name} has retreated back into the forest")
                else:
                    opponents.remove(current_opponent)
                print(f"Beware, {len(opponents) + 1} creatures continue to lurk in the Forest")
            else:
                print(f"{hero.name} succumbs to the vicious attack by {current_opponent.name}.")
                lives -= 1
                if lives > -1:
                    print(f"{hero.name} - you have {lives} lives remaining.")
                elif lives == -1:
                    break
                time.sleep(3)
                print(f"{hero.name} recovers from the defeat and is ready to further explore the forest.\n")

        elif move == "r":
            print(f"Like a coward, {hero.name} runs from the threat, but lives to fight another day.\n")

        elif move == "l":
            print(f"{hero.name} takes a moment to gaze off into the distance, ignoring the threat that {current_opponent.name} poses.\n")
        
        elif move == "q":
            print(f"{hero.name} exits the Fierce Forest and proves they are no hero at all.")
            break
        
    while boss_alive and len(opponents) == 0:
        if lives > -1: 
            current_opponent = boss
            print(f"\nDun Dun Duuuuunnn\n{current_opponent.name} (at level {current_opponent.level}) crashes through the trees, snapping branches, headed straight at you.")

            move = input("Do you wish to [a]ttack, [r]unaway, or [l]ookaround?: ")

            while move not in ["a", "r", "l", "q"]:
                print("Please enter one of the following letters [a, r, l] to play.")
                print("To exit the game, enter [q] to quit.")
                
            if move == "a":
                if hero.attack(current_opponent):
                    boss_alive = False
                    print(f"You have defeated the final boss, {current_opponent.name}. \n{hero.name}, you have proved to be a fearless fighter and defeated all the threats in the Fierce Forest.\n Congrats! The Woods are yours!!!...for now")
                else:
                    print(f"{hero.name} succumbs to the vicious attack by {current_opponent.name}.")
                    lives -= 1
                    if lives > -1:
                        print(f"{hero.name} - you have {lives} lives remaining.")
                    elif lives == -1:
                        print(f"\n{hero.name}, you fought with all you had, but Fierce Forest proved to be too much. The Woods remain under control of the creatures that reside within.\n")
                        break
                    time.sleep(3)
                    print(f"{hero.name} recovers from the defeat and is ready to further explore the forest.\n")

            elif move == "r":
                print(f"Like a coward, {hero.name} runs from the threat, but lives to fight another day.\n")

            elif move == "l":
                print(f"{hero.name} takes a moment to gaze off into the distance, ignoring the threat that {current_opponent.name} poses.\n")
        
            elif move == "q":
                print(f"{hero.name} exits the Fierce Forest and proves they are no hero at all.")
                break

    if len(opponents) > 0 and lives == -1 and boss_alive:
        print(f"\n{hero.name}, you fought with all you had, but Fierce Forest proved to be too much. The Woods remain under control of the creatures that reside within.\n")

    # if len(opponents) == 0 and lives > -1 and not boss_alive:
    #     print(f"\n{hero.name}, you have proved to be a fearless fighter and defeated all the threats in the Fierce Forest. The Woods are yours....for now.")


if __name__ == "__main__":
    main()

