import discord
import os
from discord.ext import commands
from pathlib import Path
from dotenv import load_dotenv

from datetime import datetime

# Loading Data From .env File
load_dotenv()
env_path = Path('.') / '.env'
BOTTOKEN = os.getenv("BOT_TOKEN")

# Setting Up Bot
client = commands.Bot(command_prefix = '=')

# Printing String When Bot Is Ready To Be Used
@client.event
async def on_ready():
	print('Bot is Ready')

@client.event
async def on_message(message):
    # Only Reads From Private Testing Discord and Math-UwU-and-Nitro-Channel
    #                              Priv                                           Math UWU
   
    # if message.channel.id == '829357837976076351' or message.channel.id == '784543998366842920':
    current_time = datetime.now()
    current_time = current_time.strftime("%d/%m/%Y %H:%M:%S") # Get Current Time (For Debugging)
    print('[%s] - %s sent %s' % (current_time, message.author, message.content))

@client.command()
async def wehaveawinner(ctx):
    await ctx.send('NottCurious Wins Everything!!!!!!!!!!!!!!!!!!!!')

@client.command()
async def whosadick(ctx):
    await ctx.send('Kelvin\'s a Dick!!')


# Execute Commands
client.run(BOTTOKEN)

log_txt_file.close()
