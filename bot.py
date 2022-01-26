import discord
import logging
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('token')

logging.basicConfig(level=logging.INFO)

# Writes logs to a file called discord.log 
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# create instance of a client
client = discord.Client()

# decorator to register an event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # ignore messages from ourselves
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# run bot with token
client.run(TOKEN)