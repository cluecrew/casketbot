# cluebot.py
import os
import discord
import pandas as panda


from dotenv import load_dotenv

load_dotenv()
Token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
beginnerUrl = 'http://secure.runescape.com/m=hiscore/index_lite.ws?player='
username = 'Clue_Crew'

urlwithusername = beginnerUrl + username

column_names = ["Rank", "Clues", "XP"]

url = urlwithusername
stats = panda.read_csv(url, names=column_names)
print(stats)

Ranks = stats.Rank.to_list()
Clues = stats.Clues.to_list()

easyClueCount = Clues[54]
mediumClueCount = Clues[55]
hardClueCount = Clues[56]
eliteClueCount = Clues[57]

print("Easy Clues "+ str(easyClueCount))


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(Token)

