import discord
from discord.ext import commands

#how to call the bot to run a command
client = commands.Bot(command_prefix = "!")

@client.event

#when the bot successfully gathers all info
async def on_ready():
	print("bot is ready")

#calls Controller
client.run('NzY4ODgyMDQ4MDcyMDI0MDk3.X5G7NQ.h0ShLojdiDCAeium9MSot461TRY')