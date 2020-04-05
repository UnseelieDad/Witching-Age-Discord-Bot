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

@bot.command(name="hs", help="Rolls the hack and slash move from dungeon world")
async def hack_and_slash(ctx):
    
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    roll = d1 + d2

    result = f"{d1} + {d2} = {roll}:"

    if roll >= 10:
        response = f"{result}\n Deal your damage and choose one:\n - Avoid the enemy's attack\n - Deal an extra d6 damage"
    elif roll <= 9 and roll >= 7:
        response = f"{result}\n Deal your damage and the enemy makes an attack against you."
    else:
        response = f"{result}\n Miss. Mark XP"
    
    await ctx.send(response)

bot.run(TOKEN)