import unittest

from app import count_unique_items


class TestCountUniqueItems(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_unique_items([]), 0)

    def test_duplicates(self):
        self.assertEqual(count_unique_items(["a", "a", "b"]), 2)


if __name__ == "__main__":
    unittest.main()
