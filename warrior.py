import random
from fighter import Fighter
from fight import Fight
from person import Person


class Warrior(Fighter):
    def __init__(self, name: str, age: int = 0, wealth: int = 0, skills: dict = None, challengers: list = None, skillsChallenged: list = None) -> None:
        """
        Constructor for the Warrior.

        :param name: str
        :param age: int
        :param wealth: int
        :param skills: dict
        :param challengers: list
        """
        if age < 18:
            print(name + " cannot be a warrior.")
            Person.__init__(self, name, age, wealth)
            return

        Fighter.__init__(self, name, age, wealth, skills)

        if challengers is None:
            self.challenged = []
            self.skillsChallenged = []
        else:
            self.challenged = challengers
            self.skillsChallenged = skillsChallenged

        self.setSkills({"spear": 0,
                         "unarmed_combat": 0,
                         "mace": 0,
                         "broadsword": 0})

        if skills:
            self.setSkills(skills)

        self.level = 3

    # Removed getters because super

    def getChallenge(self) -> list:
        """
        Gets the list of pending challenges

        :return: list
        """
        return self.challenged

    def getSkillsChallenge(self) -> list:
        """
        Gets the list of skills used in pending challenges

        :return: list
        """
        return self.skillsChallenged

    def challenge(self, fighter2: object, skill: str) -> None:
        """
        Challenges another fighter.

        :param fighter2: object
        :param skill: str
        :return: None
        """

        # A fighter cannot fight themselves

        if not self.isEqual(fighter2):

            if not self.getSkills and not isinstance(fighter2, Fighter):
                print(self.getName + " and " + fighter2.getName + " both are not fighters and hence cannot fight.")

            elif not self.getSkills:
                print(self.getName + " is not a fighter.")
                return

            elif not isinstance(fighter2, Fighter):
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

                # elif skill not in self.getSkills or skill not in fighter2.getSkills:
                #     print(skill + " is not a valid skill for the fighter")
                #     return

                # If the skill they are using is over 0 then the warrior/fighter is added to the list.

                if fighter2 not in self.getChallenge():
                    self.getChallenge().append(fighter2)
                    self.getSkillsChallenge().append(skill)

                    print(fighter2.getName + " has been added to the list.")

        else:
            print("A fighter cannot fight themselves!")
            return None

    def accept_random(self) -> None:
        """
        Fights a random fighter from the pending challenges.

        :return: None
        """
        print(self.getName + "'s challenges: " + str(self.getChallenge()))
        if len(self.getChallenge()) > 0:
            x = (random.random() * len(self.getChallenge()) - 1)
            x = int(round(x))

            toChallenge = self.getChallenge().pop(x)
            print(self.getName + " is challenging " + toChallenge.getName)

            skill = self.getSkillsChallenge().pop(x)

            if self.getAge > 17 and toChallenge.getAge > 17:

                f = Fight(self, toChallenge, skill)
                f.winner()

                self.getChallenge().remove(x)
                self.getSkillsChallenge().remove(x)

                # print(self.getName + "'s challenges: " + str(self.getChallenge()))
            else:
                print(toChallenge.getName + " is not a fighter.")
                self.getChallenge().remove(x)
                self.getSkillsChallenge().remove(x)

        else:
            print("There are no pending challenges.")

    def reject_random(self) -> None:
        """
        Rejects a random challenge from the pending list of challenges.

        :return: None
        """
        if len(self.getChallenge()) > 0:
            print(self.getName + "'s challenges: " + str(self.getChallenge()))
            toReject = int(round(random.random() * len(self.getChallenge()) - 1))

            rejected = self.getChallenge().pop(toReject)

            self.getChallenge().remove(toReject)
            self.getSkillsChallanged().remove(toReject)
            print(self.getName + "'s challenges: " + str(self.getChallenge()))

            print(rejected.getName + " has been removed.")

        else:
            print("There are no pending challenges.")

    def accept_first(self) -> None:
        """
        Fights the first warrior in the list.

        :return: None
        """
        if len(self.getChallenge()) > 0:
            toChallenge = self.getChallenge().pop(0)
            skill = self.getSkillsChallenge().pop(0)

            f = Fight(self, toChallenge, skill)
            f.winner()

            self.getChallenge().remove(0)
            self.getSkillsChallenge().remove(0)

        else:
            print("There are no pending challenges.")

    def decline_first(self) -> None:
        """
        Declines the challenge from the first fighter in the list.

        :return: None
        """
        if len(self.getChallenge()) > 0:
            # print(self.getName + "'s challenges: " + str(self.getChallenge()))
            rejected = self.getChallenge().pop(0)

            print(rejected.getName + " has been rejected.")

            self.getChallenge().remove(0)
            self.getSkillsChallenge().remove(0)
            # print(self.getName + "'s challenges: " + str(self.getChallenge()))

            print(rejected.getName + " has been removed.")

        else:
            print("There are no pending challenges.")
