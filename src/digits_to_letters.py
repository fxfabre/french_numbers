"""
Use case to convert any positive number (as integer) to letters

12 : douze
21 : vingt-et-un
"""

from src.translator_rules.translate_rules_fr import (
    ICommand,
    UnitsCommand,
    TensCommand,
    ComplexTensCommand,
    HundredsCommand,
    ThousandsCommand,
)

fr_commands: list[ICommand] = [
    UnitsCommand(),
    TensCommand(),
    ComplexTensCommand(),
    HundredsCommand(),
    ThousandsCommand(),
]


def digits_to_text_fr(number: int) -> str:
    if number < 0:
        raise ValueError("Unable to process negative number")
    if number == 0:
        return "zéro"

    text_number = _digits_to_text_fr(fr_commands, number)

    if _must_add_s_end(number):
        return text_number + "s"
    return text_number


def _digits_to_text_fr(commands: list[ICommand], number: int) -> str:
    """
    Does not handle exceptions (s)
    """
    text_numbers = []
    while number > 0:
        text_number, number = _loop_on_commands(_digits_to_text_fr, commands, number)
        if text_number:
            text_numbers.append(text_number)
        else:
            raise ValueError(f"Unable to process number {number}. too big ?")

    return "-".join(text_numbers)


def _must_add_s_end(number: int) -> bool:
    left, rest = divmod(number, 100)

    # yes if ends with 200, 300 ...
    if (left > 1) and (rest == 0):
        return True

    # yes if ends with 80
    return number % 100 == 80


def _loop_on_commands(
    digit_to_txt_processor, commands: list[ICommand], number: int
) -> tuple[str, int]:
    for command in commands:
        if command.can_execute(number):
            return command.execute(lambda nb: digit_to_txt_processor(commands, nb), number)
    return "", number
