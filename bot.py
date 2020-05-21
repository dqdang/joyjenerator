import discord.utils
from discord.ext import commands
import os
import requests 

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL=os.getenv('')
LINK = os.getenv("LINK")

bot = commands.Bot(command_prefix='!')

async def send_joy():
    response = requests.get(LINK)
    if response.ok:
        response = response.json()
        return response['message']
    return None

async def check_time():
    await bot.wait_until_ready()
    while not bot.is_closed:
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        now=datetime.strftime(datetime.now(),'%H:%M')
        if now == send_time:
            await bot.send_message(send_joy)
        # await asyncio.sleep(60)

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

@bot.command(name='joy')
async def joy(ctx):
    await ctx.send(send_joy())

bot.loop.create_task(check_time())
bot.run(TOKEN)
