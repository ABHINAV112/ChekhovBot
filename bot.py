import discord
import requests
from discord.ext import commands, tasks
from Run_Code import execute_command
from config import BOT_TOKEN
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
        if str(message.channel) == "server" and str(message.author).startswith("abhinav"):
            command = message.content.split("\n")[0]
            if("-" not in command):
                await message.channel.send("The run command must be of the from \"$run-option\"")
                return
            
            option = command.split("-")[-1]
            instructions = '\n'.join(message.content.split("\n")[1:])

            option_list = {"terminal","python","cpp","c"}
            if(option not in option_list):
                await message.channel.send("Invalid option")
                return
            if(instructions==""):
                await message.channel.send("Invalid instructions")
                return


            output = execute_command(option,instructions)
            print(len(output))
            if(len(output)<=2000):
                await message.channel.send(output)
            else:
                text_file = open("output/output.txt", "w")
                text_file.write(output)
                text_file.close()
                await message.channel.send(file=discord.File('output/output.txt'))            

        else:
            await message.channel.send("You cannot use the $run command from this channel")


client.run(BOT_TOKEN)