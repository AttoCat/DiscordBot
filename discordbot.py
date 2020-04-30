import discord
import dotenv
import os

dotenv.load_dotenv()
client = discord.Client()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")


@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

client.run(TOKEN)
