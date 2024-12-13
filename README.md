# Number to french converter
Take a number as input and print this number in full letters in french (fr-fr).
- 41 : quarante-et-un
- 1736 : mille-sept-cent-trente-six

Limitations :
- It can hanlde only positive numbers, below 1 trillion 


## Basic usage :
Call `main.py` with a digit : `python main.py 36` will diplay `36 : trente-six`


## Dev dependencies & tests
- To install dev dependencies, install dependencies from `requirements-dev.txt`.
- To run tests : `pytest tests`


## Project structure
- There is some documentation in each file to explain the role of it
- The conversion digit -> text is based on rules to apply.
- The rules are contained in src/translator_rules/translator_rules_fr
