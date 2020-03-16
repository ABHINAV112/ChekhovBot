import discord
from sys import argv
import random

client = discord.Client()
@client.event

async def on_ready():
    pass
async def background_loop():

    await client.wait_until_ready()
    channel = client.get_channel(683704977377460242)
    messages = ["Hello!", "How are you doing?", "Howdy!"]
    await channel.send(argv[1]+" has logged into the server!")
    print(random.choice(messages) +" "+ argv[1])
    await client.close()

client.loop.create_task(background_loop())
client.run("Njg2ODM4Nzc2NDU0MTg0OTgx.XmdDrA.EcXGF2vY6-vBzHKr70nbpfuadF4")