from discord.ext import commands
from dotenv import load_dotenv
import os
import requests 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
LINK = os.getenv("LINK")

bot = commands.Bot(command_prefix='!')

@bot.command(name='joy')
async def joy(ctx):
    response = requests.get(LINK)
    if response.ok:
        response = response.json()
        await ctx.send(response['message'])

bot.run(TOKEN)
