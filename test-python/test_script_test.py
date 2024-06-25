import unittest
from test_script import add, subtract
from xmlrunner import XMLTestRunner
import os

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 1), -1)

if __name__ == "__main__":
    # Create the test-reports directory if it doesn't exist
    reports_dir = os.path.join(os.getenv('WORKSPACE', '.'), 'test-reports')
    os.makedirs(reports_dir, exist_ok=True)
    
    # Define the output file for the test results
    output_file = os.path.join(reports_dir, 'test_script_test_results.xml')
    
    # Run the tests and write the results to the output file
    with open(output_file, 'wb') as output:
        unittest.main(testRunner=XMLTestRunner(output=output))
