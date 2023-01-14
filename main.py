import discord
import random
import inspect
import requests
import urllib
import datetime
import asyncio
import os
import json
import sqlite3
import ast


from time import sleep
from discord import app_commands
from discord.ext import commands, tasks
from unittest import skip



color = 0x2f3136
client = commands.Bot(commands.when_mentioned_or(";"), intents=discord.Intents.all())
client.remove_command("help")


"""Loading Cogs"""
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


"""Function To Load Databases"""
def loadDBs():
    """Loading Economy Database"""
    db = sqlite3.connect("eco.sqlite")
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS main 
    (user_id INTEGER, wallet INTEGER, bank INTEGER)''')
    print('[Status] Connected to Economy DB')

    """Loading Main Database"""
    db2 = sqlite3.connect("main.sqlite")
    cursor = db2.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS main 
    (guild_id INTEGER, msg TEXT, channel_id INTEGER)''')
    print('[Status] Connected to Main DB')

    """Loading Levels Database"""
    db3 = sqlite3.connect("levels.sqlite")
    cursor = db3.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS main 
    (level INTEGER, xp INTEGER, user INTEGER, guild_id INTEGER)''')
    print('[Status] Connected to Levels DB')


"""Event To Notify When Added To A Channel"""
@client.event 
async def on_guild_join(guild):
      channel = guild.text_channels[0]
      channellol = client.get_channel(1063881152831705250)
      invlink = await channel.create_invite(unique=True)
      await channellol.send(embed=discord.Embed(description=f"<a:Black_World:1018544976260517948> **i have been added to:** `{guild.name}` **|** `{guild.id}` **|** `{guild.owner.name}`", color=color))
      await channellol.send(f"{invlink}")


"""On Ready Event To Notify When Bot Is Online"""
@client.event
async def on_ready():
    loadDBs()
    channel = client.get_channel(1063881152831705250)
    lat = int(client.latency * 1000)
    if lat > 100:
        emoji = '<:8920theconnectionisbad:1045747873595281408>'
    elif lat < 30:
        emoji = '<:7431theconnectionisexcellent:1020011599085449309>'
    await channel.send(embed=discord.Embed(description=f"<a:Black_World:1018544976260517948>  `wrath` **is online and running on** {emoji} `{lat} ms` ", color=color))
    #await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.competing,name=f"{len(client.guilds)} Guilds"))
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing,name=f"being rewritten"))
    print("wrath is online")

async def main(): 
    await load()
    await client.start('MTAyNzYyNzU2Njk2MzYyMTg5OA.Gq3qQ_.COcQrNZt8bZy9VkxBRH9ZN4UvIw08TYPwRDkmg')

asyncio.run(main())
