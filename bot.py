import asyncio
from datetime import datetime
import discord
from discord.ext import commands
import os
import requests 

# from dotenv import load_dotenv
# load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv("DISCORD_SERVER")
LINK = os.getenv("LINK")

client = discord.Client()

def send_joy():
    response = requests.get(LINK)
    if response.ok:
        response = response.json()
        return response['message']
    return None

async def check_time():
    await client.wait_until_ready()
    channel = client.get_channel(712826642493472832)
    while not client.is_closed():
        await channel.send(send_joy())
        await asyncio.sleep(3600 * 2) # every 2 hours

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!joy':
        await message.channel.send(send_joy())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(check_time())
client.run(TOKEN)
