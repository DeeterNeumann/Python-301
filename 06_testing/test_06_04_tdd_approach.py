# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest
import os
import tempfile
import open_or_create_file

# open_or_create_file function
# def open_or_create_file(file_path):
#     return open(file_path, 'a+')

# function that opens (creates file if not present) and writes

class TestFileOps(unittest.TestCase):
    def test_open_or_create_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "testfile.txt")

            self.assertFalse(os.path.exists(file_path))

            with open_or_create_file.open_or_create_file(file_path) as f:
                self.assertTrue(os.path.exists(file_path))
                f.write("Success!")

            with open(file_path, "r") as f:
                content = f.read()
                self.assertEqual(content, "Success!")

if __name__ == "__main__":
    unittest.main()