"""
Contain all rules to apply, to convert a digit to text
"""

import math
from abc import ABC


class ICommand(ABC):
    """
    Base Interface for all commands

    Each command can apply 1 rule to convert digit to text
    """

    def can_execute(self, number: int) -> bool:
        """
        Does this command can process the given number ?
        :return: true / false
        """
        raise NotImplementedError()

    def execute(self, digit_to_txt_processor, number: int) -> tuple[str, int]:
        """
        :param number: number to translate to text
        :return:
            - text corresponding to the part of the number translated
            - number : the rest of the number to process

        Example if the current command ca process hundreds :
        - input : 121
        - output : ("cent', 21)
        """

        raise NotImplementedError()


class UnitsCommand(ICommand):
    """
    Process number from 0 to 16 + exceptions (71)
    """

    numbers_mapping = {
        0: "zéro",
        1: "un",
        2: "deux",
        3: "trois",
        4: "quatre",
        5: "cinq",
        6: "six",
        7: "sept",
        8: "huit",
        9: "neuf",
        10: "dix",
        11: "onze",
        12: "douze",
        13: "treize",
        14: "quatorze",
        15: "quinze",
        16: "seize",
        71: "soixante-et-onze",
    }

    def can_execute(self, number: int) -> bool:
        return number in self.numbers_mapping

    def execute(self, digit_to_txt_processor, number: int) -> tuple[str, int]:
        return self.numbers_mapping[number], 0


class TensCommand(ICommand):
    """
    Process 17 to 59
    """

    numbers_mapping = {10: "dix", 20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante"}

    def can_execute(self, number: int) -> bool:
        return (number >= 17) and (number <= 59)

    def execute(self, digit_to_txt_processor, number: int) -> tuple[str, int]:
        quotient, remainder = divmod(number, 10)
        base = self.numbers_mapping[quotient * 10]
        if remainder == 1:  # Gestion des "et-un"
            return f"{base}-et-un", 0
        return base, remainder


class ComplexTensCommand(ICommand):
    """
    Process numbers between 60 and 99
    Except numbers processed in UnitsCommand, as exceptions (71)
    """

    numbers_mapping = {60: "soixante", 80: "quatre-vingt"}

    def can_execute(self, number: int) -> bool:
        """
        Not exactly true, but by design, exceptions (71) are processed before
        """
        return (number >= 60) and (number <= 99)

    def execute(self, digit_to_txt_processor, number: int) -> tuple[str, int]:
        if 60 <= number < 80:
            base = 60
        elif 80 <= number < 100:
            base = 80
        else:
            cmd_name = self.__class__.__name__
            raise ValueError(f"Unable to prcess {number} in this command {cmd_name}")

        return self.numbers_mapping[base], number - base


class HundredsCommand(ICommand):
    """
    Process hundreds
    """

    def __init__(self):
        self.units_command = UnitsCommand()

    def can_execute(self, number: int) -> bool:
        return (number >= 100) and (number <= 999)

    def execute(self, digit_to_txt_processor, number: int) -> tuple[str, int]:
        quotient, remainder = divmod(number, 100)
        cents_txt = digit_to_txt_processor(quotient)
        if quotient == 1:
            return "cent", number - 100
        return f"{cents_txt}-cent", number % 100


class ThousandsCommand(ICommand):
    """
    Process number > 1000
    """

    numbers_mapping = {1000: "mille", 1_000_000: "million", 1_000_000_000: "milliard"}

    def can_execute(self, number: int) -> bool:
        return (number >= 1000) and (number < 1000 * max(self.numbers_mapping))

    def execute(self, digit_to_txt_processor, number: int) -> tuple[str, int]:
        # Find the biggest unit to process : mille, millions, milliard ...
        current_unit_log = int(math.log(number, 1000))
        current_unit = 1000**current_unit_log
        current_unit_name = self.numbers_mapping[current_unit]  # million, milliard

        # Split 12_123_123 into (12, 123_123)
        left, rest = divmod(number, current_unit)

        if left == 0:
            return "", rest
        if (left > 1) and (current_unit_name != "mille"):
            current_unit_name = current_unit_name + "s"

        if left == 1:
            text = current_unit_name  # million, milliard
        else:
            text = digit_to_txt_processor(left) + f"-{current_unit_name}"
        return text, rest
