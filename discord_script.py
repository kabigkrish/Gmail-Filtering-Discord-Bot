import time
import gmailapicall
import discord
import os
import mail_to_pdf
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()
client.run(os.getenv('token'))
client.close()
print('start')
text = gmailapicall.mainn()
print(len(text))
if(len(text) == 2):
    mail_to_pdf.topdf(text[0])
else:
    mail_to_pdf.topdf(text)


def restart():
    import sys
    print("argv was", sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")

    os.execv(sys.executable, ['python'] + sys.argv)


@client.event
async def on_ready():
    # Gets channel from internal cache
    channel = client.get_channel(842160648058306593)
    await channel.send("hello world")
    await channel.send(file=discord.File("gmail.pdf"))
print('stop')
time.sleep(2)
restart()


# https://stackoverflow.com/questions/50957031/how-to-make-discord-py-bot-run-forever-if-client-run-returns
# MIGHT HELP
