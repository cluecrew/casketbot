# casketbot.py
import os
import time
import csv
import math
import discord
import pandas as panda
from discord.ext import commands
from hardDropTable import *

####WELCOME TO CASKETBOT#### 


from dotenv import load_dotenv
load_dotenv()
Token = os.getenv('DISCORD_TOKEN') #pull discord token from environment file

def clueStatsLookup(name):
    try:
        clueStatsLookup.urlerror = 0
        beginnerUrl = "http://secure.runescape.com/m=hiscore/index_lite.ws?player="
        username = str(name)
        clueStatsLookup.urlwithusername = beginnerUrl + username
        column_names = ["Rank", "Clues", "XP"]
        #print(clueStatsLookup.urlwithusername+ " will be the URL for this request!")
        url = clueStatsLookup.urlwithusername
        stats = panda.read_csv(url, names=column_names)
        
        print("Stats found for "+username)
        Ranks = stats.Rank.to_list() 
        Clues = stats.Clues.to_list()
        Clues = [0 if i==-1 else i for i in Clues]
        Ranks = [0 if i==-1 else i for i in Ranks]
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
    except:
        print("URL not applicable for: "+username)
        clueStatsLookup.urlerror = 1
        pass
    
#client = discord.Client()
bot = commands.Bot(command_prefix='=')

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


@bot.command(name='setrsn', help='Set your Runescape 3 Username to pull clue stats')
async def setRsn(ctx, *args):
    usernameDesired = ""
    for arg in args:
        usernameDesired = usernameDesired + "_" + arg
    #print(usernameDesired+" is the desired username!")
    #print(ctx.author.display_name)
    embed = discord.Embed(title="Set Username for " + ctx.author.display_name, url=clueStatsLookup.urlwithusername, description="You have assigned" + usernameDesired + " to your profile!" , color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.ibb.co/jy4nvMV/thumbnail10.png")
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    embed.set_footer(text = time_string)
    await ctx.send(embed=embed)
    
@bot.command(name='opencasket', help='Simulates opening a Hard Clue Casket')
async def openCasket(ctx):
    reward = hardDrop()
    print (ctx.author.display_name+" has been rewarded with: "+reward)
    await ctx.send("You have been rewarded: "+reward)


@bot.command(name='clues', help='Responds with Clue Stats')
async def clueCheck(ctx, *args):
    userId = int(ctx.author.id)
    print(str(userId))
    usernameForLookup = ""
    for arg in args:
        usernameForLookup = usernameForLookup + "_" + arg
    #print(usernameForLookup)
    clueStatsLookup(usernameForLookup)
    clueCheck.usernameWithSpaces = usernameForLookup.replace("_"," ")
    #print("Stats looked up!")
    #embed response into a message block that looks professional
    if clueStatsLookup.urlerror == 0:
        await sendClueStatsEmbed(ctx)
    else:
        await ctx.send("Please type a valid username after the command. (=clues Clue Crew)")
    
async def sendClueStatsEmbed(ctx):
    embed = discord.Embed(title="Clue stats for" + str(clueCheck.usernameWithSpaces), url=clueStatsLookup.urlwithusername, description="Successful Search!", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.ibb.co/jy4nvMV/thumbnail10.png")
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    embed.set_footer(text = time_string)
    clueCounter = [clueStatsLookup.easyClueCount,clueStatsLookup.mediumClueCount,clueStatsLookup.hardClueCount,clueStatsLookup.eliteClueCount,clueStatsLookup.masterClueCount]
    pointTotal = 0
    #print(clueCounter)
    for x in range(5):
        pointTotal = pointTotal + math.pow(2, x) * ((math.floor(clueCounter[x]/500) * math.pow(2,5)) + (math.floor(clueCounter[x]/250) - math.floor(clueCounter[x]/500)) * math.pow(2,4) + (math.floor(clueCounter[x]/100) - math.floor(clueCounter[x]/500)) * math.pow(2,3) + (math.floor(clueCounter[x]/50) - math.floor(clueCounter[x]/100) - math.floor(clueCounter[x]/250) + math.floor(clueCounter[x]/500)) * math.pow(2,2) + (math.floor(clueCounter[x]/10) - math.floor(clueCounter[x]/50)) * math.pow(2,1) + (clueCounter[x]-math.floor(clueCounter[x]/10)) * math.pow(2,0))
        #print(pointTotal)
    #print(pointTotal)
    pointTotal = int(pointTotal)
    embed.add_field(name="Total Clue Points", value="Total Clue Points: "+ str(pointTotal))
    embed.add_field(name="Total Clues Completed",value="Total Clues: " + str(clueStatsLookup.totalClues))
    embed.add_field(name="Master Clues",value="Count: "+str(clueStatsLookup.masterClueCount)+","+" Rank: "+str(clueStatsLookup.masterRank),inline=False)
    embed.add_field(name="Elite Clues",value="Count: "+str(clueStatsLookup.eliteClueCount)+","+" Rank: "+str(clueStatsLookup.eliteRank),inline=False)
    embed.add_field(name="Hard Clues",value="Count: "+str(clueStatsLookup.hardClueCount)+","+" Rank: "+str(clueStatsLookup.hardRank),inline=False)
    embed.add_field(name="Medium Clues",value="Count: "+str(clueStatsLookup.mediumClueCount)+","+" Rank: "+str(clueStatsLookup.mediumRank),inline=False)
    embed.add_field(name="Easy Clues",value="Count: "+str(clueStatsLookup.easyClueCount)+","+" Rank: "+str(clueStatsLookup.easyRank),inline=False)
    
    await ctx.send(embed=embed)

bot.run(Token)
