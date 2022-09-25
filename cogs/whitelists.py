import discord
from discord.ext import commands
import random
import pymongo
from unittest import skip
import requests
from discord.ext.commands import cooldown, BucketType
import aiohttp


color = 0x2f3136
success = 0xA4FF00
error = 0xFF1A1A

mongoClient = pymongo.MongoClient('mongodb+srv://sinful:khaleed111@cluster0.i8qcd.mongodb.net/?retryWrites=true&w=majority')
db = mongoClient.get_database("apollo2").get_collection("whitelist")


def is_owner(ctx):
    return ctx.message.author.id == 995021078428663889

def is_whitelisted(ctx):
    return ctx.message.author.id in db.find_one({ "guild_id": ctx.guild.id })["users"] or ctx.message.author.id == 995021078428663889
    
def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 995021078428663889


class whitelists(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["wl"])
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.check(is_whitelisted)
    async def whitelist(self, ctx, member: discord.Member = None):
        try:
            if member == None:
                await ctx.send(embed=discord.Embed(description=f"<:error:995036612897554442> **mention a user to** `whitelist`", color=error))
            if member.id in db.find_one({ "guild_id": ctx.guild.id })["users"]:
                await ctx.send(embed=discord.Embed(description=f"<:error:995036612897554442> {member.mention} **is already** `whitelisted`", color=error))
                return

            db.update_one({ "guild_id": ctx.guild.id }, { "$push": { "users": member.id }})
            await ctx.send(embed=discord.Embed(description=f"<:successful:995036527220510802> **succesfully** `whitelisted` {member.mention}", color=success))

        except Exception as e:
            await ctx.send(embed=discord.Embed(description=f"```{e}```", color=0x2f3136))



    @commands.command(aliases=["dwl"])
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.check(is_whitelisted)
    async def dewhitelist(ctx, member: discord.Member = None):
        try:
            if member == None:
                await ctx.send(embed=discord.Embed(description=f"<:error:995036612897554442> **mention a user to** `dewhitelist`", color=error))

            if member.id not in db.find_one({ "guild_id": ctx.guild.id })["users"]:
                await ctx.send(embed=discord.Embed(description=f"<:error:995036612897554442> **that user is not** `whitelisted`", color=error))
                return

            db.update_one({ "guild_id": ctx.guild.id }, { "$pull": { "users": member.id }})

            await ctx.send(embed=discord.Embed(description=f"<:successful:995036527220510802> **succesfully** `dewhitelisted` {member.mention}", color=success))
        except Exception as e:
            await ctx.send(embed=discord.Embed(description=f"```{e}```", color=0x2f3136))


    @commands.command(aliases=["wld"])
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.check(is_whitelisted)
    async def whitelisted(self, ctx):
      guild = ctx.message.guild
      if ctx.message.author.id == ctx.guild.owner.id:
        data = db.find_one({ "guild_id": ctx.guild.id })['users']
        embed = discord.Embed(title=f"whitelisted users for {ctx.guild.name}", description="\n", color=color)
        embed.set_thumbnail(url=guild.icon.url)
        for i in data:
          if self.client.get_user(i) == None:
            skip
          if self.client.get_user(i) != None:
            if self.client.get_user(i) == ctx.guild.owner:
              embed.description += f"<a:crown:1018544927447208069>・`{self.client.get_user(i)}` - `{i}`\n"
            if self.client.get_user(i) != ctx.guild.owner:
              if self.client.get_user(i).bot:
                embed.description += f"<:ClydeBot:1018545663501414501>・`{self.client.get_user(i)}` - `{i}`\n"
              else:
                embed.description += f"<:member:1017684974608064512>・`{self.client.get_user(i)}` - `{i}`\n"
        await ctx.send(embed=embed)



async def setup(bot):
  await bot.add_cog(whitelists(bot))