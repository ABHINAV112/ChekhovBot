import discord
import requests
from discord.ext import commands, tasks

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.private_channels)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        # print(message.author)
        
        author = str(message.author).split("#")[0]
        url = "https://insult.mattbas.org/api/insult.txt?who={}".format(author)
        payload = {}
        headers= {}
        response = requests.request("GET", url, headers=headers, data = payload)
        # output = response.json()["insult"]
        output = response.text
        await message.channel.send(output)
    if message.content.startswith("$current_ip"):
        url="https://chekhov-d2823.firebaseapp.com/api/wan"
        payload = {}
        headers= {}
        response = requests.request("GET", url, headers=headers, data = payload).json()
        output = ""
        for key in response:
            output+=key+" : "+response[key]+'\n'
        await message.channel.send(output)


client.run('Njg2ODM4Nzc2NDU0MTg0OTgx.XmdDrA.EcXGF2vY6-vBzHKr70nbpfuadF4')