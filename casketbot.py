# casketbot.py
import os
import time
import csv
import math
import discord
import requests
import operator
import pandas as panda
from discord.ext import commands
from hardDropTable import *

####WELCOME TO CASKETBOT 1.0#### 


from dotenv import load_dotenv
load_dotenv()
Token = os.getenv('DISCORD_TOKEN') #pull discord token from environment file

def clueStatsLookup(name):
    try:
        clueStatsLookup.urlerror = 0 #at beginning of loop there is no known error with this username
        beginnerUrl = "http://secure.runescape.com/m=hiscore/index_lite.ws?player=" #Runescape API to pull user data
        clueStatsLookup.username = str(name) #convert username to string
        clueStatsLookup.urlwithusername = beginnerUrl + clueStatsLookup.username #add username to end of URL
        column_names = ["Rank", "Clues", "XP"] #create 3 distinctly named columns for user data
        #print(clueStatsLookup.urlwithusername+ " will be the URL for this request!")
        url = clueStatsLookup.urlwithusername
        
        #Log information to console if successful
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        print(time_string+":"+" Stats Found for" +clueStatsLookup.username)

        stats = panda.read_csv(url, names=column_names)
        Ranks = stats.Rank.to_list()#create rank listing 
        Clues = stats.Clues.to_list()#create clue count listing
        Clues = [0 if i==-1 else i for i in Clues] #replace -1's with zeros
        Ranks = [0 if i==-1 else i for i in Ranks] #replace -1's with zeros
        
        #Obtain Clue Count for each clue type
        
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
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        print(time_string+":"+" URL not applicable for: "+clueStatsLookup.username)
        clueStatsLookup.urlerror = 1
        pass
