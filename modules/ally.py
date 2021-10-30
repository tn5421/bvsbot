import re
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
    
    if allies.get(userinput) == 0:
      output = "Does not match an ally in the database! Pester tn5421#0271 if this is in error!"
    else:
      output = str(allies.get(userinput))
      
      output=re.sub('\'((?=type)|(?=obtain)|(?=description)|(?=bonus)|(?=teams))', '  ', output) 
      # remove leading quotation marks on categories
      output=re.sub('\':', ':', output) # remove trailing quotation marks on categories
      output=re.sub('{', ' ', output) # replace the opening { with a space
      output=re.sub('[}\[\]]', '', output) # strip out some undesired characters
      output=re.sub('\'[^0-9A-Za-z+\-:]', '\'\n', output) # insert a newline character after closing quotation marks
      output=re.sub('\n +\'', '\n          \'', output) # align non-category lines
    
    stream.close() # close file.

    await ctx.send(output)
    print("Ally Shenanigans!")

def setup(bot: commands.Bot):
    bot.add_cog(ally(bot))
