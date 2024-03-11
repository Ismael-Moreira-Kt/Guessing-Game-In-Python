import unittest
from unittest.mock import patch
from main import Program



class TestProgram(unittest.TestCase):

    def test_setAttempts_with_valid_input(self):
        program = Program()
        with patch('builtins.input', return_value='3'):
            self.assertEqual(program.setAttempts(), 3)


    def test_setAttempts_with_invalid_input(self):
        program = Program()
        with patch('builtins.input', side_effect=['6', '0', '1']):
            self.assertEqual(program.setAttempts(), 1)


    def test_setAttempts_with_negative_input(self):
        program = Program()
        with patch('builtins.input', side_effect=['-1', '-2', '-3']):
            self.assertEqual(program.setAttempts(), 1)



if __name__ == '__main__':
    unittest.main()