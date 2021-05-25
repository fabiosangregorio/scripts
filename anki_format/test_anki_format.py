import unittest
from anki_format import anki_format


class TestAnkiFormat(unittest.TestCase):
    def test_format(self):
        input = "input $x$ tutti i possibili $2^{56}$ valori di $z$ che posso produrre"
        expected = "input [$]x[/$] tutti i possibili [$]2^{56}[/$] valori di [$]z[/$] che posso produrre"
        self.assertEqual(anki_format(input), expected)
