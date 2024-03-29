#internalcommands.py
import os
import time
from discord.ext import commands
import discord
import logging
from datetime import datetime, timedelta
from tinydb import TinyDB, Query
from discord import client
from discord.utils import get
start_time = time.time()

db = TinyDB('db.json')
User = Query()
logging.basicConfig(level=logging.DEBUG)

class Stats(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot

    @commands.command(name='stats', help='Get Stats on a user')
    async def status(self, ctx:commands.context.Context, arg):
        member_id = arg
        ret_list = db.search((User.name == int(member_id)))
        time_sum = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        for instance in ret_list:
            logging.log(logging.DEBUG, instance)
            start_time = datetime.fromtimestamp(instance["start_time"])
            if instance['session_status'] == "TERMINATED":
                end_time = datetime.fromtimestamp(instance["end_time"])
            else:
                end_time = datetime.now()
            time_sum += self.find_time_diff(start_time, end_time)
        user = self.bot.get_user(int(member_id))
        await ctx.send(f"```User Summary:\nUser Name: {user.global_name}\nTime Online: {time_sum}\n```")
        
    def find_time_diff(self, start_time : datetime, end_time : datetime) -> timedelta:
        diff = end_time - start_time
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return timedelta(days=days, seconds=seconds, microseconds=0, milliseconds=0, minutes=minutes, hours=hours, weeks=0)
    
                

async def setup(bot):
    await bot.add_cog(Stats(bot))




