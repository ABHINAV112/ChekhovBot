# Checkov Bot

Dockerized discord bot which runs on our custom made server. The discord bot has the following commands and is run on a specific discord channel.

## Installation

In order to run this

### python

If you have python installed, then run the following commands

```bash
pip install discord
pip install requests
```

And run the following command

```bash
python bot.py
```

### Docker

If you have docker installed, then run the following commands

```bash
docker pull abhinav112/discord-bot
docker run -d abhinav112/discord-bot
```

## Commands

### \$hello

Calls an API and delivers a simple joke

### \$current_ip

Returns the servers ip address

### \$run-option

Runs commands written into the discord channel. NOTE: no stdin should be provided anywhere as it will cause the programs not to run

#### terminal

Runs bash commands from the server

#### python

Runs python3 code from the discord server

#### c

Compiles and runs c code

#### cpp

Compiles and runs cpp code
