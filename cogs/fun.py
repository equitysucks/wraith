import discord
from discord.ext import commands
import random
import asyncio
import requests
from discord.ext.commands import cooldown, BucketType
import aiohttp

color = 0x2f3136

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.av = 'https://cdn.discordapp.com/attachments/1046007816571338792/1063772884914413598/f5c9023ededc5dda88f472d0c37e7fa7.jpg'
        print('[Status] Loaded Cog: Fun')
        
    
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


    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def hack(self, ctx, *, member: discord.Member):
      responses = [
        f"{member.name}@fatgmail.com", f"{member.name}@hotmom.com",
        f"{member.name}@gaylord.com", f"{member.name}@gaymail.com"
        f"{member.name}@hentaimaster.com"
    ]

      password = [
        f"gaymailxoxo", f"{member.name}isgayxo", f"imabitch",
        f"bigdick{member.name}"
      ]
      websites = [
        f"fatbitchesfightingoverfood.com",
        f"ilovehentai.com",
        f"daddykhai.kh",
    f"stopchangingyournameproxyorsinful.com",
        f"https://www.pornhub.com/home/search/gay", f"bigfreecocks.com",         f"howtomakeyourpplarger.com"
      ]
      ipaddy = [f"135.791.113", f"123.456.789", f"987.654.321", f"696.969.690"]
      msgs = [
        f"Why is my dick so little?", f"How do I tell my friends I'm gay",
        f"I'm stuck inside the washing machine", f"khai is so hot damn", f"Send nudes", "I'm gay"
      ]
      messags = [
        f"Gay", f"Cock", f"Fuck", f"khai >>>", f"we love khai",
f"fatbitchesfightingoverfood", "Fap", "OOP"
      ]
      if member == ctx.message.author:
        emb = discord.Embed(color=color,
                            description="<:error:995036612897554442> **you cannot hack yourself.**")
        emb.set_author(
            name='error : author',
            icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=emb)
        return

      if member == member.id:
        member = member
      message = await ctx.send(f"```hacking {member.name}```")
      await asyncio.sleep(3)
      await message.edit(content=f"```finding {member.name}'s discord info..```")
      asyncio.sleep(3)
      await message.edit(content=f"```cracking {member.name}'s login info..```")
      await asyncio.sleep(2)
      await message.edit(content=f"```information now being leaked..```")
      await asyncio.sleep(2)
      await message.edit(
        content=
        f"```・email: {random.choice(responses)}\n・password: {random.choice(password)}```"
    )
      await asyncio.sleep(2)
      await message.edit(
          content=f"finding {member.name}'s most recent websites..")
      await asyncio.sleep(2)
      await message.edit(content=f"{random.choice(websites)}")
      await asyncio.sleep(2)
      await message.edit(content=f"```searching for {member.name}'s ip addy..```")
      await asyncio.sleep(2)
      await message.edit(content=f"```found {member.name}'s ip addy```")
      await asyncio.sleep(2)
      await message.edit(content=f"```ip addy: {random.choice(ipaddy)}```")
      await asyncio.sleep(3)
      await message.edit(content="```finding most used word..```")
      await asyncio.sleep(2)
      await message.edit(content=f"```found {member.name}'s most common word```")
      await asyncio.sleep(2)
      await message.edit(content=f"```most common words: {random.choice(msgs)}```")
      await asyncio.sleep(3)
      await message.edit(content="```finding most recent word..```")
      await asyncio.sleep(2)
      await message.edit(content=f"```found {member.name}'s most recent word```")
      await asyncio.sleep(2)
      await message.edit(content=f"```most recent word: `{random.choice(messags)}```")
      await asyncio.sleep(2)
      await message.edit(content=f"```selling {member.name}'s cc details```")
      await asyncio.sleep(2)
      await message.edit(content=f"```hacked {member.name}```")



    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def randnum(self, ctx):
      embed = discord.Embed(description=f'`{(random.randint(1, 101))}`',color=color)
      await ctx.send(embed=embed)


async def setup(bot):
  await bot.add_cog(fun(bot))
