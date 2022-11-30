from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def dice_roll(self, number_of_rolls=1):
        self.number_of_rolls = number_of_rolls
        print(f"\nThe dice will be rolled {self.number_of_rolls} times")

        for i in range(1, self.number_of_rolls + 1):
            number = randint(1, self.sides)
            print(f"Number rolled: {number}")


six_sided_die = Die()
six_sided_die.dice_roll(10)

ten_sided_die = Die(10)
ten_sided_die.dice_roll(10)

twenty_sided_die = Die(20)
twenty_sided_die.dice_roll(10)
