const Discord = require("discord.js");
const client = new Discord.Client();
const fetch = require("node-fetch");

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

async function getServerIP() {
  var requestOptions = {
    method: "GET"
  };
  let res = await fetch(
    "https://chekhov-d2823.firebaseapp.com/api/wan",
    requestOptions
  );
  let resJson = await res.json();
  // console.log(resJson);
  return resJson;
}

client.on("message", async msg => {
  console.log(msg.channel.name);
  let channelName = msg.channel.name;
  if (msg.content == "ping") {
    msg.reply("pong");
  }
  if (msg.content === "$hello") {
    if (msg.author.username == "naseer2426") {
      msg.channel.send("This is your mom, and you, you are not my baby.");
    } else {
      msg.channel.send("Hope you have a nice day!");
    }
  }

  if (msg.content === "$ip") {
    if (channelName == "server") {
      let resJson = await getServerIP();
      msg.channel.send(resJson["WAN-IP"]);
    } else {
      msg.channel.send("Command cannot be run from this channel");
    }
  }

  if (msg.content === "$run") {
  }
});

client.login("Njg2ODM4Nzc2NDU0MTg0OTgx.XmdDrA.EcXGF2vY6-vBzHKr70nbpfuadF4");
