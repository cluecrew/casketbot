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
        rollAnimal = random.randint(1,3)
        if rollAnimal == 1:
            reward = "A Fox Mask"
        if rollAnimal == 2:
            reward = "A Unicorn Mask"
        if rollAnimal == 3:
            reward = "A Black Unicorn Mask"
    elif rollHard == 92:
        rollDragon = random.randint(1,3)
        if rollDragon == 1:
            reward = "A Green Dragon Mask"
        if rollDragon == 2:
            reward = "A Blue Dragon Mask"
        if rollDragon == 3:
            reward = "A Red Dragon Mask"
    elif rollHard == 93:
        rollEffigy = random.randint(1,30)
        if rollEffigy == 1:
            reward = "A Sack of Effigies Cape"
        else:
            rollBarrel = random.randint(1,120)
            if rollBarrel == 1:
                reward = "Explosive Barrel Cape"
            else:
                reward = "25,000 GP"
    elif rollHard == 94:
        rollBackstab = random.randint(1,15)
        if rollEffigy == 1:
            reward = "A Backstab Cape"
        else:
            reward = "10,000 GP"
    elif rollHard == 95:
        rollDye = random.randint(1,10)
        if rollDye == 1:
            reward = "A Shadow Dye"
        else:
            rollBarrows = random.randint(1,5)
            if rollBarrows == 1:
                reward = "A Barrows Dye"
            else:
                reward = "20,000 GP"
    elif rollHard == 96:
        rollMegaRare = random.randint(1,11)
        if 1 <= rollMegaRare <= 5:
            reward = "A gilded set piece"
        if 6 <= rollMegaRare <= 9:
            reward = "A Potion Set"
        if 10 == rollMegaRare:
            reward = "A Starved Ancient Effigy"
        if 11 == rollMegaRare:
            reward = "A drop from the 3rd Age Table"
    print("Drop Complete! - Hard Drop Table")
    return reward