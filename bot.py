import discord
from discord.ext import commands

#how to call the bot to run a command
client = commands.Bot(command_prefix = "!")

@client.event

#asyncronous function - (you don't have to wait for it to finish. Once it's started, you can go back to something else) when the bot successfully gathers all info
async def on_ready():
	print("bot is ready")

@client.command()
async def WLR(context):
	await context.send("T__T Rokkstar++ MaDe !! </33")

@client.event
async def on_member_join(member):
	print(f"{member} made it in...")

@client.event
async def on_member_remove(member):
	print(f"Smell ya later {member}!")

#calls Controller
client.run('NzY4ODgyMDQ4MDcyMDI0MDk3.X5G7NQ.xFpgfH-0IpJNTAJKRpBMmZeX3wQ')
#might have to change token every upload
