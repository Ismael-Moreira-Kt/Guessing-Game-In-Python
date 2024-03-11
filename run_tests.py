import unittest
import os



if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)