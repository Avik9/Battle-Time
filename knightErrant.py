import random
from person import Person
from warrior import Warrior


class KnightErrant(Warrior):

    def __init__(self, name: str, age: int = 0, wealth: int = 0, skills: object = None, challengers: object = None, skillsChallenged: list = None, isTravelling: bool = False) -> None:
        """
        Constructor fot creating a KnightErrant

        :param name: str
        :param age: int
        :param wealth: int
        :param skills: dict
        :param challengers: list
        :param isTravelling: bool
        """
        if age < 18:
            print(name + " cannot be a warrior.")
            Person.__init__(self, name, age, wealth)
            return

        Warrior.__init__(self, name, age, wealth, skills, challengers)
        self.__skills = None
        self.isTravelling = isTravelling

        if challengers is None:
            self.challenged = []
            self.skillsChallenged = []

        else:
            self.challenged = challengers
            self.skillsChallenged = skillsChallenged

        self.__skills = {"spear": 0,
                         "unarmed_combat": 0,
                         "mace": 0,
                         "broadsword": 0}

        if skills:
            self.__skills = skills

        self.level = 4

    # Removed getters because super

    def travel(self) -> bool:
        """
        Returns if the KnightErrant is travelling.

        :return: isTravelling: bool
        """
        self.isTravelling = True

    def return_from_travelling(self) -> None:
        """
        Returns the KnightErrant from the travel.

        :return: None
        """
        self.isTravelling = False

        r = random.random()

        if r < 0.5:
            treasureFound = round(r * 100)

            print(self.getName + " has found a treasure of " + str(treasureFound) + " coins.")

            self.gainWealth(treasureFound)

            print(self.getName + "'s new wealth is " + str(self.getWealth) + ".")

        else:
            print(self.getName + " has not found any treasure.")

    def challenge(self, fighter2: object, skill: str) -> None:
        """
        Challenges another fighter.

        :param fighter2: object
        :param skill: str
        :return: None
        """
        if self.isTravelling:
            print("Since " + self.getName + " is travelling, he cannot challenge anyone")

        if isinstance(fighter2, KnightErrant):
            if fighter2.isTravelling:
                self.getChallenge().append(fighter2)
                self.getSkillsChallenge().append(skill)
                print(fighter2.getName + " is travelling. " + self.getName + "'s challenge will be added to " +
                      fighter2.getName + "'s current challenges")

            else:
                # A fighter cannot fight themselves

                if not self.isEqual(fighter2):

                    if not self.getSkills and not isinstance(fighter2, Warrior):
                        print(self.getName + " and " + fighter2.getName +
                              " both are not fighters and hence cannot fight.")

                    elif not self.getSkills:
                        print(self.getName + " is not a fighter.")
                        return

                    elif not isinstance(fighter2, Warrior):
                        print(fighter2.getName + " is not a fighter.")
                        return

                    elif not fighter2.getSkills:
                        print(fighter2.getName + " is not a fighter.")
                        return

                    # If they are both fighters:

                    elif self.getSkills and fighter2.getSkills:

                        # If the wealth of both the fighters is more than 0

                        if self.getWealth <= 0:
                            print(self.getName(self) + " has no wealth to fight.")
                            return None

                        elif fighter2.getWealth <= 0:
                            print(self.getName(fighter2) + " has no wealth to fight.")
                            return None

                        # If the skill they are fighting with does not exist

                        elif skill not in self.getSkills or skill not in fighter2.getSkills:
                            print(skill + " is not a valid skill for the fighter")
                            return None

                        # If the skill they are using is over 0 then the warrior/fighter is added to the list.

                        if fighter2 not in self.getChallenge():
                            self.getChallenge().append(fighter2)
                            self.getSkillsChallenge().append(skill)

                else:
                    print("A fighter cannot fight themselves!")
                    return None

    def __str__(self) -> str:
        """
        Returns the state of the KnightErrant.

        :return: str
        """
        if self.getSkills:
            return Person.__str__(self) + " " + self.getName + "'s skills are: \n\tSpear: " + str(
                self.getSkills["spear"]) \
                   + "\n\tUnarmed Combat: " + str(self.getSkills["unarmed_combat"]) + "\n\tMace: " + str(
                self.getSkills["mace"]) \
                   + "\n\tBroadsword: " + str(self.getSkills["broadsword"]) + "\nKnightErrant is currently travelling: " + str(self.isTravelling)

        else:
            return Warrior.__str__(self)
