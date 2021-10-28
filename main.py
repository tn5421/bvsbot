import time
import json
import discord

from discord.ext import commands

settings = json.loads(open('settings.json').read())
token = settings['token']
bvs_ver = settings['version']

# client = discord.Client()
bot = commands.Bot(command_prefix="!", description="A simple WKAI bot written by tn5421, with help from Mitillos")

wk_list = ["Craftworld at War", "AspenStory",
           "ADAM", "FarmVale", "ForeverQuest"]

def distance(list1, list2):
    j = (list2 - list1) % 5
    return j

def get_rday():
    return (int(time.strftime("%d")))

# def wk_day():
#     return (get_rday() % 5)

@bot.command(name='ping', help='Sends a \'pong\' message to the channel.')
async def ping(ctx):
    await ctx.send('Pong!')
    print("Client should have pinged")

@bot.command(name='wkai')
async def wkai(ctx):
    day_wkai = "Today's WKAI summon is a "

    wk_day = get_rday() % 5
    day_wkai += wk_list[wk_day]

    await ctx.send(day_wkai)
    print("Client should have posted today's WKAI")

@bot.command(name='cow')
async def cow(ctx):
    cow_wkai = "The next Craftworld of War summoning is in "
    wk_day = get_rday() % 5
    if wk_day == 0:
        cow_wkai += "5 Days"
    else:
        cow_wkai += (str(5 - wk_day)) + " Day(s)"
    await ctx.send(cow_wkai)
    print("Client should have posted next CoW WKAI")

@bot.command(name='aspen')
async def aspen(ctx):
    aspen_wkai = "The next AspenStory summoning is in "
    wk_day = get_rday() % 5
    wk_distance = distance(wk_day, 1)
    if wk_day == 1:
        aspen_wkai += "5 Days"
    else:
        aspen_wkai += (str(wk_distance)) + " Day(s)"
    await ctx.send(aspen_wkai)
    print("Client should have posted next Aspen WKAI")

@bot.command(name='adam')
async def adam(ctx):
    adam_wkai = "The next ADAM summoning is in "
    wk_day = get_rday() % 5
    wk_distance = distance(wk_day, 2)
    if wk_day == 2:
        adam_wkai += "5 Days"
    else:
        adam_wkai += (str(wk_distance)) + " Day(s)"
    await ctx.send(adam_wkai)
    print("Client should have posted next ADAM WKAI")

@bot.command(name='farm')
async def farm(ctx):
    farm_wkai = "The next FarmVale summoning is in "
    wk_day = get_rday() % 5
    wk_distance = distance(wk_day, 3)
    if wk_day == 3:
        farm_wkai += "5 Days"
    else:
        farm_wkai += (str(wk_distance)) + " Day(s)"
    await ctx.send(farm_wkai)
    print("Client should have posted next FarmVille WKAI")

@bot.command(name='fq')
async def fq(ctx):
    fq_wkai = "The next ForeverQuest summoning is in "
    wk_day = get_rday() % 5
    wk_distance = distance(wk_day, 4)
    if wk_day == 4:
        fq_wkai += "5 Days"
    else:
        fq_wkai += (str(wk_distance)) + " Day(s)"
    await ctx.send(fq_wkai)
    print("Client should have posted next FQ WKAI")

@bot.command(name='version')
async def version(ctx):
    botver = "BvS-Discord-Bot is currently version " + (str(bvs_ver))
    await ctx.send(botver)
    print("Client should have posted its version string")

bot.run(token)
