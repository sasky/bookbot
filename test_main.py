
import unittest
from main import *

# info on unit testing, taken from 
# https://www.dataquest.io/blog/unit-tests-python/
#
#

class TestCalculations(unittest.TestCase):

    def test_generate_string_from_txt_file(self):
        # given we have a file path to a txt file
        path = "test_books/test_book.txt"
        desired =  "This is just a little \ntest book.\n"
        # when we run the function
        string = generate_string_from_txt_file(path)
        self.assertEqual(string, desired,"the path matches the book")

    def test_word_count(self):
        # given a string with three words
        self.assertEqual(count_words("one two three"),3,"should be three words in word count")

    def test_count_each_char_in_string(self):
        #given this string
        count_the_chars = "Hello this is a test string for charecter counting"
        desired = {
            'a': 2,
            'c': 3,
            'e': 4,
            'f': 1,
            'g': 2,
            'h': 3,
            'i': 4,
            'l': 2,
            'n': 3,
            'o': 3,
            'r': 4,
            's': 4,
            't': 6,
            'u': 1
        }

        result = count_each_char_in_string(count_the_chars)
        self.assertEqual( result, desired, "charecter counting is working")


    def test_sort_char_count_by_num(self):
        # given we have a dict like so
        to_sort = {
            'a': 2,
            'c': 3,
            'e': 4,
            'n': 5,
            'r': 6,
            's': 7,
            't': 8,
            'u': 9
        }
        # when we sort
        result = sort_char_count_by_num(to_sort)
        # then we want a dict like so
        desired = {
            'u': 9,
            't': 8,
            's': 7,
            'r': 6,
            'n': 5,
            'e': 4,
            'c': 3,
            'a': 2
        }
        self.assertEqual( result, desired, "charecter sorting is working")


if __name__ == '__main__':
    unittest.main()
