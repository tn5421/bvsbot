import discord
from discord.ext import commands

class ally(commands.Cog, name="Allies"):

    """Prints Ally related information"""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ally', help='Description Slug')
    async def ally(self, ctx: commands.Context, ally: str):
        """Longer DocString should be Longer"""
        ally = ally.lower()

        if ally == "annie":
            output = """
            Annie can be found in the B-Rank Gen mission Proctor a Chunin Exam. She teaches one jutsu and has 2 team templates at Level 1."""
        elif ally == "billy2":
            output = ""
        elif ally == "billy2":
            output = ""
        await ctx.send(str(output))
        print("Ally Shenanigans!")

def setup(bot: commands.Bot):
    bot.add_cog(ally(bot))

