import os

import discord
import dotenv
import datetime
dotenv.load_dotenv()
client = discord.Client()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

Start_ID = 706779308211044352
d_now = datetime.datetime.now()


@client.event
async def greet():
    channel = client.get_channel(Start_ID)
    await channel.send("正常に起動しました")


@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)
    await greet()


@client.event
async def on_message(message):
    if message.content == "おはよう！":
        if message.channel.id == Start_ID:
            await message.channel.send(
                f'Error: ここでは実行できません\n'
                f'  Cannot perform this operation here.')
            return
        await message.channel.send(d_now.strftime(
            f'おはようございます。\n'
            f'今日の日付は%-m月%-d日です。'))

client.run(TOKEN)
