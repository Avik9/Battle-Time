class Person:
    def __init__(self, name: str, age: int = 0, wealth: int = 0) -> None:
        """
        :param name: str
        :param age: int
        :param wealth: int
        """
        self.name = name
        self.age = age
        self.wealth = wealth
        self.adult = age > 18
        self.level = 1

    @property
    def getName(self) -> str:
        """
        Returns the name of the person.

        :return: name: str
        """
        return self.name

    @property
    def getAge(self) -> int:
        """
        Returns the age of the person.

        :return: age: int
        """
        return self.age

    @property
    def getWealth(self) -> str:
        """
        Returns the wealth of the person.

        :return: wealth: int
        """
        return self.wealth

    def gainWealth(self, w) -> None:
        """
        Adds the passed in wealth.

        :param w: wealth: int
        :return: None
        """
        self.wealth += w

    def loseWealth(self, w) -> None:
        """
        Subtracts the amount of wealth passed in.

        :param w: wealth
        :return: None
        """
        self.wealth = max(0, self.wealth - w)

    @property
    def isAdult(self) -> bool:
        """
        Returns if the person is the adult.

        :return: adult: bool
        """
        return self.adult

    @property
    def getLevel(self) -> int:
        """
        Returns the level of the person.

        :return: level: int
        """
        return self.level

    def challenge(self, person2: object, skill : str) -> None:
        """
        Says that the person cannot be a fighter.

        :param person2: object
        :param skill: str
        :return: None
        """
        print(self.name + " is not a fighter.")

    def isEqual(self, p) -> bool:
        """
        Checks if two people are equal.

        :param p: object
        :return: isEqual: bool
        """
        if self.isAdult == p.isAdult and self.age == p.age and self.wealth == p.wealth and self.name == p.name:
            return True
        else:
            return False

    def __str__(self) -> str:
        """
        Returns the state of the person.

        :return: str
        """
        return self.getName + " is " + str(self.getAge) + " years old. His wealth is " + str(self.getWealth) + "."

    @isAdult.setter
    def isAdult(self, value):
        self._isAdult = value
