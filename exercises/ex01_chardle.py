"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730569172"
""""The following code was used to make sure the length of the word inputed was actually five letters. For the second part it was to make sure it was one letter"""
term: str = input("Enter a 5-character word: ")
if len(term) != 5:
    print("Error: Word must contain five characters")
    exit()   
character: str = input("Enter a single character: ")
if len(character) == 1:
    print("Searching for " + str(character) +" in " + term)
else:
     print("Error: Character must be a single character")
     exit()
""" Statements used to count instances of a letter and communicate to user amount of instances """
matching_letters: int = 0
if term[0] == character:
    print(character + " found at index 0")
    matching_letters = matching_letters + 1
if term[1] == character:
    print(character + " found at index 1")
    matching_letters = matching_letters + 1
if term[2] == character:
    print(character + " found at index 2")
    matching_letters = matching_letters + 1
if term[3] == character:
    print(character + " found at index 3")
    matching_letters = matching_letters + 1
if term[4] == character:
    print(character + " found at index 4")
    matching_letters = matching_letters + 1
if matching_letters == 0:
    print("No instances of " + character + " in " + term )
else:
    print(str(matching_letters) + " Instances of " + character + " found in " + term)