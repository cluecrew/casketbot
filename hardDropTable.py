# hardDropTable.py
import os
import random
def hardDrop():
    rollHard = random.randint(1,96)
    print("Rolled a "+str(rollHard)+"!")
    if  1 <= rollHard <= 15:
        reward = "A Piece from the God Trimmed Armor Table"
    elif  16 <= rollHard <= 25:
        reward = "A Piece from the Trimmed Rune Armor Table"
    elif  26 <= rollHard <= 50:
        reward = "A Piece from the Heraldic Rune Armor Table"
    elif  51 <= rollHard <= 54:
        reward = "A Piece from the Trimmed Dragonhide Table"
    elif  55 <= rollHard <= 57:
        reward = "A Piece from the Enchanted Outfit Table"
    elif  58 <= rollHard <= 69:
        reward = "A Piece from the Vestment Table"
    elif  70 <= rollHard <= 81:
        reward = "A Piece from the Blessed Dragonhide Table"
    elif  82 <= rollHard <= 84:
        reward = "A Hat from the Cavalier Hat Table"
    elif rollHard == 85:
        reward = "A Pirate Hat"
    elif rollHard == 86:
        reward = "A Robinhood Hat"
    elif rollHard == 87:
        reward = "An Amulet of Fury (t)"
    elif rollHard == 88:
        reward = "An Amulet of Glory (t)"
    elif rollHard == 89:
        reward = "A Top Hat"
    elif rollHard == 90:
        reward = "A Rune Cane"
    elif rollHard == 91:
        reward = "Any Mask from the Animal Mask Table"
    elif rollHard == 92:
        reward = "Any Mask from the Dragon Mask Table"
    elif rollHard == 93:
        reward = "A Chance to pull from the Sack of Effigies Table"
    elif rollHard == 94:
        reward = "A Chance to pull from the Backstab Table"
    elif rollHard == 95:
        reward = "A Chance to pull from the Dye Table"
    elif rollHard == 96:
        reward = "A reward from the Mega-Rare Table"
    print("Drop Complete! - Hard Drop Table")
    return reward