import os
import yaml
import discord
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

  @commands.command(name='version', brief='Prints the bot version', help='Prints the' \
    + 'bot\'s current version, as well as the version of Python it is written for.')
  async def version(self, ctx: commands.Context):
    botver = "BvS Bot is currently version " + version
    await ctx.send(botver)
    print("Client should have posted its version string")

def setup(bot: commands.Bot):
  bot.add_cog(info(bot))
