import unittest
from main import main
from utils import utility_function

class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def test_main(self):
        self.assertEqual(main(), "Expected Result")

    def test_utility_function(self):
        self.assertEqual(utility_function("input"), "Expected Result")

if __name__ == '__main__':
    unittest.main()