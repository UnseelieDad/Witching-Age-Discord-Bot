# balasar.py

import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command(name="d6", help="Rolls a d6")
async def d6(ctx):
    response = random.choice(range(1,7))
    await ctx.send(response)

bot.run(TOKEN)