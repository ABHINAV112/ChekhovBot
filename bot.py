import discord
import requests






client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

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
        print(output)
        await message.channel.send(output)

client.run('Njg2ODM4Nzc2NDU0MTg0OTgx.XmdDrA.EcXGF2vY6-vBzHKr70nbpfuadF4')