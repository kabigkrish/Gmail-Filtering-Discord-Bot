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
@client.event
async def on_ready(): 
    channel = client.get_channel(842160648058306593) #  Gets channel from internal cache
    await channel.send("hello world")
    await channel.send(file=discord.File("gmail.pdf"))
client.run(os.getenv('token'))
