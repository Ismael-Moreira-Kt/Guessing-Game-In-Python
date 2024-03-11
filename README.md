# Guessing Game in Python

This is the project of a random number guessing game.

## External Content Used
- [Random](https://docs.python.org/3/library/random.html)
- [PyTest](https://docs.pytest.org/en/7.1.x/contents.html)

## Files
#### main.py
It is the file that contains all the game logic.
It is divided into some functions, namely:
- *setDifficulty:* This is the function that defines the difficulty. It calls the setAttempts and setTips functions and returns the contents of both.
- *setAttempts:* Responsible for defining the number of attempts. The user has 3 attempts to provide a valid number, otherwise the number of attempts will be set to 1.
- *setTips:* Responsible for checking whether the user wants tips or not. If the user fails the process three times, the program will automatically define that there will be no help.
- *initGame:* Responsible for managing the game, he manages the game. It is the one that calls the difficulty checking functions, reads the user input and calls the function that checks the result.
- *checkNumber:* Checks if the user won the game. Otherwise, it checks if the user can get hints, otherwise it returns a simple 1.

<br>

#### run_tests.py
Responsible for running all tests automatically.

<br>

#### test_Attempts.py
setAttempts function tests.

<br>

#### test_CheckNumber.py
cheackNumber function tests.

<br>

#### test_Tips.py
setTips function tests.
