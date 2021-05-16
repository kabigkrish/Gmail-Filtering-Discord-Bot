import gmailapicall
import discord
import os
from dotenv import load_dotenv
load_dotenv()
client=discord.Client()

out=gmailapicall.mainn()
oo=str(out[0])
sizee=len(str(oo))

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return 
    if message.content.startswith('!hello'):
        for i in range(0,sizee,2001):
            await message.channel.send(oo[i:i+2000]) 

client.run(os.getenv('token'))
