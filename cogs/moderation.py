import discord
from discord.ext import commands
import random
import requests
import pymongo
from discord.ext.commands import cooldown, BucketType
import aiohttp
import asyncio

color = 0x2f3136
success = 0xA4FF00
error = 0xFF1A1A

mongoClient = pymongo.MongoClient('mongodb+srv://sinful:khaleed111@cluster0.i8qcd.mongodb.net/?retryWrites=true&w=majority')
db = mongoClient.get_database("apollo2").get_collection("whitelist")

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1,5, commands.BucketType.user)
    async def lock(self, ctx, channel: discord.TextChannel = None):

        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(title='', description=f'<:successful:995036527220510802>  {ctx.author.mention} **succesfully locked** `{ctx.channel.name}`', color=success)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1,5, commands.BucketType.user)
    async def unlock(self, ctx, channel: discord.TextChannel = None):

        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(title='', description=f'<:successful:995036527220510802>  {ctx.author.mention} **succesfully unlocked** `{ctx.channel.name}`', color=success)
        await ctx.send(embed=embed)

    @commands.command(aliases=["offsm"])
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def offslowmode(self, ctx):
        await ctx.channel.edit(slowmode_delay=0)
        embed = discord.Embed(title='', description=f'<:successful:995036527220510802>  {ctx.author.mention} **succesfully turned off channel slowmode**', color=success)
        await ctx.send(embed=embed)


    @commands.command(aliases=["sm","slowmode"])
    @commands.has_permissions(manage_channels=True)
    async def setslowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(title='', description=f'<:successful:995036527220510802>  {ctx.author.mention} **succesfully set channel slowmode to** `{seconds}s`', color=success)
        await ctx.send(embed=embed)

    @commands.command(aliases=["rape", "nig", "b"])
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1,5, commands.BucketType.user)
    async def ban(self, ctx, member:discord.Member=None):
        if member == None:
            embed = discord.Embed(description=f"<:error:995036612897554442>  {ctx.author.mention} **please mention a user to ban.**" ,color=error)
            await ctx.send(embed=embed)
        await member.ban()
        embed = discord.Embed(title='', description=f'<:successful:995036527220510802>  {ctx.author.mention} **succesfully banned** `{member}`', color=success)
        await ctx.send(embed=embed)
  


    @commands.command(aliases=["k"])
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1,5, commands.BucketType.user)
    async def kick(self, ctx, member:discord.Member=None):
        if member == None:
            embed = discord.Embed(description=f"<:error:995036612897554442>  {ctx.author.mention} **please mention a user to kick.**" ,color=error)
            await ctx.send(embed=embed)
        await member.kick()
        embed = discord.Embed(title='', description=f'<:successful:995036527220510802>  {ctx.author.mention} **succesfully kicked** `{member}`', color=success)
        await ctx.send(embed=embed)



    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def nuke(self, ctx):
        channel_info = [ctx.channel.category, ctx.channel.position]
        await ctx.channel.clone()
        await ctx.channel.delete()
        embed=discord.Embed(description=f'<:successful:995036527220510802>  {ctx.author.mention} **succesfully nuked** `{ctx.channel.name}`',color=success)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1020365855789432923/1021090139423903924/giphy.gif")
        new_channel = channel_info[0].text_channels[-1]
        await new_channel.edit(position=channel_info[1])
        await new_channel.send(embed=embed)



    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def unban(self, ctx, userid):
        user = discord.Object(id=userid)
        await ctx.guild.unban(user)
        em = discord.Embed(description=f'<:successful:995036527220510802>  {ctx.author.mention} **succesfully unbanned** `{userid}`', color=success)
        await ctx.send(embed=em)



    @commands.command()
    @commands.cooldown(1,15, commands.BucketType.user)
    async def purge(ctx, amount=0):
        if amount == 0:
            embed = discord.Embed(description=f"<:error:995036612897554442>  {ctx.author.mention} **specify the amount of messages to purge.**" ,color=error)
            msg = await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=amount)
            await asyncio.sleep(3)
            embed = discord.Embed(description=f"<:successful:995036527220510802> {ctx.author.mention} **succesfully purged** `{amount}` **message(s)**",color=success, delete_after=5)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await msg.delete()



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1,15, commands.BucketType.user)
    async def clear(self, ctx, amount=0):
        if amount == 0:
            embed = discord.Embed(description=f"<:error:995036612897554442>  {ctx.author.mention} **specify the amount of messages to celear.**" ,color=error)
            msg = await ctx.send(embed=embed)
        else:
            await ctx.channel.purge(limit=amount)
            embed = discord.Embed(tdescription=f"<:successful:995036527220510802> {ctx.author.mention} **succesfully cleared** `{amount}` **message(s)**",color=success, delete_after=5)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await msg.delete()




    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1,5, commands.BucketType.user)
    async def mute(self, ctx, member: discord.Member=None, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        if member == None:
            embed = discord.Embed(description=f"<:error:995036612897554442>  {ctx.author.mention} **please mention a user to mute.**" ,color=error)
            await ctx.send(embed=embed)
            return
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in ctx.guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

        await member.add_roles(mutedRole, reason=reason)
        embed=discord.Embed(description=f"<:successful:995036527220510802> {ctx.author.mention} **succesfully muted** `{member}`", color=success)
        await ctx.message.reply(embed = embed) 



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1,5, commands.BucketType.user)
    async def unmute(self, ctx, member: discord.Member):

        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        if member == None:
            embed = discord.Embed(description=f"<:error:995036612897554442>  {ctx.author.mention} **please mention a user to unmute.**" ,color=error)
            await ctx.send(embed=embed)

        await member.remove_roles(mutedRole)
        embed=discord.Embed(description=f"<:successful:995036527220510802> {ctx.author.mention} **succesfully unmuted** `{member}`", color=success)
        await ctx.message.reply(embed = embed) 

async def setup(bot):
  await bot.add_cog(moderation(bot))