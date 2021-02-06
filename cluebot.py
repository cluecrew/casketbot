# cluebot.py
import os
import discord
import pandas as panda
from discord.ext import commands


from dotenv import load_dotenv
load_dotenv()
Token = os.getenv('DISCORD_TOKEN') #pull discord token from environment file

def clueStatsLookup(name):
    beginnerUrl = "http://secure.runescape.com/m=hiscore/index_lite.ws?player="
    username = str(name)
    clueStatsLookup.urlwithusername = beginnerUrl + username
    column_names = ["Rank", "Clues", "XP"]
    print(beginnerUrl)
    url = clueStatsLookup.urlwithusername
    stats = panda.read_csv(url, names=column_names)
    print(stats)
    Ranks = stats.Rank.to_list() 
    Clues = stats.Clues.to_list()
    clueStatsLookup.easyClueCount = Clues[54]
    clueStatsLookup.mediumClueCount = Clues[55]
    clueStatsLookup.hardClueCount = Clues[56]
    clueStatsLookup.eliteClueCount = Clues[57]
    clueStatsLookup.masterClueCount = Clues[58]
    #Obtain Ranking for each clue type
    
    clueStatsLookup.easyRank = Ranks[54]
    clueStatsLookup.mediumRank = Ranks[55]
    clueStatsLookup.hardRank = Ranks[56]
    clueStatsLookup.eliteRank = Ranks[57]
    clueStatsLookup.masterRank = Ranks[58]
    clueStatsLookup.totalClues = clueStatsLookup.easyClueCount + clueStatsLookup.mediumClueCount + clueStatsLookup.hardClueCount + clueStatsLookup.eliteClueCount + clueStatsLookup.masterClueCount
    print("Successful function")

#client = discord.Client()
bot = commands.Bot(command_prefix='=')

######Original Function to Find Clue Stats based on username
#beginnerUrl = 'http://secure.runescape.com/m=hiscore/index_lite.ws?player='
#username = 'Clue_Crew'
#urlwithusername = beginnerUrl + username
#column_names = ["Rank", "Clues", "XP"]
#url = urlwithusername
#stats = panda.read_csv(url, names=column_names)
#print(stats)
#print("Stats Fetched")
#Create a list for rank and clue categories
#Ranks = stats.Rank.to_list() 
#Clues = stats.Clues.to_list()
#print("Data converted to list format")
#Obtain Clue Count for each Clue Type
#
#easyClueCount = Clues[54]
#mediumClueCount = Clues[55]
#hardClueCount = Clues[56]
#eliteClueCount = Clues[57]
#masterClueCount = Clues[58]
#Obtain Ranking for each clue type
#
#easyRank = Ranks[54]
#mediumRank = Ranks[55]
#hardRank = Ranks[56]
#eliteRank = Ranks[57]
#masterRank = Ranks[58]
#totalClues = easyClueCount + mediumClueCount + hardClueCount + eliteClueCount + masterClueCount #Count total clues
#print("Easy Clues "+ str(easyClueCount)) #Print number of easy clues as a string (will only print a string)
################
###############

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
#@client.event
#async def on_message(message):
#   if message.author == client.user:
#        return
#    if message == "test":
#        print("Test initiated")
#        clueStatsLookup("Clue_Crew")
#        response = easyClueCount
#        await message.channel.send(response)        

@bot.command(name='clues', help='Responds with Clue Stats')
async def clueCheck(ctx):
    clueStatsLookup("Clue_Crew")
    print("Stats looked up!")
    response = ("Success!")
    response2 = ("You have completed a total of "+ str(clueStatsLookup.totalClues) + " Clues!")
    await ctx.send(response)
    await ctx.send(response2)
    #embed response into a message block that looks professional
    embed = discord.Embed(title="Clue Hunting Stats", url=clueStatsLookup.urlwithusername, description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.ibb.co/jy4nvMV/thumbnail10.png")
    await ctx.send(embed=embed)    

bot.run(Token)

