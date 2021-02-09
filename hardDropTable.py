# hardDropTable.py
import os
import random
def hardDrop():
    rollHard = random.randint(1,96)
    #print("Rolled a "+str(rollHard)+"!")
    if  1 <= rollHard <= 15:
        reward = "A Piece from the God Trimmed Armor Table"
        dropId = 2669
    elif  16 <= rollHard <= 25:
        reward = "A Piece from the Trimmed Rune Armor Table"
        dropId = 2623
    elif  26 <= rollHard <= 50:
        reward = "A Piece from the Heraldic Rune Armor Table"
        dropId = 19179
    elif  51 <= rollHard <= 54:
        reward = "A Piece from the Trimmed Dragonhide Table"
        dropId = 12943
    elif  55 <= rollHard <= 57:
        reward = "A Piece from the Enchanted Outfit Table"
        dropId = 7400
    elif  58 <= rollHard <= 69:
        reward = "A Piece from the Vestment Table"
        dropId = 10470
    elif  70 <= rollHard <= 81:
        reward = "A Piece from the Blessed Dragonhide Table"
        dropId = 10370
    elif  82 <= rollHard <= 84:
        reward = "A Hat from the Cavalier Hat Table"
        dropId = 2639
    elif rollHard == 85:
        reward = "A Pirate Hat"
        dropId = 8950
    elif rollHard == 86:
        reward = "A Robinhood Hat"
        dropId = 2581
    elif rollHard == 87:
        reward = "An Amulet of Fury (t)"
        dropId = 33502
    elif rollHard == 88:
        reward = "An Amulet of Glory (t)"
        dropId = 10362
    elif rollHard == 89:
        reward = "A Top Hat"
        dropId = 13101
    elif rollHard == 90:
        reward = "A Rune Cane"
        dropId = 13099
    elif rollHard == 91:
        rollAnimal = random.randint(1,3)
        if rollAnimal == 1:
            reward = "A Fox Mask"
            dropId = 19272
        if rollAnimal == 2:
            reward = "A Unicorn Mask"
            dropId = 19275
        if rollAnimal == 3:
            reward = "A Black Unicorn Mask"
            dropId = 19278
    elif rollHard == 92:
        rollDragon = random.randint(1,3)
        if rollDragon == 1:
            reward = "A Green Dragon Mask"
            dropId = 19281
        if rollDragon == 2:
            reward = "A Blue Dragon Mask"
            dropId = 19284
        if rollDragon == 3:
            reward = "A Red Dragon Mask"
            dropId = 19287
    elif rollHard == 93:
        rollEffigy = random.randint(1,30)
        if rollEffigy == 1:
            reward = "A Sack of Effigies Cape"
            dropId = 33518
        else:
            rollBarrel = random.randint(1,120)
            if rollBarrel == 1:
                reward = "Explosive Barrel Cape"
                dropId = 33516
            else:
                reward = "25,000 GP"
                dropId = 30069
    elif rollHard == 94:
        rollBackstab = random.randint(1,15)
        if rollBackstab == 1:
            reward = "A Backstab Cape"
            dropId = 33520
        else:
            reward = "10,000 GP"
            dropId = 30069
    elif rollHard == 95:
        rollDye = random.randint(1,10)
        if rollDye == 1:
            reward = "A Shadow Dye"
            dropId = 33296
        else:
            rollBarrows = random.randint(1,5)
            if rollBarrows == 1:
                reward = "A Barrows Dye"
                dropId = 33294
            else:
                reward = "20,000 GP"
                dropId = 30069
    elif rollHard == 96:
        rollMegaRare = random.randint(1,11)
        if 1 <= rollMegaRare <= 5:
            reward = "A gilded set piece"
            dropId = 3481
        if 6 <= rollMegaRare <= 9:
            reward = "A Potion Set"
            dropId = 3024
        if 10 == rollMegaRare:
            reward = "A Starved Ancient Effigy"
            dropId = 18778
        if 11 == rollMegaRare:
            reward = "A drop from the 3rd Age Table" 
            dropId = 10348
    return reward, dropId;