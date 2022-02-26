import os
import yaml
import discord
import math
from discord.ext import commands

data = yaml.load(open("settings.yaml", "r"))
version = str(data.get('version'))  

class info(commands.Cog, name="Information"):

  """Prints bot related information."""
  def init(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name='ping', help='Sends a \'pong\' message to the channel.')
  async def ping(self, ctx: commands.Context):
    await ctx.send('Pong!')
    print("Client should have pinged")

  @commands.command(name='tacos', help='Uses APP to determine whether ' \
    + 'or not you should use Tacos')
  async def tacos(self, ctx: commands.Context, appetite: int):
    tacocount = math.floor(appetite / 60)
    goldcount = math.floor(appetite / 100)

    tacostam = (95 + (5*tacocount)) * tacocount
    goldstam = (goldcount * 300)

    choice = f"Tacos provide {tacostam} Stamina versus Golden Potions providing {goldstam} Stamina"

    await ctx.send(choice)
    print("Client should have recommended for or against TACOS")

  @commands.command(name='version', brief='Prints the bot version', help='Prints the' \
    + 'bot\'s current version, as well as the version of Python it is written for.')
  async def version(self, ctx: commands.Context):
    botver = "BvS Bot is currently version " + version
    await ctx.send(botver)
    print("Client should have posted its version string")

def setup(bot: commands.Bot):
  bot.add_cog(info(bot))
