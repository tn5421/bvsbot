import time
import json
import discord
import datetime

from discord.ext import commands

settings = json.loads(open('settings.json').read())
token = settings['token']
bvs_ver = settings['version']

# client = discord.Client()
bot = commands.Bot(command_prefix="!", description="A simple WKAI bot written by tn5421, with help from Mitillos")

wk_list = ["Craftworld at War", "AspenStory",
           "ADAM", "FarmVale", "ForeverQuest"]

def get_rday(offsetdays=0):
    return (int((datetime.datetime.now(datetime.timezone(-datetime.timedelta(hours=5)))+datetime.timedelta(days=offsetdays)).strftime("%d")))

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
    for offset in range(1,10):
        if (get_rday(offset) % 5 == 0):
           cow_wkai = "The next Craftworld of War summoning is in {0} Day(s)".format(offset)
           break;
    await ctx.send(cow_wkai)
    print("Client should have posted next CoW WKAI")

@bot.command(name='aspen')
async def aspen(ctx):
    for offset in range(1,10):
        if (get_rday(offset) % 5 == 1):
           aspen_wkai = "The next AspenStory summoning is in {0} Day(s)".format(offset)
           break;
    await ctx.send(aspen_wkai)
    print("Client should have posted next Aspen WKAI")

@bot.command(name='adam')
async def adam(ctx):
    for offset in range(1,10):
        if (get_rday(offset) % 5 == 2):
           adam_wkai = "The next ADAM summoning is in {0} Day(s)".format(offset)
           break;
    await ctx.send(adam_wkai)
    print("Client should have posted next ADAM WKAI")

@bot.command(name='farm')
async def farm(ctx):
    for offset in range(1,10):
        if (get_rday(offset) % 5 == 3):
           farm_wkai = "The next FarmVale summoning is in {0} Day(s)".format(offset)
           break;
    await ctx.send(farm_wkai)
    print("Client should have posted next FarmVille WKAI")

@bot.command(name='fq')
async def fq(ctx):
    for offset in range(1,10):
        if (get_rday(offset) % 5 == 4):
           fq_wkai = "The next ForeverQuest summoning is in {0} Day(s)".format(offset)
           break;
    await ctx.send(fq_wkai)
    print("Client should have posted next FQ WKAI")

@bot.command(name='version')
async def version(ctx):
    botver = "BvS-Discord-Bot is currently version " + (str(bvs_ver))
    await ctx.send(botver)
    print("Client should have posted its version string")

bot.run(token)
