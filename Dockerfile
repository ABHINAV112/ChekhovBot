FROM naseer2426/gl-dep

WORKDIR /usr/src/discord-bot

COPY . .

RUN python3 -m pip install -U discord.py
RUN pip3 install requests

CMD [ "python3","bot.py" ]