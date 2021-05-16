import gmailapicall
import discord
import os
import mail_to_pdf
from dotenv import load_dotenv
load_dotenv()
client=discord.Client()
text=gmailapicall.mainn()
print(len(text))
if(len(text)==2):
    mail_to_pdf.topdf(text[0])
else:
    mail_to_pdf.topdf(text)
#mail_to_pdf.topdf(text[0])
@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return 
    if message.content.startswith('!hello'): 
        await message.channel.send(file=discord.File('gmail.pdf'))
        # await bot.send_file(gmail,'gmail.pdf')
client.run(os.getenv('token'))
