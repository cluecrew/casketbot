# hardDropTable.py
import os
import random
def hardDrop():
    rollHard = random.randint(1,96)
    print("Rolled a "+str(rollHard)+"!")
    if  1 <= rollHard <= 15:
        print("Any God Trimmed Armor")
    elif  16 <= rollHard <= 25:
        print("Any Trimmed Rune Armor")
    elif  26 <= rollHard <= 50:
        print("Any Heraldic Rune Armor")
    elif  51 <= rollHard <= 54:
        print("Any Trimmed Dragonhide")
    elif  55 <= rollHard <= 57:
        print("Any Enchanted Outfit Piece")
    elif  58 <= rollHard <= 69:
        print("Any Vestment Piece")
    elif  70 <= rollHard <= 81:
        print("Any Blessed Dragonhide Piece")
    elif  82 <= rollHard <= 84:
        print("Any Cavalier")
    elif rollHard == 85:
        print("Pirate Hat")
    elif rollHard == 86:
        print("Robinhood Hat")
    elif rollHard == 87:
        print("Amulet of Fury (t)")
    elif rollHard == 88:
        print("Amulet of Glory (t)")
    elif rollHard == 89:
        print("Top Hat")
    elif rollHard == 90:
        print("Rune Cane")
    elif rollHard == 91:
        print("Animal Mask Table")
    elif rollHard == 92:
        print("Dragon Mask Table")
    elif rollHard == 93:
        print("Sack of Effigies Table")
    elif rollHard == 94:
        print("Backstab Table")
    elif rollHard == 95:
        print("Dye Table")
    elif rollHard == 96:
        print("Mega-Rare Table")
    print("Drop Complete! - Hard Drop Table")
    
hardDrop()