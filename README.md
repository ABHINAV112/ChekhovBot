# Checkov Bot

Dockerized discord bot which runs on our custom made server. The discord bot has the following commands and is run on a specific discord channel.

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
