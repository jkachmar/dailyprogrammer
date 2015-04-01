"""Testing for /r/dailyprogramming Challenge #207 [Easy]."""
import unittest
from prob_207_easy import base_pair


class BasePairTestCase(unittest.TestCase):

    """Tests 'prob_207_easy.py'."""

    def test_base_pair(self):
        """Test that base_pair() returns appropriate DNA strand."""
        strand = 'A A T G C C T A T G G C'
        mirror = 'T T A C G G A T A C C G'

        self.assertEqual(base_pair(strand), mirror)

if __name__ == '__main__':
    unittest.main()
