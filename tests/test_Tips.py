import unittest
from unittest.mock import patch
from main import Program



class TestProgram(unittest.TestCase):

    def test_setTips_with_valid_input(self):
        program = Program()
        with patch('builtins.input', return_value='Y'):
            self.assertEqual(program.setTips(), 'Y')


    def test_setTips_with_invalid_input(self):
        program = Program()
        with patch('builtins.input', side_effect=['X', 'Y']):
            self.assertEqual(program.setTips(), 'Y')


    def test_setTips_with_too_many_attempts(self):
        program = Program()
        with patch('builtins.input', side_effect=['X', 'W', 'Z', 'N']):
            self.assertEqual(program.setTips(), 'N')



if __name__ == '__main__':
    unittest.main()