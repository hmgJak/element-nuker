import discord
from discord.ext import commands
import colorama
from colorama import Fore as C

token = input("Token:")
intents = discord.Intents.all()
client = commands.Bot(
  command_prefix='!',
  intents=intents,
  help_command=None
)

@client.event
async def on_connect():
  try:
    for guild in client.guilds:
      invite = await guild.invites()
      if not invite:
        try:
          invite = await guild.text_channels[0].create_invite()
          print(f"""
Bot: {client.user}
Servers: {guild}
Links: {invite}
Membercount: {guild.membercount}""")
        except discord.Forbidden:
          invite = await guild.invites()
          print(f"""
Bot: {client.user}
Servers: {guild}
Links: {invite}
""")
  except Exception as e:
    print(f"{C.RED}{e}")

try:
  client.run(token) 
except Exception as e:
  print(f"{C.RED}{e}")
except discord.Error.HTTPException:
  print(f"{C.RED} Network Error")
