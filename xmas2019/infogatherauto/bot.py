import discord
import sys
import json

import colorama

colorama.init()

with open("settings.json") as f:
    SETTINGS = json.load(f)

class InfoBot(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} - bot is a member of the folling guilds")

        print(self.guilds)

        print()

        self.target_guild = None
        for guild in self.guilds:
            if guild.name == SETTINGS["target-guild-name"]:
                self.target_guild = guild

        if self.target_guild is None:
            print("The bot is not a member of the target guild. Quitting.")
            sys.exit()
        else:
            print("The bot is a member of the target guild.\nIndexing messages\n")

        for channel in self.target_guild.channels:
            if type(channel) == discord.TextChannel:

                print("Channel '{channel.name}' '{channel.topic}'")

                async for message in channel.history(limit=200):
                    if "x-mas" in message.content.lower():
                        print(colorama.Fore.GREEN + "    " + message.content + colorama.Style.RESET_ALL)
                    print(f"    {message.author.nick if type(message.author) == discord.Member else message.author.name} - {message.content}")



    async def on_message(self, message):
        # don't respond to our own messages
        if message.author == self.user:
            return

        if message.content == "prog-ping":
            await message.channel.send("prog-pong")
            print("[*] PING: responded")

        if message.content == "prog-pong":
            await message.channel.send("prog-ping")
            print("[*] PONG: responded")

client = InfoBot(activity=discord.Game(name="X-MAS{g0tch4_flag}"))
client.run(SETTINGS["discord-token"])