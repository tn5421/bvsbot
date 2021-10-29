import json
import discord
import os

from discord.ext import commands

settings = json.loads(open('settings.json').read())
token = settings['token']

client = commands.Bot(command_prefix="!", description="A simple WKAI bot written by tn5421, with help from Mitillos")

for file in os.listdir("modules"):
    if file.endswith(".py"):
        file = file[:-3]
        client.load_extension(f"modules.{file}")

client.run(token)

