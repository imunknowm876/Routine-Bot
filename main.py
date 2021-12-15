import discord
import os
from datetime import datetime
import string
import json

# my_secret=os.environ['TOKEN']
f = open('routine.json')
data = json.load(f)


client=discord.Client();
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    curr_date =datetime.today().strftime('%A').lower()
    if message.author==client.user:
        return
    if message.content.startswith('$sch'):
        await message.channel.send(data[curr_date])

client.run('OTIwNTcwMjk3NzY0MTc1OTAy.YbmR5g.gSyv8aTkZODtvd5wZfrBC26ph_8')
# client.run(my_secret)




