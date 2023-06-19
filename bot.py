# bot.py
import os
import time
from json import dumps
from dotenv import load_dotenv
from tinydb import TinyDB, Query
from tinydb.operations import set
import datetime
from datetime import date, datetime
import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import logging
import logging.handlers

#######################
#                     #
#    LOGGING SETUP    #
#                     #
#######################
logging.basicConfig(level=logging.DEBUG)

##################
#                #
#    DB SETUP    #
#                #
##################
db = TinyDB('db.json')
User = Query()
Event_id = Query

#####################
#                   #
#    TOKEN SETUP    #
#                   #
#####################
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN is None:
    raise EnvironmentError("No DISCORD_TOKEN Env variable found! Did you set your .env file?")

######################
#                    #
#    CLIENT SETUP    #
#                    #
######################
intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.voice_states = True

client = commands.Bot(intents=intents, command_prefix='+')
start_time = time.time()

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        logging.log(logging.DEBUG, obj.isoformat().strip('\"'))
        return obj.isoformat().strip('\"')
    raise TypeError ("Type %s not serializable" % type(obj))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="+help for help"))
    print('Bot is now online')

@client.event
async def on_resumed():
    print('Bot is resumed')

@client.event #not working right now
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
            
@client.event
async def on_voice_state_update(member, before, after):
    if not before.channel or not after.channel: #only send update if user joins or leaves channel
        if db.search((User.name == member.id) & (User.session_status == "ACTIVE")) == []: #Should only create a new DB entry of no Active session for user
            db.insert({'name': member.id, 'start_time': 0, 'end_time': 0, 'session_status': 'ACTIVE'})
            start_time = datetime.now()
            db.update(set('start_time', start_time.timestamp()), (User.name == member.id) & (User.session_status == "ACTIVE"))
        if before.channel and not after.channel:
            end_time = datetime.now()
            db.update(set('end_time',  end_time.timestamp()), (User.name == member.id) & (User.session_status == "ACTIVE"))
            db.update(set('session_status',  "TERMINATED"), (User.name == member.id) & (User.session_status == "ACTIVE"))
    else:
        pass
        
            

async def load_extensions(client : commands.Bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load_extensions(client)
        await client.start(TOKEN)
        

if __name__ == '__main__':
    asyncio.run(main())