async def sendClueStatsEmbed(ctx):
    with open('clueStats.txt','a') as f:
        f.write(str(clueCheck.userId))
        f.write(",")
        f.write(str(ctx.author.display_name))
        f.write(",")
        f.write(str(clueStatsLookup.username))
        f.write(",")
        f.write(str(clueStatsLookup.totalClues))
        f.write(",")
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        f.write(time_string)
        f.write("\n")
    embed = discord.Embed(title="Clue stats for" + str(clueCheck.usernameWithSpaces), url=clueStatsLookup.urlwithusername, color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.ibb.co/pbVPb24/casketbot-profile-pic.png")
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
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


#@bot.command(name='setrsn', help='Set your Runescape 3 Username to pull clue stats')
#async def setRsn(ctx, *args):
    #userId = int(ctx.author.id)
    #usernameDesired = ""
    #for arg in args:
        #usernameDesired = usernameDesired + "_" + arg
    #usernameWithSpaces = usernameDesired.replace("_"," ")
    #print(usernameDesired+" is the desired username!")
    #print(ctx.author.display_name)  
    #embed = discord.Embed(title="Set Username for " + usernameWithSpaces, url=clueStatsLookup.urlwithusername, description="You have assigned" + usernameDesired + " to your profile!" , color=discord.Color.blue())
    #embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    #embed.set_thumbnail(url="https://i.ibb.co/jy4nvMV/thumbnail10.png")
    #named_tuple = time.localtime() # get struct_time
    #time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    #embed.set_footer(text = time_string)
    #Sawait ctx.send(embed=embed)
    
@bot.command(name='opencasket', help='Simulates opening a Hard Clue Casket')
async def openCasket(ctx):
    userId = int(ctx.author.id)
    reward, dropId = hardDrop()
    with open('dropData.txt','a') as f:
        f.write(str(userId))
        f.write(",")
        f.write(str(ctx.author.display_name))
        f.write(",")
        f.write(str(reward))
        f.write(",")
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        f.write(time_string)
        f.write("\n")
    embed = discord.Embed(title="Hard Clue Casket Opened! ", description="You have been rewarded: " + reward, color=discord.Color.green())
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://secure.runescape.com/m=itemdb_rs/obj_sprite.gif?id="+str(dropId))
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
    embed.set_footer(text = time_string)
    print (time_string + ":"+ctx.author.display_name+" has been rewarded with: "+reward)
    await ctx.send(embed=embed)
    #await ctx.send("You have been rewarded: "+reward)


@bot.command(name='clues', help='Responds with Clue Stats')
async def clueCheck(ctx, *args):
    clueCheck.userId = int(ctx.author.id)
    #print(str(clueCheck.userId))
    #if username is in file/search for username in file
    
    
    
    
    
    
    #if username is not in file
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


###VIS WAX Command###
def remafterrune(text):
    where_rune = text.find('Rune')
    if where_rune == -1:
        return text
    return text[:where_rune + 4]


def getID(rune):
    runeID = 0
    if operator.contains(rune,"Fire"):
        runeID = 554
        return runeID
    if operator.contains(rune,"Water"):
        runeID = 555
        return runeID
    if operator.contains(rune,"Air"):
        runeID = 556
        return runeID
    if operator.contains(rune,"Earth"):
        runeID = 557
        return runeID
    if operator.contains(rune,"Mind"):
        runeID = 558
        return runeID
    if operator.contains(rune,"Body"):
        runeID = 559
        return runeID
    if operator.contains(rune,"Death"):
        runeID = 560
        return runeID
    if operator.contains(rune,"Nature"):
        runeID = 561
        return runeID
    if operator.contains(rune,"Chaos"):
        runeID = 562
        return runeID
    if operator.contains(rune,"Law"):
        runeID = 563
        return runeID
    if operator.contains(rune,"Cosmic"):
        runeID = 564
        return runeID
    if operator.contains(rune,"Blood"):
        runeID = 565
        return runeID
    if operator.contains(rune,"Soul"):
        runeID = 566
        return runeID
    if operator.contains(rune,"Steam"):
        runeID = 4694
        return runeID
    if operator.contains(rune,"Mist"):
        runeID = 4695
        return runeID
    if operator.contains(rune,"Dust"):
        runeID = 4696
        return runeID
    if operator.contains(rune,"Smoke"):
        runeID = 4697
        return runeID
    if operator.contains(rune,"Mud"):
        runeID = 4698
        return runeID
    if operator.contains(rune,"Lava"):
        runeID = 4699
        return runeID
    else:
        print("Rune ID not found")
    return runeID


@bot.command(name='vis',help='Responds with Vis Wax Combos for Today')
async def visWax(ctx):
    url = 'https://warbandtracker.com/goldberg/'
    html = requests.get(url).content
    df_list = panda.read_html(html)
    df = df_list[0]
    #print(df)
    rune1 = df[0]
    rune1 = str(rune1[1])
    rune2 = df[0]
    rune2 = str(rune2[3])
    rune3 = df[1]
    rune3 = str(rune3[3])
    rune4 = df[2]
    rune4 = str(rune4[3])
    rune1 = (remafterrune(rune1))
    rune2 = (remafterrune(rune2))
    rune3 = (remafterrune(rune3))
    rune4 = (remafterrune(rune4))
    rune1ID = str(getID(rune1))
    rune2ID = str(getID(rune2))
    rune3ID = str(getID(rune3))
    rune4ID = str(getID(rune4))
    embed = discord.Embed(title="Vis Wax Combinations", url="https://warbandtracker.com/goldberg/", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.ibb.co/pbVPb24/casketbot-profile-pic.png")
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
    embed.set_footer(text = time_string)
    embed.add_field(name="First Rune", value=rune1)
    embed.add_field(name="Second Rune",value=rune2 + " or "+rune3+" or "+rune4)
    print(time_string + ": "+ctx.author.display_name+" requested today's Vis Wax Combo ("+rune1+") and (" +rune2+" or "+rune3+" or "+rune4+")")
    await ctx.send(embed=embed) 











    
bot.run(Token)
