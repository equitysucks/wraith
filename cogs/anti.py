import discord
from discord.ext import commands
import random
import requests
import datetime
import pymongo
from discord.ext.commands import cooldown, BucketType
import aiohttp
import os


class anti(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.error = '<:error:995036612897554442>'
        self.success = '<:successful:995036527220510802>'
        self.color = 0x2f3136
        self.successclr = 0x43d764
        self.errorclr = 0xFF1A1A
        self.av = 'https://cdn.discordapp.com/attachments/1046007816571338792/1063772884914413598/f5c9023ededc5dda88f472d0c37e7fa7.jpg'
        print('[Status] Loaded Cog: Anti')
  
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        async for i in guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(microseconds = 0.2), action=discord.AuditLogAction.ban):
            await guild.ban(i.user, reason="[wrath anti]: banned a user")

async def setup(bot):
  await bot.add_cog(anti(bot))