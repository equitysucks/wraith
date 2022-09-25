import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import requests
import math
import asyncio

color = 0x2f3136

class utility(commands.Cog):
    def __init__(self, client):
      self.client = client

    @commands.command(aliases=['av'])
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def avatar(self, ctx, *, user: discord.Member = None):
      try:
        if user is None:
          user = ctx.message.author
        embed = discord.Embed(title=f'{user.name}\'s avatar', color=color)
        embed.set_image(url=user.avatar.url)
        embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
        await ctx.send(embed=embed)

      except Exception as e:
        await ctx.send(embed=discord.Embed(description=f"```{e}```", color=0x2f3136))
      
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servericon(self, ctx):
      if ctx.guild.icon == None:
        embed = discord.Embed(title=f'`{ctx.guild.name}` **has no server icon**', color=color)
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(title=f'{ctx.guild.name}\'s icon', color=color)
        embed.set_image(url=ctx.guild.icon.url)
        embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
        await ctx.send(embed=embed)

        
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverbanner(self, ctx, member: discord.Member = None):
      try:
        if ctx.guild.banner == None:
          embed = discord.Embed(title=f'`{ctx.guild.name}` **has no server banner**', color=color)
          await ctx.send(embed=embed)
      except:
        embed = discord.Embed(title=f'{ctx.guild.name}\'s banner', color=color)
        embed.set_image(url=ctx.guild.banner.url)
        embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar.url}")
        await ctx.send(embed=embed)   

    @commands.command(aliases=['si'])
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def serverinfo(self, ctx):
      try:
          guild = ctx.message.guild
          online = len([member.status for member in guild.members
                        if member.status == discord.Status.online or
                        member.status == discord.Status.idle or member.status == discord.Status.do_not_disturb])

          total_users = len(guild.members)
          total_bots = len([member for member in guild.members if member.bot == True])
          total_humans = total_users - total_bots
          text_channels = len(ctx.guild.text_channels)
          voice_channel = len(ctx.guild.voice_channels)


          embed = discord.Embed(colour=color)
          embed.add_field(name="<a:crown:1018544927447208069> **Owner**", value=f"`{str(guild.owner)}`")
          embed.add_field(name="<a:boost:1018545023446421504> **Boosts**", value=f"`{guild.premium_subscription_count}`")
          embed.add_field(name="<:roles:1018545308868813021> **Roles**", value=f"`{len(guild.roles)}`")
          embed.add_field(name="<:member:1017684974608064512> **Members**", value="<:online:1018545518395273328> `{}` **|** `{}`".format(online, total_users))
          embed.add_field(name=":man_standing: **Humans**", value=f"`{total_humans}`")
          embed.set_thumbnail(url=ctx.guild.icon.url)
          embed.add_field(name="<:ClydeBot:1018545663501414501> **Bots**", value=f"`{total_bots}`")
          embed.add_field(name="<:chanwhite:1018545884646088824> **Text Channels**", value=f"`{text_channels}`")
          embed.add_field(name="<:ChannelVC:1018545842682073139> **Voice Channels**", value=f"`{voice_channel}`")
          embed.set_author(name=guild.name, url=guild.icon.url)
          embed.set_thumbnail(url=guild.icon.url)
          await ctx.send(embed=embed)
      except Exception as e:
        await ctx.send(embed=discord.Embed(title="Exception", description=f"```{e}```", color=0x2f3136))



    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def poll(self, ctx, *, message):
      await ctx.message.delete()
      message = await ctx.send(f"```{message} | {ctx.message.author}```")
      await message.add_reaction('<:successful:995036527220510802>')
      await message.add_reaction('<:error:995036612897554442>')

    @commands.command(aliases=['mc'])
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def membercount(self, ctx):
      embed = discord.Embed(description=f"<:member:1017684974608064512> `{ctx.guild.name}` **has** `{ctx.guild.member_count}` **members**", color=color)
      await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def emoji(self, ctx, emoji: discord.Emoji):
        await ctx.send(embed=discord.Embed(description="**Emoji:** %s\n**ID:**  `%s`" % (emoji, emoji.id), color=color))
    

    @commands.command(aliases=["invs"])
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def invites(self, ctx, member: discord.Member = None):
        totalInvites = 0
        if member == None:
            member = ctx.author
        for i in await ctx.guild.invites():
            if i.inviter == member:
                totalInvites += i.uses
        if member == ctx.author:
             embed = discord.Embed(description="<:member:1017684974608064512> **you've invited** `%s` **member(s) to the server**" % (totalInvites), color=color)
        else:
            embed = discord.Embed(description="<:member:1017684974608064512> `%s` **has invited** `%s` **member(s) to the server**" % (member.name, totalInvites), color=color)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
      await member.add_roles(role)
      await ctx.send(embed=discord.Embed(description=f"<:successful:995036527220510802> **succesfully added** `{role.name}` **to** `{member.name}`", color=color))

    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def derole(self, ctx, member: discord.Member, role: discord.Role):
      await member.remove_roles(role)
      await ctx.send(embed=discord.Embed(description=f"<:successful:995036527220510802> **succesfully removed** `{role.name}` **from** `{member.name}`", color=color))

    @commands.command(aliases=["eadd"])
    @commands.cooldown(1, 8, commands.BucketType.channel)
    @commands.has_permissions(manage_emojis=True)
    async def emojiadd(self, ctx, emote):
        try:
            if emote[0] == '<':
                name = emote.split(':')[1]
                emoji_name = emote.split(':')[2][:-1]
                anim = emote.split(':')[0]
                if anim == '<a':
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
                else:
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
                try:
                    response = requests.get(url) 
                    img = response.content
                    emote = await ctx.guild.create_custom_emoji(name=name, image=img) 
                    return await ctx.send(embed=discord.Embed(description="<:successful:995036527220510802> **succesfully added** \"%s\"" % (emote), color=color))
                except Exception:
                    return await ctx.send(embed=discord.Embed(description=f"<:error:995036612897554442> **failed to add emoji**", color=color))
            else:
                return await ctx.send(embed=discord.Embed(description=f"<:error:995036612897554442> **invalid emoji**", color=color))
        except Exception:
            return await ctx.send(embed=discord.Embed(description=f"<:error:995036612897554442> **failed to add emoji**", color=color))



async def setup(bot):
  await bot.add_cog(utility(bot))
