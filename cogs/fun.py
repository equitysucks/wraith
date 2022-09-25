import discord
from discord.ext import commands
import random
import requests
from discord.ext.commands import cooldown, BucketType
import aiohttp

color = 0x2f3136

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def hug(self, ctx, member: discord.Member):
      if member is None:
        embed=discord.Embed(description="<:error:995036612897554442> **input a `user` to slap.**", color=color)
        await ctx.send(embed=embed)
      else:
        hugg = requests.get("https://nekos.life/api/v2/img/hug")
        res = hugg.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **hugged** `{member.name}`", color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def slap(self, ctx, member: discord.Member=None):
      if member is None:
        embed=discord.Embed(description="<:error:995036612897554442> **input a `user` to slap.**", color=color)
        await ctx.send(embed=embed)
      else:
        slapp = requests.get("https://nekos.life/api/v2/img/slap")
        res = slapp.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **slapped** `{member.name}`",color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)



    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def kiss(self, ctx, member: discord.Member=None):
      if member is None:
        embed=discord.Embed(description="<:error:995036612897554442> **input a `user` to kiss.**", color=color)
        await ctx.send(embed=embed)
      else:
        kisss = requests.get("https://nekos.life/api/v2/img/kiss")
        res = kisss.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **kissed** `{member.name}`", color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def feed(self, ctx, member: discord.Member=None):
      if member is None:
        embed=discord.Embed(description="<:error:995036612897554442> **input a `user` to feed.**",color = color)
        await ctx.send(embed=embed)
      else:
        feedd = requests.get("https://nekos.life/api/v2/img/feed")
        res = feedd.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **fed** `{member.name}`", color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def pat(self, ctx, member: discord.Member=None):
      if member is None:
        embed=discord.Embed(description="<:error:995036612897554442> **input a `user` to pat.**", color=color)
        await ctx.send(embed=embed)
      else:
        patt = requests.get("https://nekos.life/api/v2/img/pat")
        res = patt.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **patted** `{member.name}`", color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def coinflip(self, ctx):
      choices = ["heads", "tails"]
      rancoin = random.choice(choices)
  
      embed = discord.Embed(description=f'<a:bitcoin:1018243666348884098> `{ctx.author.name}` **flipped a coin and landed on** `{rancoin}`', color=color)
      await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(fun(bot))
