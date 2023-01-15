from cgitb import text
import discord
from discord.ext import commands
import os
import datetime
import sqlite3
import random
import time


def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 995021078428663889

class levels(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.error = '<:error:995036612897554442>'
        self.success = '<:successful:995036527220510802>'
        self.color = 0x2f3136
        self.successclr = 0x43d764
        self.errorclr = 0xFF1A1A
        self.av = 'https://cdn.discordapp.com/attachments/1046007816571338792/1063772884914413598/f5c9023ededc5dda88f472d0c37e7fa7.jpg'
        print('[Status] Loaded Cog: Levels')

    @commands.Cog.listener()
    async def on_message(self, message):
      try:
        db = sqlite3.connect('levels.sqlite')
        cursor = db.cursor()

        author = message.author
        guild = message.guild
        cursor.execute('SELECT xp FROM main WHERE user = ? and guild_id = ?', (author.id, guild.id, ))
        xp = cursor.fetchone()
        cursor.execute('SELECT level FROM main WHERE user = ? AND guild_id = ?', (author.id, guild.id,))
        level = cursor.fetchone()

        if not xp or not level:
          cursor.execute("INSERT INTO main (level, xp, user, guild_id) VALUES (?, ?, ?, ?)", (0, 0, author.id, guild.id))

        try:
          xp = xp[0]
          level = level[0]
        except TypeError:
          xp = 0
          level = 0
        if level < 5:
          xp += random.randint(1, 3)
          cursor.fetchone("UPDATE main SET xp = ? WHERE user = ? AND guild_id = ?", (xp, author.id, guild.id))
        else:
          rand = random.randint(1, (level//4))
          if rand == 1:
            xp += random.randint(1, 3)
            cursor.fetchone("UPDATE main SET xp = ? WHERE user = ? AND guild_id = ?", (xp, author.id, guild.id))
        if xp >= 2:
          level += 1
          cursor.fetchone("UPDATE main SET level = ? WHERE user = ? AND guild = ?", (level, author.id, guild.id, ))
          cursor.fetchone("UPDATE main SET xp = ? WHERE user = ? AND guild = ?", (0, author.id, guild.id))
          await message.reply(embed=discord.Embed(color=self.color, description=f'<:9803upvoteicon:1053036284823740616> {author.mention} **has leveled up** `{level}`'))
          db.commit()
          cursor.close()
          db.close()
      except Exception as e:
        print(e)


async def setup(bot):
  await bot.add_cog(levels(bot))
