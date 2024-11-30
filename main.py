# alphabets list.
ALPHABETS : dict = {
    'a' : 1, 'b' : 1, 'c' : 1, 'd' : 1, 'e' : 1, 'f' : 1, 'g' : 1, 'h' : 1, 'i' : 1,
    'j' : 2, 'k' : 2, 'l' : 1, 'm' : 3, 'n' : 1, 'o' : 1, 'p' : 2, 'q' : 5, 'r' : 2,
    's' : 2, 't' : 1, 'u' : 2, 'v' : 3, 'w' : 4, 'x' : 14, 'y' : 10, 'z' : 10
}


# WELCOME SCREEN.
print("=============================================================")
print("---------------------- WELCOME TO WORDLE --------------------")
print("=============================================================")
print("\n\n")


# taking details about a word.
print("-------------------------------------------------------------")
print("- SELECT WORD SIZE FOR GAME ---------------------------------")
total_letters : int = 0
while total_letters < 5 or total_letters > 12:
    total_letters = int(input("- size must be btw 5 & 12 (included) :>> "))
print("-------------------------------------------------------------\n\n")


# what letter the word should start from.
print("-------------------------------------------------------------")
print("- SELECT A CHAR FROM ALPHABETS START WORD -------------------")
starting_letter : str = '1'
while not starting_letter.isalpha():
    starting_letter = input("- char from (a & z) included :>> ")
print("-------------------------------------------------------------\n\n")


# taking player entry
print("-------------------------------------------------------------")
print("- SELECT TOTAL PLAYER IN THE GAME ---------------------------")
total_players : int = 0
while total_players < 2 or total_players > 5:
    total_players = int(input("- between 2 & 5 (included) :>> "))
print("-------------------------------------------------------------\n\n")

