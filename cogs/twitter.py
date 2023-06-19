#internalcommands.py
import os
import time
import datetime
from discord.ext import commands

class Twitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='Tweet', help='Send out a tweet')
    async def Calendar(self, ctx, string="EI0Fa5ujzE"):
        if string == "EI0Fa5ujzE":
            optionsScreen = "```Here are the commands you can use:\n +Twitter tweet <Tweet Text>```"
            await ctx.send(optionsScreen)
            
            
async def setup(bot):
    await bot.add_cog(Twitter(bot))
