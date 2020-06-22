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

@bot.command(name='admins', help='List all Admins', pass_context=True)
async def admins(ctx):
    onlineusers= []
    server = ctx.message.guild
    role_name = ('Admin')
    role_id = server.roles[0]
    await ctx.send('Admins Online: ')
    for role in server.roles:
      if role_name == role.name:
        role_id = role
        break
    else:
      await ctx.send("Role doesn't exist")
      return
    for member in server.members:
      if role_id in member.roles:
        if member.status == discord.Status.online:
          await ctx.send("```" + f"{member.name}" + "```")
@client.event #not working right now
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


bot.load_extension("cogs.internalcommands")
bot.run(TOKEN)
