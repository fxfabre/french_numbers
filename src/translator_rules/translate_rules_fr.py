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

    def execute(self, number: int) -> tuple[str, int]:
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
    Process number from 0 to 16
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
    }

    def can_execute(self, number: int) -> bool:
        return number in self.numbers_mapping

    def execute(self, number: int) -> tuple[str, int]:
        return self.numbers_mapping[number], 0


class TensCommand(ICommand):
    """
    Process 17 to 59
    """

    numbers_mapping = {10: "dix", 20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante"}

    def can_execute(self, number: int) -> bool:
        return (number >= 17) and (number <= 59)

    def execute(self, number: int) -> tuple[str, int]:
        quotient, remainder = divmod(number, 10)
        base = self.numbers_mapping[quotient * 10]
        if remainder == 1:  # Gestion des "et-un"
            return f"{base}-et-un", 0
        return base, remainder


# # Commande pour 60 à 99
# class ComplexTensCommand(ICommand):
#     def __init__(self):
#         self.base_60 = "soixante"
#         self.base_80 = "quatre-vingt"
#
#     def execute(self, number: int) -> tuple[str, int]:
#         if 60 <= number < 80:
#             remainder = number - 60
#             if remainder == 0:
#                 return self.base_60
#             return f"{self.base_60}-{UnitsCommand().execute(remainder)}"
#         elif 80 <= number < 100:
#             remainder = number - 80
#             if remainder == 0:
#                 return self.base_80
#             return f"{self.base_80}-{UnitsCommand().execute(remainder)}"
#         return ""
#
#
# # Commande pour les centaines
# class HundredsCommand(ICommand):
#     def __init__(self):
#         self.units_command = UnitsCommand()
#
#     def execute(self, number: int) -> tuple[str, int]:
#         quotient, remainder = divmod(number, 100)
#         if quotient == 0:
#             return ""
#         elif quotient == 1:
#             base = "cent"
#         else:
#             base = f"{self.units_command.execute(quotient)}-cent"
#
#         if remainder > 0:
#             tens_command = CombinedTensCommand()
#             return f"{base} {tens_command.execute(remainder)}"
#         return base
#
#
# # Commande combinée pour les dizaines (0-99)
# class CombinedTensCommand(ICommand):
#     def execute(self, number: int) -> tuple[str, int]:
#         if number < 17:
#             return UnitsCommand().execute(number)
#         elif number < 60:
#             return TensCommand().execute(number)
#         elif number < 100:
#             return ComplexTensCommand().execute(number)
#         return ""
#
#
# # Interpréteur principal
# class NumberToWords:
#     def execute(self, number: int) -> str:
#         if number < 0 or number > 999:
#             raise ValueError("Le nombre doit être entre 0 et 999")
#         if number < 100:
#             return CombinedTensCommand().execute(number)
#         return HundredsCommand().execute(number)
