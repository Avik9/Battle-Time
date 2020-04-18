from person import Person
from fight import Fight

class Fighter(Person):

    def __init__(self, name: str, age: int = 0, wealth: int = 0, skills: dict = None) -> None:
        """
        Constructor for the Fighter class.

        :type skills: object
        :param name: str
        :param age: int
        :param wealth: int
        """

        Person.__init__(self, name, age, wealth)
        self.__skills = None
        self.challenged = []

        if age < 18:
            print(name + " cannot be a fighter.")
            return

        self.__skills = {"spear": 0,
                         "unarmed_combat": 0,
                         "mace": 0,
                         "broadsword": 0}

        if skills:
            self.__skills = skills
            if self.__skills["spear"] > 10 or self.__skills["spear"] < 0:
                print("The skill level for spear is invalid.")

            if self.__skills["unarmed_combat"] > 10 or self.__skills["unarmed_combat"] < 0:
                print("The skill level for unarmed_combat is invalid.")

            if self.__skills["mace"] > 10 or self.__skills["mace"] < 0:
                print("The skill level for mace is invalid.")

            if self.__skills["broadsword"] > 10 or self.__skills["broadsword"] < 0:
                print("The skill level for broadsword is invalid.")

        self.level = 2


    @property
    def getSkills(self) -> dict:
        """
        Returns the skills of the fighter.

        :return: __skills: dict
        """
        if self.age > 18:
            return self.__skills

        else:
            return {}

    def setSkills(self, newSkills: dict) -> None:
        """
        Sets the skills to these new skills

        :param newSkills: dict
        :return: None
        """

        self.__skills = newSkills

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
                    print(self.getName + " has no wealth to fight.")
                    return None

                if fighter2.getWealth <= 0:
                    print(fighter2.getName + " has no wealth to fight.")
                    return None

                # If the skill they are fighting with does not exist

                if skill not in self.getSkills or skill not in fighter2.getSkills:
                    print(skill + " is not a valid skill for the fighter")
                    return None

                # If the skill they are using is over 0 then they fight.

                duel = Fight(self, fighter2, skill)
                winner = duel.winner()

        else:
            print("A fighter cannot fight themselves!")
            return None

    def withdraw(self, withdrawFighter: str) -> None:
        """
        Withdraws the fighter's name from the list

        :param withdrawFighter: str
        :return: None
        """
        if self.getSkills and withdrawFighter.getSkills:

            pos = -1

            for x in range(0, len(self.challenged)):
                if withdrawFighter == self.challenged[x].getFighter1 or withdrawFighter == self.challenged[x].getFighter1:
                    pos = x
                else:
                    pass

            if x > -1:
                self.challenged.remove(x)

            else:
                print(self.getName + " has not challenged " + withdrawFighter.getName)

        else:
            print(self.getName + " does not have any challenges since it is not a fighter.")

    def __str__(self) -> str:
        """
        Returns the state of the Fighter.

        :return: str
        """
        if self.getSkills:
            return Person.__str__(self) + " " + self.getName + "'s skills are: \n\tSpear: " + str(
                self.getSkills["spear"]) \
                   + "\n\tUnarmed Combat: " + str(self.getSkills["unarmed_combat"]) + "\n\tMace: " + str(
                self.getSkills["mace"]) \
                   + "\n\tBroadsword: " + str(self.getSkills["broadsword"])

        else:
            return Person.__str__(self)
