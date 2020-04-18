import random
from person import Person

class Fight:

    def __init__(self, fighter1, fighter2, skill: str) -> None:
        """
        Constructor for the fight class.

        :param fighter1: object
        :param fighter2: object
        :param skill: str
        """
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.skill = skill

    def winner(self) -> object:
        """
        Returns the winner of the fight.

        :return: winner: object
        """
        if len(self.fighter1.getSkills) > 0 and len(self.fighter2.getSkills) > 0:

            if self.fighter1.getSkills[self.skill] > self.fighter2.getSkills[self.skill]:

                if (self.fighter1.getLevel == self.fighter2.getLevel) or (
                        self.fighter1.getLevel > self.fighter2.getLevel):  # Same level competition or the higher level won

                    self.fighter1.gainWealth(10)
                    self.fighter2.loseWealth(10)

                    print(self.fighter1.getName + " won and " + self.fighter2.getName + " lost.")

                    r = random.random()

                    if r > 0.75:
                        self.fighter1.getSkills[self.skill] += 1
                        print(self.fighter1.getName + "'s " + self.fighter1.skill + " skill level has been "
                                                                  "increased by 1 and is now " + str(
                            self.fighter1.getSkills[self.skill]))

                    if r < 0.25:
                        self.fighter2.getSkills[self.skill] += 1
                        print(self.fighter2.getName + "'s " + self.skill + " skill level has been "
                                                                           "increased by 1 and is now " + str(
                            self.fighter2.getSkills[self.skill]))

                elif self.fighter1.getLevel == 2 and self.fighter2.getLevel == 3:  # Fighter wins against Warrior
                    self.fighter1.gainWealth(25)
                    self.fighter2.loseWealth(25)

                    print(self.fighter1.getName + " won and " + self.fighter1.getName + " lost.")

                    self.fighter1.getSkills[self.skill] += 1

                elif self.fighter1.getLevel == 2 and self.fighter2.getLevel == 4:  # Fighter wins against KnightErrant
                    self.fighter1.gainWealth(40)
                    self.fighter2.loseWealth(40)

                    print(self.fighter1.getName + " won and " + self.fighter1.getName + " lost.")

                    self.fighter1.getSkills[self.skill] += 2

                elif self.fighter1.getLevel == 3 and self.fighter2.getLevel == 4:  # Warrior wins against KnightErrant
                    self.fighter1.gainWealth(20)
                    self.fighter2.loseWealth(20)

                    print(self.fighter1.getName + " won and " + self.fighter1.getName + " lost.")

                    self.fighter1.getSkills[self.skill] += 1

                return self.fighter1

            elif self.fighter1.getSkills[self.skill] < self.fighter2.getSkills[self.skill]:
                if (self.fighter1.getLevel == self.fighter2.getLevel) or (
                        self.fighter1.getLevel < self.fighter2.getLevel):  # Same level competition or the higher level won

                    self.fighter2.gainWealth(10)
                    self.fighter1.loseWealth(10)

                    print(self.fighter2.getName + " won and " + self.fighter1.getName + " lost.")


                    r = random.random()

                    if r > 0.75:
                        self.fighter2.getSkills[self.skill] += 1
                        print(self.fighter2.getName + "'s " + self.fighter2.skill + " skill level has been "
                                                                  "increased by 1 and is now " + str(
                            self.fighter2.getSkills[self.skill]))

                    if r < 0.25:
                        self.fighter2.getSkills[self.skill] += 1
                        print(self.fighter2.getName + "'s " + self.skill + " skill level has been "
                                                                           "increased by 1 and is now " + str(
                            self.fighter2.getSkills[self.skill]))

                elif self.fighter1.getLevel == 3 and self.fighter2.getLevel == 2:  # Fighter wins against Warrior
                    self.fighter2.gainWealth(25)
                    self.fighter1.loseWealth(25)

                    print(self.fighter2.getName + " won and " + self.fighter1.getName + " lost.")

                    self.fighter2.getSkills[self.skill] += 1

                elif self.fighter1.getLevel == 4 and self.fighter2.getLevel == 2:  # Fighter wins against KnightErrant
                    self.fighter2.gainWealth(40)
                    self.fighter1.loseWealth(40)

                    print(self.fighter2.getName + " won and " + self.fighter1.getName + " lost.")

                    self.fighter2.getSkills[self.skill] += 2

                elif self.fighter1.getLevel == 4 and self.fighter2.getLevel == 3:  # Warrior wins against KnightErrant
                    self.fighter2.gainWealth(20)
                    self.fighter1.loseWealth(20)

                    print(self.fighter2.getName + " won and " + self.fighter1.getName + " lost.")

                    self.fighter2.getSkills[self.skill] += 1

                return self.fighter2

            else:
                winner = random.choice((self.fighter1, self.fighter2))

                if winner == self.fighter1:
                    loser = self.fighter2

                else:
                    loser = self.fighter1

                print(winner.getName + " won and " + loser.getName + " lost.")

                if (self.fighter1.getLevel == self.fighter2.getLevel) or (loser.getLevel < winner.getLevel):

                    r = random.random()

                    if r > 0.75:
                        winner.getSkills[self.skill] += 1
                        print(winner.getName + "'s " + self.skill + " skill level has been "
                                                                    "increased by 1 and is now " + str(
                            winner.getSkills[self.skill]))

                    if r < 0.25:
                        loser.getSkills[self.skill] += 1
                        print(loser.getName + "'s " + self.skill + " skill level has been "
                                                                   "increased by 1 and is now " + str(
                            loser.getSkills[self.skill]))

                elif winner.getLevel == 2 and loser.getLevel == 3:  # Fighter wins against Warrior
                    winner.gainWealth(25)
                    loser.loseWealth(25)

                    print(winner.getName + " won and " + loser.getName + " lost.")

                    winner.getSkills[self.skill] += 1

                elif self.fighter1.getLevel == 2 and self.fighter2.getLevel == 4:  # Fighter wins against KnightErrant
                    winner.gainWealth(40)
                    loser.loseWealth(40)

                    print(winner.getName + " won and " + loser.getName + " lost.")

                    winner.getSkills[self.skill] += 2

                elif self.fighter1.getLevel == 3 and self.fighter2.getLevel == 4:  # Warrior wins against KnightErrant
                    winner.gainWealth(20)
                    loser.loseWealth(20)

                    print(winner.getName + " won and " + loser.getName + " lost.")

                    winner.getSkills[self.skill] += 1

                return winner