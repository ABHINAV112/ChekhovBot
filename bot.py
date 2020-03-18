import discord
import requests
import traceback
from discord.ext import commands, tasks
from runDisc import execAndTrackError
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
        if str(message.channel) == "server":
            url="https://chekhov-d2823.firebaseapp.com/api/wan"
            payload = {}
            headers= {}
            response = requests.request("GET", url, headers=headers, data = payload).json()
            output = ""
            for key in response:
                output+=key+" : "+response[key]+'\n'
            await message.channel.send(output)
        else:
            await message.channel.send("You cannot use the $current_ip command from this channel")

    if message.content.startswith("$run"):
        if str(message.channel) == "server":

            exc,inf = execAndTrackError("\n".join(message.content.split("\n")[1:]))
            if inf:
                trace = "".join([traceback.format_exception(*inf)[0]]+traceback.format_exception(*inf)[2:])
                await message.channel.send(trace)
            else:
                if exc:
                    await message.channel.send(exc)
                else:
                    await message.channel.send("The program did not write any text to stdout")

        else:
            await message.channel.send("You cannot use the $run command from this channel")


client.run('Njg2ODM4Nzc2NDU0MTg0OTgx.XmdDrA.EcXGF2vY6-vBzHKr70nbpfuadF4')