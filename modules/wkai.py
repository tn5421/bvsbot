import time
import datetime
import discord

from discord.ext import commands

wk_list = ["Craftworld at War", "AspenStory",
        "ADAM", "FarmVale", "ForeverQuest"]

def get_rday(offsetdays=0):
  return (int((datetime.datetime.now(datetime.timezone(-datetime.timedelta(hours=5)))+datetime.timedelta(days=offsetdays)).strftime("%d")))

class wkai(commands.Cog, name="WorldKaiju"):
  """Prints relative World Kaiju summon times."""
  def init(self, bot: commands.Bot):
    self.bot = bot

  @commands.command(name='wkai', help='Prints the WorldKaiju summon for the day.')
  async def wkai(self, ctx: commands.Context):
    day_wkai = "Today's WKAI summon is a "

    wk_day = get_rday() % 5
    day_wkai += wk_list[wk_day]

    await ctx.send(day_wkai)
    print("Client should have posted today's WKAI")

  @commands.command(name='cow', help='Prints the next time a Craftworld of War can be summoned.')
  async def cow(self, ctx: commands.Context):
    for offset in range(1,10):
      if (get_rday(offset) % 5 == 0):
        cow_wkai = "The next Craftworld of War summoning is in {0} Day(s)".format(offset)
        break
    await ctx.send(cow_wkai)
    print("Client should have posted next CoW WKAI")

  @commands.command(name='aspen', help='Prints the next time an AspenStory can be summoned.')
  async def aspen(self, ctx: commands.Context):
    for offset in range(1,10):
      if (get_rday(offset) % 5 == 1):
        aspen_wkai = "The next AspenStory summoning is in {0} Day(s)".format(offset)
        break
    await ctx.send(aspen_wkai)
    print("Client should have posted next Aspen WKAI")

  @commands.command(name='adam', help='Prints the next time an ADAM can be summoned.')
  async def adam(self, ctx: commands.Context):
    for offset in range(1,10):
      if (get_rday(offset) % 5 == 2):
        adam_wkai = "The next ADAM summoning is in {0} Day(s)".format(offset)
        break
    await ctx.send(adam_wkai)
    print("Client should have posted next ADAM WKAI")

  @commands.command(name='farm', help='Prints the next time a FarmVale can be summoned.')
  async def farm(self, ctx: commands.Context):
    for offset in range(1,10):
      if (get_rday(offset) % 5 == 3):
        farm_wkai = "The next FarmVale summoning is in {0} Day(s)".format(offset)
        break
    await ctx.send(farm_wkai)
    print("Client should have posted next FarmVille WKAI")

  @commands.command(name='fq', help='Prints the next time a ForeverQuest can be summoned.')
  async def fq(self, ctx: commands.Context):
    for offset in range(1,10):
      if (get_rday(offset) % 5 == 4):
        fq_wkai = "The next ForeverQuest summoning is in {0} Day(s)".format(offset)
        break
    await ctx.send(fq_wkai)
    print("Client should have posted next FQ WKAI")

def setup(bot: commands.Bot):
  bot.add_cog(wkai(bot))
