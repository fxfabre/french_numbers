import unittest
from parameterized import parameterized

from src.digits_to_letters import digits_to_letters_fr


class TestNumberInterpreter(unittest.TestCase):

    @parameterized.expand(
        [
            (0, "zéro"),
            (1, "un"),
            (9, "neuf"),
            (10, "dix"),
            (11, "onze"),
            (17, "dix-sept"),
            (19, "dix-neuf"),
            (20, "vingt"),
            (21, "vingt-et-un"),
            (22, "vingt-deux"),
            (30, "trente"),
            (42, "quarante-deux"),
            # (70, "soixante-dix"),
            # (71, "soixante-et-onze"),
            # (74, "soixante-quatorze"),
            # (77, "soixante-dix-sept"),
            # (80, "quatre-vingts"),
            # (81, "quatre-vingt-un"),
            # (90, "quatre-vingt-dix"),
            # (91, "quatre-vingt-onze"),
            # (99, "quatre-vingt-dix-neuf"),
            # (100, "cent"),
            # (130, "cent-trente"),
            # (200, "deux-cents"),
            # (201, "deux-cent-un"),
            # (1110, "mille-cent-dix"),
            # (252, "deux-cent-cinquante-deux"),
            # (200000, "deux-cent-mille"),
            # (180000, "cent-quatre-vingt-mille"),
        ]
    )
    def test_number_to_words(self, input_number, expected_output):
        self.assertEqual(digits_to_letters_fr(input_number), expected_output, str(input_number))

    def test_invalid_input_negative(self):
        with self.assertRaises(ValueError):
            digits_to_letters_fr(-1)

    def test_invalid_input_too_large(self):
        with self.assertRaises(ValueError):
            digits_to_letters_fr(1000)
