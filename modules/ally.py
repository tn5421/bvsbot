import yaml
import discord
from discord.ext import commands

class ally(commands.Cog, name="Allies"):

  """Prints Ally related information"""
  def init(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name='ally', brief='Find info on allies!', help='Find more information '\
  + 'on allies! Please format your command like this: !ally billy2.')
  async def ally(self, ctx: commands.Context, userinput: str):
    
    # allies.yaml will not be categorized in a manner 
    # consistent with the bvs.wikidot.com wiki. 
    # Instead, feel free to add categorization subtags
    # to their 'type' subattribute.
    
    userinput = userinput.lower()
    stream = open("data/allies.yaml", "r") # abstracted so we can close it again
    allies = yaml.load(stream)
    output = allies.get(userinput)
    stream.close() # close file.
     
    # You are welcome to re-write this into a regex at any time!
    # Thank you in advance for your consideration.
    
    # P.S. These transformations such, I hope one of you is a REGEX WIZARD!
    
    output = str(output)
    output = output.strip("{}\'\"")
    
    await ctx.send(output)
    print("Ally Shenanigans!")

def setup(bot: commands.Bot):
    bot.add_cog(ally(bot))
