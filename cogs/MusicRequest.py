#internalcommands.py
import os
import time
import datetime
from discord.ext import commands

start_time = time.time()
class MusicRequest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pull', help='Pull Hydra to your currect VC')
    async def status(self, ctx, arg1):
        if lower(arg1) == "lofi":
            await ctx.sned("Pulling LoFi Radio to your current VC")
        elif lower(arg1) == "synthwave":
            await ctx.send("Pulling Synthwave Radio to your current VC")
        else:
            await ctx.send("The current Radio stations you can pull are:\n Synthwave\n LoFi\n ")
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(MusicRequest(bot))

