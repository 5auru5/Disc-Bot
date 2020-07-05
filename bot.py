# bot.py
import os
import time
import psutil
import datetime
import discord
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='+')
start_time = time.time()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="+help for help"))
    print('Bot is now online')

@bot.event
async def on_resumed():
    print('Bot is resumed')

@client.event #not working right now
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


bot.load_extension("cogs.internalcommands")
bot.load_extension("cogs.GoogleServices")
bot.load_extension("cogs.Twitter")
bot.run(TOKEN)
