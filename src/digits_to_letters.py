"""
Use case to convert any positive number (as integer) to letters

12 : douze
21 : vingt-et-un
"""

from src.translator_rules.translate_rules_fr import ICommand, UnitsCommand, TensCommand


def digits_to_letters_fr(number: int) -> str:
    if number < 0:
        raise ValueError("Unable to process negative number")
    if number == 0:
        return "zéro"

    fr_commands: list[ICommand] = [UnitsCommand(), TensCommand()]

    text_numbers = []
    while number > 0:
        text_number, number = _loop_on_commands(fr_commands, number)
        if text_number:
            text_numbers.append(text_number)
        else:
            raise ValueError(f"Unable to process number {number}. too big ?")
    return "-".join(text_numbers)


def _loop_on_commands(commands, number) -> tuple[str, int]:
    for command in commands:
        if command.can_execute(number):
            return command.execute(number)
    return "", number
