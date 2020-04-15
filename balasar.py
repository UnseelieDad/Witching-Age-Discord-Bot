# balasar.py

import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

# add roll better command

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

@bot.command(name="roll", aliases=["r"], help="Rolls specified dice and modifers (xdy+z)")
async def roll_dice(ctx, roll_string : str):
    
    roll_string.replace(" ", "")
    dice_number = int(roll_string[0])
    dice_type = int(roll_string[2])

    dice = []
    for die in range(0,dice_number):
        die = random.randint(1, dice_type)
        dice.append(die)
    
    total = sum(dice)
    
    dice = list(map(str, dice))
    response = "| + |".join(dice)
    response = "|" + response + "|"

    
    if len(roll_string) > 3:
        mod_sign = roll_string[3]
        modifier = int(roll_string[4])
        if mod_sign == "-":
            total -= modifier
            response += f" - {modifier}"
        elif mod_sign == '+':
            total += modifier
            response += f" + {modifier}"

    response += f"\n= {total}"

    await ctx.send(response)

bot.run(TOKEN)