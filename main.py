import discord
import os
from discord.ext import commands
from pathlib import Path
from dotenv import load_dotenv

# Loading Data From .env File
load_dotenv()
env_path = Path('.') / '.env'
api_key = os.getenv("API_KEY")
BOTTOKEN = os.getenv("BOT_TOKEN")

# Setting Up Bot
client = commands.Bot(command_prefix = '=')

# Printing String When Bot Is Ready To Be Used
@client.event
async def on_ready():
	print('Bot is Ready')

@client.command()
async def wehaveawinner():
    print('NottCurious Wins Everything!!!!!!!!!!!!!!!!!!!!')

@client.command()
async def whosadick(ctx):
    await ctx.send('Kelvin\'s a Dick!!')

# Execute Commands
client.run(BOTTOKEN)