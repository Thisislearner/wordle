import random
from prettytable import PrettyTable

# alphabets list.
ALPHABETS : dict = {
    'a' : 1, 'b' : 1, 'c' : 1, 'd' : 1, 'e' : 1, 'f' : 1, 'g' : 1, 'h' : 1, 'i' : 1,
    'j' : 2, 'k' : 2, 'l' : 1, 'm' : 3, 'n' : 1, 'o' : 1, 'p' : 2, 'q' : 5, 'r' : 2,
    's' : 2, 't' : 1, 'u' : 2, 'v' : 3, 'w' : 4, 'x' : 14, 'y' : 10, 'z' : 10
}


# keep all details regarding players.
PLAYERS : dict = {}
PLAYERS_ID : list = [] # hold ids' of player.
PLAYERS_SCORES : list = [] # stores scores of players.


def valid_entry(player_entry : str, first_chr : str, wrd_len : int) -> bool :
    """check if player entry is valid or not"""
    if not player_entry.isalpha() or player_entry[0] != first_chr or len(player_entry) != wrd_len:
        return False
    return True


def score_calc(wrd_entry : str) -> int:
    """calculates total score"""
    total_score : int = 0 # var hold total score.
    for c in wrd_entry:
        total_score += ALPHABETS[c]
    return total_score


# WELCOME SCREEN.
print("=============================================================")
print("---------------------- WELCOME TO WORDLE --------------------")
print("=============================================================")
print("\n\n")


# taking details about a word.
print("-------------------------------------------------------------")
print("- SELECT WORD SIZE FOR GAME ---------------------------------")
word_size : int = 0
while word_size < 5 or word_size > 12:
    word_size = int(input("- size must be btw 5 & 12 (included) :>> "))
print("-------------------------------------------------------------\n\n")


# what letter the word should start from.
print("-------------------------------------------------------------")
print("- SELECT A CHAR FROM ALPHABETS START WORD -------------------")
starting_letter : str = '1'
while not starting_letter.isalpha():
    starting_letter = input("- char from (a & z) included :>> ").lower()
print("-------------------------------------------------------------\n\n")


# taking player entry
print("-------------------------------------------------------------")
print("- SELECT TOTAL PLAYER IN THE GAME ---------------------------")
total_players : int = 0
while total_players < 2 or total_players > 5:
    total_players = int(input("- between 2 & 5 (included) :>> "))
print("-------------------------------------------------------------\n\n")


# taking player details
for i in range(total_players):
    current_id : int = 0 # current default id.
    # generating unique random id.
    while current_id < 100 or any(x == current_id for x in PLAYERS_ID):
        current_id = random.randint(100, 999)
    # adding id to PLAYERS_ID LIST.
    PLAYERS_ID.append(current_id)
    PLAYERS[current_id] = {} # player detail dict.
    # defining player data.
    PLAYERS[current_id]["name"] = input(f"Player{i + 1} name is :>> ")
    PLAYERS[current_id]["word"] = "" # dict item to hold player entry
    PLAYERS[current_id]["winner"] = False # no one winner default.
    PLAYERS[current_id]["points"] = 0


# taking input from player.
for i_d in PLAYERS.keys():
    print("\n")
    print("========================================================================")
    print(f"-- {PLAYERS[i_d]['name']} ID {i_d} -------------------------------")
    print(f"-- Enter a {word_size} letter word starting with '{starting_letter.upper()}'")
    # giving three attempts
    entered_word : str = ""
    for i in range(3):
        entered_word = input(f"Attempt ({i + 1} of 3) :>> ")
        # checking for valid entry
        if valid_entry(entered_word, starting_letter, word_size):
            break
    #storing player entry
    PLAYERS[i_d]["word"] = entered_word
    # giving scores to player based on entry.
    current_plr_scr : int = -1
    if valid_entry(entered_word, starting_letter, word_size):
           current_plr_scr = score_calc(entered_word)
    PLAYERS[i_d]["points"] = current_plr_scr
    # storing scores
    PLAYERS_SCORES.append(current_plr_scr)

# printing players entry and point
display_table = PrettyTable(["ID", "NAME", "WORD ENTERED", "POINTS", "WINNER/LOOSER"])

# highest score calculation
highest_score : int = 0
for i in PLAYERS_ID:
    if PLAYERS[i]["points"] > highest_score:
        highest_score = PLAYERS[i]["points"]

# loop to print
for i_d in PLAYERS_ID:
    # checking for winner.
    winner : str = "------"
    if PLAYERS[i_d]["points"] == highest_score:
        PLAYERS[i_d]["winner"] = True
        winner = "WINNER"
    display_table.add_row([i_d, PLAYERS[i_d]["name"], PLAYERS[i_d]["word"], PLAYERS[i_d]["points"], winner])

# new loop to display rank
for i in range(len(PLAYERS_SCORES)):
    for j in range(0, (len(PLAYERS_SCORES) - 1) - i):
        if PLAYERS_SCORES[j] < PLAYERS_SCORES[j + 1]:
            current_item = PLAYERS_SCORES[j]
            PLAYERS_SCORES[j] = PLAYERS_SCORES[j + 1]
            PLAYERS_SCORES[j + 1] = current_item

# printing general display
print(display_table)

# rank display
id_displayed : list = []  # holds ids already displayed.
rank : int = 1
rank_display = PrettyTable(["RANK", "ID", "NAME", "POINTS"])

# loop to print rank
for i in PLAYERS_SCORES:
    plr_id : int  = 0 # gets current id match
    for d in PLAYERS:
        if PLAYERS[d]["points"] == i:  # when points match found
            plr_id = d
            rank_display.add_row([rank, d, PLAYERS[d]['name'], PLAYERS[d]['points']])
            break
    PLAYERS.pop(plr_id)
    rank += 1

print(rank_display)