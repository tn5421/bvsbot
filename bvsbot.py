import yaml
import discord
import os

from discord.ext import commands

data = yaml.load(open("settings.yaml", 'r'))
token = str(data.get('token'))

intents = discord.Intents().all()

client = commands.Bot(command_prefix="!", description="A simple bot" \
  + "written for the community!", intents=intents)

for file in os.listdir("modules"):
  if file.endswith(".py"):
    file = file[:-3]
    client.load_extension(f"modules.{file}")

client.run(token)
