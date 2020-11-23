import unittest
import grep


class GrepTestCase(unittest.TestCase):
    def test_grep_happy_path_1(self):
        self.assertEqual(grep.execute_grep("llo", ["hello", "helllo", "world", "llllllllo", "llooo", "helo"]),
                         {0: "hello", 1: "helllo", 3: "llllllllo", 4: "llooo"})

    def test_grep_happy_path_2(self):
        self.assertEqual(grep.execute_grep("hello", ["say hello to him", "helllo", "hello world", "in this world",
                                                     "python is the best", "say hello to this hello world"]),
                         {0: "say hello to him", 2: "hello world", 5: "say hello to this hello world"})

    def test_grep_happy_path_3(self):
        self.assertEqual(grep.execute_grep("hello world", ["say hello to him", "helllo", "hello world once again", "in this world",
                                                     "python is the best", "say hello to this hello world"]),
                         {2: "hello world once again", 5: "say hello to this hello world"})

    def test_grep_happy_path_4(self):
        self.assertEqual(grep.execute_grep("hello", ["only good morning here", "have a good day", "nothing here"]),
                         {})

    def test_grep_happy_path_5(self):
        self.assertEqual(grep.execute_grep("x", ["only good morning here", "have a good day", "nothingx here"]),
                         {2: "nothingx here"})

    def test_grep_happy_path_6(self):
        self.assertEqual(grep.execute_grep("", ["only good morning here", "have a good day", "nothing here"]),
                         "Please provide at least 1 character.")


if __name__ == '__main__':
    unittest.main()
