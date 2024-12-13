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


## Prompts chatGPT utilisés :

Tu es un expert Python spécialisé dans la rédaction de code maintenable et performant. Chaque solution doit respecter les principes SOLID, et privilégier une architecture modulaire adaptée aux projets à long terme. Utilise des design patterns pertinents (Factory, Dependency Injection) pour améliorer la lisibilité et l’évolutivité. Préfère des solutions Pythonic, tire parti des bibliothèques qui te semblent utiles et veille à optimiser l’utilisation des ressources (CPU, mémoire).
Tu dois écrire une fonction qui prend en entrée un nombre et doit l'écrire en français en toutes lettres.
Exemples : 
12 : douze
71 : soixante-et-onze
252 : deux-cent-cinquante-deux

Quelles sont les architectures possible ?

<hr />

Est ce que tu peux me générer un fichier de test, avec unittest et parameterized, pour tester ce code ?

<hr />

Est ce que tu peux me donner le code avec le pattern command, et :
- Une command pour les nombre de 0 à 16
- Une command pour les dizaines, de 20 à 50
- Une command pour gérer les nombre de 60 à 79, qui utilisera la command pour les nombres de 1 à 16. Elle doit aussi pouvoir gérer les nombre de 80 à 99
- Une command pour la gestion des "et-un" comme "trente-et-un"
- Une command pour la gestion des centaines
