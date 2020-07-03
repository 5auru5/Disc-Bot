#internalcommands.py
import os
import time
import datetime
from discord.ext import commands

class GoogleServices(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Calendar', help='Create and manage Google Calendar events')
    async def Calendar(self, ctx, string):
        await ctx.send("This command is being configured")
    
    @commands.command(name='CreateDoc', help='Create a new Google Doc')
    async def CreateDoc(self, ctx, string):
        await ctx.send("This command is being configured")

    @commands.command(name='CreateSheet', help='Create a new Google Sheet')
    async def CreateSheet(self, ctx, string):
        await ctx.send("This command is being configured")
    
    @commands.command(name='CreateSlide', help='Create a new Google Slide')
    async def CreateSlide(self, ctx, string):
        await ctx.send("This command is being configured")
def setup(bot):
    bot.add_cog(GoogleServices(bot))




