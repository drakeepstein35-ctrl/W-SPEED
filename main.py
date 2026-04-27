import discord
import os
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1462125650767904768

intents = discord.Intents.default()
client = discord.Client(intents=intents)

count = 1

@tasks.loop(minutes=1)
async def send_count():
    global count
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(str(count))
        count += 1

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    send_count.start()

client.run(TOKEN)
