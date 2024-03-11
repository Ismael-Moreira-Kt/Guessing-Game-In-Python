from unittest.mock import patch
import unittest
from main import Program



class TestProgram(unittest.TestCase):

    def test_correct_number(self):
        program = Program()

        with patch('builtins.input', return_value='10'):
            result = program.checkNumber(randomNumber=10, number=10, tips='N', i=1)
            self.assertEqual(result, 0)


    def test_incorrect_number_with_tips(self):
        program = Program()

        with patch('builtins.input', side_effect=['5', '10']):
            result = program.checkNumber(randomNumber=10, number=5, tips='Y', i=1)
            self.assertEqual(result, 1)


    def test_incorrect_number_without_tips(self):
        program = Program()

        with patch('builtins.input', side_effect=['15', '10']):
            result = program.checkNumber(randomNumber=10, number=15, tips='N', i=1)
            self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()