# casketbotv2.py
import os
import time
import csv
import math
import discord
import requests
import operator
import pandas as panda
from discord.ext import commands
import sqlite3
from sqlite3 import Error

####WELCOME TO CASKETBOT 2.0####
from dotenv import load_dotenv
load_dotenv()
Token = os.getenv('DISCORD_TOKEN') #pull discord token from environment file

##Create Connection to Database##
def create_connection(db_file):
##Connect to the SQLITE Database##
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

##Bot Command Prefix ##
bot = commands.Bot(command_prefix='=')

#Discord Connected & Ready Status to Log##
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
#Primary Stat Pulling Function#
#Returns DB variables#

def dye_values(hard, elite, master):
        barrows_dye_value = 179262*hard+182360*(elite+master)
        shadow_dye_value = 472331*hard+452871*(elite+master)
        ice_dye_value = 245290*(elite+master)
        third_age_dye_value = 735871*(elite+master)
        blood_dye_value = 735871*(elite+master)
        osh_value = 103846*master
        #substitute the real total dye value once competition is well under way
        total_dye_value = barrows_dye_value+shadow_dye_value+ice_dye_value+third_age_dye_value+blood_dye_value+osh_value
        #total_dye_value = 100000*(hard+elite+master)
        return (total_dye_value)

def clueStatsLookup(name):
    try:
        clueStatsLookup.urlerror = 0 #at beginning of loop there is no known error with this username
        beginnerUrl = "http://secure.runescape.com/m=hiscore/index_lite.ws?player=" #Runescape API to pull user data
        clueStatsLookup.username = str(name.lstrip("_")) #convert username to string
        clueStatsLookup.urlwithusername = beginnerUrl + clueStatsLookup.username #add username to end of URL
        column_names = ["Rank", "Clues", "XP"] #create 3 distinctly named columns for user data
        #print(clueStatsLookup.urlwithusername+ " will be the URL for this request!")
        url = clueStatsLookup.urlwithusername
        
        #Pull Clan info#
        #clanUrl_firsthalf = "https://secure.runescape.com/m=website-data/playerDetails.ws?names=%5B%22"
        #clanUrl_secondhalf ="%22%5D&callback=jQuery000000000000000_0000000000&_=0"
        #clanUrl = clanUrl_firsthalf+clueStatsLookup.username+clanUrl_secondhalf
        #clan_information = panda.read_csv(clanUrl)
        #claninfo = str(list(clan_information.columns.values))
        #if "clan" in claninfo:
            #pos = claninfo.index('clan',0)
            #pos2 = claninfo.index('title',0)
            #startpos = pos +6
            #endpos = pos2-5
            #clan = str(claninfo[startpos:endpos])
        #else:
            #clan = "Not Affiliated"
        #clueStatsLookup.clan = clan
        
        #Log information to console if successful
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        stats = panda.read_csv(url, names=column_names)
        print(time_string+":"+"Stats Found for " +clueStatsLookup.username)
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
        clueCounter = [clueStatsLookup.easyClueCount,clueStatsLookup.mediumClueCount,clueStatsLookup.hardClueCount,clueStatsLookup.eliteClueCount,clueStatsLookup.masterClueCount]
        pointTotal = 0
        #print(clueCounter)
        for x in range(5):
            pointTotal = pointTotal + math.pow(2, x) * ((math.floor(clueCounter[x]/500) * math.pow(2,5)) + (math.floor(clueCounter[x]/250) - math.floor(clueCounter[x]/500)) * math.pow(2,4) + (math.floor(clueCounter[x]/100) - math.floor(clueCounter[x]/500)) * math.pow(2,3) + (math.floor(clueCounter[x]/50) - math.floor(clueCounter[x]/100) - math.floor(clueCounter[x]/250) + math.floor(clueCounter[x]/500)) * math.pow(2,2) + (math.floor(clueCounter[x]/10) - math.floor(clueCounter[x]/50)) * math.pow(2,1) + (clueCounter[x]-math.floor(clueCounter[x]/10)) * math.pow(2,0))
            #print(pointTotal)
            #print(pointTotal)
        pointTotal = int(pointTotal)
        clueStatsLookup.pointTotals = pointTotal
        clueCheck.usernameWithSpaces = clueCheck.usernameWithSpaces.lower()
        clueCheck.usernameWithSpaces = clueCheck.usernameWithSpaces.lstrip()
        #profile_param = (Clues[54],Clues[55],Clues[56],Clues[57],Clues[58],pointTotal,str(clan),clueCheck.usernameWithSpaces);
        profile_param = (Clues[54],Clues[55],Clues[56],Clues[57],Clues[58],pointTotal,clueCheck.usernameWithSpaces);
        with open('clueStats.txt','a') as f:
            f.write(str(clueCheck.usernameWithSpaces))
            f.write(",")
            f.write(str(Clues[54]))
            f.write(",")
            f.write(str(Clues[55]))
            f.write(",")
            f.write(str(Clues[56]))
            f.write(",")
            f.write(str(Clues[57]))
            f.write(",")
            f.write(str(Clues[58]))
            f.write(",")
            named_tuple = time.localtime() # get struct_time
            time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
            f.write(time_string)
            f.write("\n")
        return profile_param
    except:
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        print(time_string+":"+"URL not applicable for: "+clueStatsLookup.username)
        clueStatsLookup.urlerror = 1
        pass





