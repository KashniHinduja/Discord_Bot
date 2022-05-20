import discord
import random

TOKEN = "OTU1ODg3MjU0NjcxMzU2MDA0.YjoNYQ.t4xQyO30_9vh9QdoYS-qMlzzbk4"

client = discord.Client()


@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.channel.name == "general":
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}!")
            return
        
        elif user_message.lower() == "help":
            await message.channel.send("nope")
            return


client.run(TOKEN)
