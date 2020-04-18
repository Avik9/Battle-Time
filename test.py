from fight import Fight
from person import Person
from fighter import Fighter
from warrior import Warrior
from knightErrant import KnightErrant

class Test:
    # When you create a fighter, make a dictionary outside and send in the dictionary as an argument

    if __name__ == "__main__":

        print("Making a person: ")

        alex = Person("Alex")

        print(str(alex) + "\n\n")


        print("Making a fighter: ")

        tom = Fighter("Tom", 20, 0, {"spear": 8, "unarmed_combat": 5, "mace": 5, "broadsword": 5})

        print(str(tom) + "\n\n")


        print("Making a warrior: ")

        henry = Warrior("Henry", 20, 100, {"spear": 6, "unarmed_combat": 7, "mace": 8, "broadsword": 9}, None, None)

        print(str(henry) + "\n\n")


        print("Making a Knight Errant that is travelling: ")

        sam = KnightErrant("Sam", 30, 200, {"spear": 6, "unarmed_combat": 7, "mace": 8, "broadsword": 9}, None, None, True)

        print(str(sam) + "\n\n")


        print("Making a Knight Errant that is not travelling: ")

        kim = KnightErrant("Kim", 30, 200, {"spear": 6, "unarmed_combat": 7, "mace": 8, "broadsword": 9}, None, None)

        print(str(kim) + "\n\n")


        print("Checking if Sam and Kim are equal: " + str(sam.isEqual(kim)))


        print("Adding wealth to Tom: ")

        tom.gainWealth(30)

        print(str(tom) + "\n\n")


        print("Deducting wealth to Tom: ")

        tom.loseWealth(30)

        print(str(tom) + "\n\n")


        print("Accepting a random fight when there are no pending fights for a Warrior: ")
        henry.accept_random()

        print("\n\n")

        print("Accepting a random fight when there are no pending fights for a KnightErrant: ")
        kim.accept_random()

        print("\n\n")


        print("A warrior is fighting a knight errant: ")

        henry.challenge(kim, "Sword")

        print("\n\n")


        print("A knightErrant fights a knightErrant that is travelling: ")

        max = KnightErrant("Max", 30, 200, {"spear": 5, "unarmed_combat": 8, "mace": 9, "broadsword": 10}, None, None,
                           False)

        max.challenge(sam, "spear")

        print("\n\n")


        print("Sam returns from travelling: ")
        sam.return_from_travelling()

        print("\n\n")


        print("Avik, a fighter is fighting Ajay, a fighter: ")


        ajay = Fighter("Ajay", 19, 200, {"spear" : 5, "unarmed_combat" : 0, "mace" : 8, "broadsword": 2})

        avik = Fighter("Avik", 25, 1000, {"spear" : 6, "unarmed_combat" : 1, "mace" : 9, "broadsword": 3})

        avik.challenge(ajay, "spear")