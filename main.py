import random


# Develop a simple Python program that
# allows the user to guess a secret number.
# The program should provide the user with
# hints to help them get the number right.


class Program:
    def setDifficulty(self):
        print("To start, how about defining the difficulty?")

        attempts = self.setAttempts()
        tips = self.setTips()

        return[attempts, tips]


    def setAttempts(self):
        attempts = 0
        i = 0

        while (attempts <= 0) or (attempts > 5):
            i += 1

            if i >= 3:
                print("Well, it's going to be one try.")
                return 1

            attempts = int(input("How many attempts do you want?\n"))

        return attempts


    def setTips(self):
        tips = '0'
        i = 0

        while tips != 'Y' and tips != 'N':
            i += 1

            if i == 3:
                print("Well, there won't be any attempts")
                tips = 'N'

                return tips

            tips = input("Do you want to receive tips? Y or N\n")
            tips = tips[0].upper()

        return tips


    def initGame(self):
        attempts, tips = self.setDifficulty()

        randomNumber = random.randint(0, 20)
        i = 0

        while i != attempts:
            i += 1
            number = int(input("What is your attempt?\n"))

            if self.checkNumber(randomNumber, number, tips, i) == 0:
                return 0

        print("Looks like you didn't make it, what a shame. The number was {}" .format(randomNumber))
        return 1


    def checkNumber(self, randomNumber, number, tips, i):
        if randomNumber == number:
            print("Congratulations! You got it right on attempt number: {}".format(i))
            return 0

        elif tips == 'Y':
            if number < randomNumber:
                print("Their number is smaller than the random number.")
            else:
                print("Your number is greater than the random number.")

        return 1


if __name__ == "__main__":
    game = Program()

    print("Welcome to the game!")
    game.initGame()