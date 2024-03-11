import random


# Develop a simple Python program that
# allows the user to guess a secret number.
# The program should provide the user with
# hints to help them get the number right.


class Program:
    def setDifficulty(self):
        print("To start, how about defining the difficulty?")

        attempts = int(input("How many attempts do you want?\n"))

        tips = input("Do you want to receive tips? Y or N\n")
        tips = tips[0].upper()

        self.initGame(attempts, tips)


    def initGame(self, attempts, tips):
        randomNumber = random.randint(0, 20)
        i = 0

        while i != attempts:
            i += 1
            number = int(input("What is your attempt?\n"))

            if randomNumber == number:
                print("Congratulations! You got it right on attempt number: {}" .format(i))
                break
            elif tips == 'Y':
                if number < randomNumber:
                    print("Their number is smaller than the random number.")
                else:
                    print("Your number is greater than the random number.")



if __name__ == "__main__":
    game = Program()

    print("Welcome to the game!")
    game.setDifficulty()