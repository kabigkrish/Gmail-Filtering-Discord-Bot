import gmailapicall
import discord
import os
from dotenv import load_dotenv
load_dotenv()
client=discord.Client()

out=gmailapicall.mainn()
oo=str(out[0])
sizee=len(str(oo))

from fpdf import FPDF
# save FPDF() class into a 
# variable pdf
pdf = FPDF()
  
# Add a page
pdf.add_page()
  
# set style and size of font 
# that you want in the pdf
pdf.set_font("Arial", size = 15)
  
# create a cell
pdf.multi_cell(0, 2, txt = str(out[0]),align='L')
  
# add another cell
pdf.cell(200, 10, txt = "A Computer Science portal for geeks.",
         ln = 2, align = 'C')
  
# save the pdf with name .pdf
pdf.output("GFG.pdf")   
# @client.event
# async def on_ready():
#     print("we have logged in as {0.user}".format(client))

# @client.event
# async def on_message(message):
#     if message.author==client.user:
#         return 
#     if message.content.startswith('!hello'):
#         for i in range(0,sizee,2001):
#             await message.channel.send(oo[i:i+2000]) 

# client.run(os.getenv('token'))