async def sendClueStatsEmbed(ctx):
    embed = discord.Embed(title="Clue stats for " + str(clueCheck.usernameWithSpaces), url=clueStatsLookup.urlwithusername, color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://i.ibb.co/pbVPb24/casketbot-profile-pic.png")
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
    embed.set_footer(text = time_string)
    #embed.set_footer(text = time_string+" | "+clueStatsLookup.clan)
    embed.add_field(name="Total Clue Points", value="Total Clue Points: "+ str(clueStatsLookup.pointTotals))
    embed.add_field(name="Total Clues Completed",value="Total Clues: " + str(clueStatsLookup.totalClues))
    embed.add_field(name="Master Clues",value="Count: "+str(clueStatsLookup.masterClueCount)+","+" Rank: "+str(clueStatsLookup.masterRank),inline=False)
    embed.add_field(name="Elite Clues",value="Count: "+str(clueStatsLookup.eliteClueCount)+","+" Rank: "+str(clueStatsLookup.eliteRank),inline=False)
    embed.add_field(name="Hard Clues",value="Count: "+str(clueStatsLookup.hardClueCount)+","+" Rank: "+str(clueStatsLookup.hardRank),inline=False)
    embed.add_field(name="Medium Clues",value="Count: "+str(clueStatsLookup.mediumClueCount)+","+" Rank: "+str(clueStatsLookup.mediumRank),inline=False)
    embed.add_field(name="Easy Clues",value="Count: "+str(clueStatsLookup.easyClueCount)+","+" Rank: "+str(clueStatsLookup.easyRank),inline=False)
    await ctx.send(embed=embed)        


async def updateTable(conn, profile_param):
    """
    UPDATE
    """
    sql = ''' INSERT OR IGNORE into clues (easy_count, medium_count, hard_count, elite_count, master_count, clue_points, name) values (?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, profile_param)
    conn.commit()
    sql = '''    UPDATE clues 
                  SET easy_count = ? ,
                  medium_count = ? ,
                  hard_count = ? ,
                  elite_count = ? ,
                  master_count = ?,
                  clue_points = ?
              WHERE name = ?'''
    cur = conn.cursor()
    cur.execute(sql, profile_param)
    conn.commit()



@bot.command(name='top', help = 'Responds with Clue Top Leaderboard')
async def topCheck(ctx, *args):
    top_clue_args = ""
    clan = ""
    top_clue_tier =""
    for arg in args:
        top_clue_args = top_clue_args + arg
    if "gors" in top_clue_args:
        clan = "Guardians of RS"
    if "pvmmax" in top_clue_args:
        clan = "PvmMax"
    if "easy" in top_clue_args:
        top_clue_type = "easy_stack"
        top_clue_tier = "easy"
        top_clue_title = " clues."
    if "medium" in top_clue_args:
        top_clue_type = "medium_stack"
        top_clue_tier = "medium"
        top_clue_title = " clues."
    if "hard" in top_clue_args:
        top_clue_type = "hard_stack"
        top_clue_tier = "hard"
        top_clue_title = " clues."
    if "elite" in top_clue_args:
        top_clue_type = "elite_stack"
        top_clue_tier = "elite"
        top_clue_title = " clues."
    if "master" in top_clue_args:
        top_clue_type = "master_stack"
        top_clue_tier = "master"
        top_clue_title = " clues."
    if top_clue_tier == "easy" or top_clue_tier == "medium" or top_clue_tier == "hard" or top_clue_tier == "elite" or top_clue_tier == "master":
        database = r"C:\Users\spenc\Desktop\CasketBot\master\db\cluesdb.db"
        conn = create_connection(database)
        cur = conn.cursor()
        if clan == "PvmMax" or clan == "Guardians of RS" :
            cur.execute("SELECT name,clan,"+top_clue_type+" FROM clues WHERE clan = '"+clan+"' ORDER BY "+top_clue_type+" DESC LIMIT 10")
        else:
            cur.execute("SELECT name,clan,"+top_clue_type+" FROM clues ORDER BY "+top_clue_type+" DESC LIMIT 10")
        rows = cur.fetchall()
        embed = discord.Embed(title="Top 10 "+top_clue_tier+top_clue_title, color=discord.Color.green())
        embed.set_thumbnail(url="https://i.ibb.co/pbVPb24/casketbot-profile-pic.png")
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        embed.set_footer(text = time_string+" - (optional) you can manually refresh your stats with =clues <username>")
        place = 1
        for row in rows:
            if place == 1:
                emoji = "<:Master:938810444645285899>"
            if place == 2:
                emoji = "<:Elite:938810444662063125>"
            if place == 3:
                emoji = "<:Hard:938810445538660412>"
            if place == 4:
                emoji = "<:Medium:938819439850315866>"
            if place == 5:
                emoji = "<:Easy:938810445022760990>"
            if place>5:
                emoji="<:gnomechild:941039082753114112>"
            #if "velho1mies" in row:
                #emoji=":rat:"
            embed.add_field(name=emoji+str(place)+". "+str(row[0])+" - "+row[1],value=str(row[2])+" "+top_clue_tier+" "+top_clue_title,inline=False)
            place=place+1
        print(time_string+":"+str(ctx.author.display_name)+" generated Leaderboard for" +top_clue_title)
        await ctx.send(embed=embed)
    else:
        top_clue_type = "competition_points"
        top_clue_tier = "competition points"
        top_clue_title = " competition points."
        database = r"C:\Users\spenc\Desktop\CasketBot\master\db\cluesdb.db"
        conn = create_connection(database)
        cur = conn.cursor()
        if clan == "PvmMax" or clan == "Guardians of RS" :
            cur.execute("SELECT name,clan,easy_stack,medium_stack,hard_stack,elite_stack,master_stack,competition_points FROM clues WHERE clan = '"+clan+"' ORDER BY "+top_clue_type+" DESC LIMIT 15")
        else:
            cur.execute("SELECT name,clan,easy_stack,medium_stack,hard_stack,elite_stack,master_stack,competition_points FROM clues ORDER BY "+top_clue_type+" DESC LIMIT 15")
        rows = cur.fetchall()
        embed = discord.Embed(title="Top 15"+top_clue_title, color=discord.Color.green())
        embed.set_thumbnail(url="https://i.ibb.co/pbVPb24/casketbot-profile-pic.png")
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        embed.set_footer(text = time_string+" - (optional) you can manually refresh your stats with =clues <username>")
        place = 1
        for row in rows:
            if place == 1:
                emoji = "<:Master:938810444645285899>"
            if place == 2:
                emoji = "<:Elite:938810444662063125>"
            if place == 3:
                emoji = "<:Hard:938810445538660412>"
            if place == 4:
                emoji = "<:Medium:938819439850315866>"
            if place == 5:
                emoji = "<:Easy:938810445022760990>"
            if place>5:
                emoji="<:gnomechild:941039082753114112>"
            #if "velho1mies" in row:
                #emoji=":rat:"
            embed.add_field(name=emoji+str(place)+". "+str(row[0])+" - "+row[1],value=str(row[2])+"|"+str(row[3])+"|"+str(row[4])+"|"+str(row[5])+"|"+str(row[6])+" for a total of "+str(row[7])+top_clue_title,inline=False)
            place=place+1
        print(time_string+":"+str(ctx.author.display_name)+" generated Leaderboard for" +top_clue_title)
        await ctx.send(embed=embed)
    
@bot.command(name='clues', help = 'Responds with Clue Stats')
async def clueCheck(ctx, *args):
    try:
        usernameForLookup = ""
        for arg in args:
            usernameForLookup = usernameForLookup + "_" + arg
        clueCheck.usernameWithSpaces = usernameForLookup.replace("_"," ")
        profile_param = clueStatsLookup(usernameForLookup)
        database = r"C:\Users\spenc\Desktop\CasketBot\master\db\cluesdb.db"
        conn = create_connection(database)
        with conn:
            await updateTable(conn, profile_param)
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        print(time_string+":"+"DB Updated for "+clueCheck.usernameWithSpaces)
        await sendClueStatsEmbed(ctx)
    except:
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
        await ctx.send("Please type a valid username after the command.")
        clueStatsLookup.urlerror = 1
        pass


@bot.command(name='stats', help = 'Responds with Clue Competition Stats')
async def clueStats(ctx, *args):
    

    stats_args= ""
    clan = ""
    for arg in args:
        stats_args = stats_args + arg
    if "gors" in stats_args:
        clan = "Guardians of RS"
    if "pvmmax" in stats_args:
        clan = "PvmMax"
    database = r"C:\Users\spenc\Desktop\CasketBot\master\db\cluesdb.db"
    conn = create_connection(database)
    cur = conn.cursor()
    stat_pull = []
    if clan == "PvmMax" or clan == "Guardians of RS" :        
        stat_pull = cur.execute("SELECT sum(case When competition_points > 0 Then 1 Else 0 End),sum(easy_stack),sum(medium_stack),sum(hard_stack),sum(elite_stack),sum(master_stack),sum(competition_points) FROM clues WHERE clan = '"+clan+"'").fetchall()
        var = []
        for x in stat_pull[0]:
            var.append(x)
        embed = discord.Embed(title="Clue Statistics for "+clan, color=discord.Color.green())
        embed.add_field(name="Total Caskets Stacked",value=str("{:,}".format(var[1]+var[2]+var[3]+var[4]+var[5]))+" Total Caskets Worth "+str("{:,}".format(var[6]))+" competition points.",inline=False)
        embed.add_field(name="Total Estimated Value",value=str("{:,}".format(var[1]*500000+var[2]*500000+var[3]*1200000+var[4]*1000000+var[5]*2000000+dye_values(var[3],var[4],var[5])))+" gp",inline=False)
        embed.add_field(name="Total Easy Clues",value=str("{:,}".format(var[1]))+" clues.",inline=False)
        embed.add_field(name="Total Medium Clues",value=str("{:,}".format(var[2]))+" clues.",inline=False)
        embed.add_field(name="Total Hard Clues",value=str("{:,}".format(var[3]))+" clues.",inline=False)
        embed.add_field(name="Total Elite Clues",value=str("{:,}".format(var[4]))+" clues.",inline=False)
        embed.add_field(name="Total Master Clues",value=str("{:,}".format(var[5]))+" clues.",inline=False)
        embed.add_field(name="Total Participants",value=str("{:,}".format(var[0]))+" clue chasers in the "+clan+" clan.",inline=False)
    else:
        stat_pull = cur.execute("SELECT sum(case When competition_points > 0 Then 1 Else 0 End),sum(easy_stack),sum(medium_stack),sum(hard_stack),sum(elite_stack),sum(master_stack),sum(competition_points) FROM clues").fetchall()
        var = []
        for x in stat_pull[0]:
            var.append(x)
        embed = discord.Embed(title="Clue Statistics for All Participants", color=discord.Color.blue())
        embed.add_field(name="Total Caskets Stacked",value=str("{:,}".format(var[1]+var[2]+var[3]+var[4]+var[5]))+" Total Caskets Worth "+str("{:,}".format(var[6]))+" competition points.",inline=False)
        embed.add_field(name="Total Estimated Value",value=str("{:,}".format(var[1]*500000+var[2]*500000+var[3]*1200000+var[4]*1000000+var[5]*2000000+dye_values(var[3],var[4],var[5])))+" gp",inline=False)
        embed.add_field(name="Total Easy Clues",value=str("{:,}".format(var[1]))+" clues.",inline=False)
        embed.add_field(name="Total Medium Clues",value=str("{:,}".format(var[2]))+" clues.",inline=False)
        embed.add_field(name="Total Hard Clues",value=str("{:,}".format(var[3]))+" clues.",inline=False)
        embed.add_field(name="Total Elite Clues",value=str("{:,}".format(var[4]))+" clues.",inline=False)
        embed.add_field(name="Total Master Clues",value=str("{:,}".format(var[5]))+" clues.",inline=False)
        embed.add_field(name="Total Participants",value=str("{:,}".format(var[0]))+" clue chasers.",inline=False)
    embed.set_thumbnail(url="https://i.ibb.co/pbVPb24/casketbot-profile-pic.png")
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y - %H:%M:%S", named_tuple)
    embed.set_footer(text = time_string+" - (optional) you can manually refresh your stats with =clues <username>")
    print(time_string+":"+str(ctx.author.display_name)+" generated Stats")
    await ctx.send(embed=embed)





async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return


bot.run(Token)


