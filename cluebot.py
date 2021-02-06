# cluebot.py
import os
import discord
from rs3_api import Hiscores

from dotenv import load_dotenv

load_dotenv()
Token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(Token)

def test_get_index_lite(self, hiscore):
        response = hiscore.get_index_lite("normal", "Clue Crew")
        assert isinstance(response, dict)

print(response)



