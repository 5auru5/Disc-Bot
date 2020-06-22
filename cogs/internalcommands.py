#internalcommands.py
import os
import time
import datetime
from discord.ext import commands

start_time = time.time()
class InternalCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Status', help='Status command to see if bot is working')
    async def test(self, ctx):
        test_reply = "```bash\nThe Bot is \"online\" and currently working```"

        response = test_reply
        await ctx.send(response)
    @commands.command(name='uptime', help='See current bot uptime')
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        await ctx.send("Current Uptime: " + text)

def setup(bot):
    bot.add_cog(InternalCommands(bot))




