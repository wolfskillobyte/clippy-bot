import os
import discord
my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('shit'):
    await message.channel.send('It sounds like you are trying to do a swear. Do you need some help?')


