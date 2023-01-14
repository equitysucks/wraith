import discord
import requests
import math
import json
import asyncio

from discord.ui import Button, View
from discord.ext.commands import cooldown, BucketType
from discord.ext import commands
from textwrap import indent
from discord import Spotify

color = 0x2f3136

class utility(commands.Cog):
    def __init__(self, client):
      self.client = client
      self.error = '<:error:995036612897554442>'
      self.success = '<:successful:995036527220510802>'
      self.color = 0x2f3136
      self.successclr = 0x2f3136
      self.errorclr = 0xFF1A1A
      self.av = 'https://media.discordapp.net/attachments/1046007816571338792/1062785924796272650/97c434fb8916fe35c113103bbd142277.jpg'
      print('[Status] Loaded Cog: Utility')

      

    @commands.command(aliases=['av'])
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def avatar(self, ctx, *, user: discord.Member = None):
      try:
        if user is None:
          user = ctx.message.author
        embed = discord.Embed(title=f'{user.name}\'s avatar', color=color)
        embed.set_image(url=user.display_avatar)
        embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=f"{ctx.author.display_avatar}")
        button = Button(label='Avatar', url=f'{ctx.author.display_avatar}', style=discord.ButtonStyle.gray)
        view = View()
        view.add_item(button)
        await ctx.reply(embed=embed, view=view)

      except Exception as e:
        await ctx.reply(embed=discord.Embed(description=f"```{e}```", color=0x2f3136))
      
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def serverid(self, ctx):
      await ctx.reply(f"> **Guild ID**: ```{ctx.guild.id}```")


    @commands.command(aliases=["memberid"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def userid(self, ctx, member:discord.Member=None):
      member = ctx.author if not member else member
      await ctx.reply(f"> **{member.name}'s ID:** ```{member.id}```")



    @commands.command(aliases=['sicon'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servericon(self, ctx):
      guild = ctx.message.guild
      try:
        if guild.icon == None:
          embed = discord.Embed(title=f'`{ctx.guild.name}` **has no server icon**', color=color)
          await ctx.send(embed=embed)
      except:
        embed = discord.Embed(title=f'{ctx.guild.name}\'s icon', color=color)
        embed.set_image(url=ctx.guild.icon)
        embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=f"{ctx.author.display_avatar}")
        button = Button(label='Icon', url=f'{ctx.guild.icon}', style=discord.ButtonStyle.gray)
        view = View()
        view.add_item(button)
        await ctx.reply(embed=embed, view=view) 
        
        
    @commands.command(aliases=['sb'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverbanner(self, ctx):
      try:
        if ctx.guild.banner == None:
          embed = discord.Embed(title=f'`{ctx.guild.name}` **has no server banner**', color=color)
          await ctx.send(embed=embed)
      except:
        embed = discord.Embed(title=f'{ctx.guild.name}\'s banner', color=color)
        embed.set_image(url=ctx.guild.banner.url)
        embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=f"{ctx.author.display_avatar}")
        button = Button(label='Banner', url=f'{ctx.guild.banner.url}', style=discord.ButtonStyle.gray)
        view = View()
        view.add_item(button)
        await ctx.reply(embed=embed, view=view) 


    @commands.command(aliases=['si'])
    @commands.cooldown(1, 3, commands.BucketType.channel)
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
          embed.add_field(name="<a:crown:1018544927447208069> **Owner**", value=f"> `{str(guild.owner)}`", inline=False)
          embed.add_field(name="<a:boost:1018545023446421504> **Boost Count**", value=f"`{guild.premium_subscription_count}`", inline=False)
          embed.add_field(name="<:roles:1018545308868813021> **Role Count**", value=f"`{len(guild.roles)}`", inline=False)
          embed.add_field(name="<:member:1017684974608064512> **Members**", value="`{}`".format(total_users), inline=False)
          embed.set_thumbnail(url=ctx.guild.icon.url)
          embed.add_field(name="<:ClydeBot:1018545663501414501> **Bots**", value=f"`{total_bots}`", inline=False)
          embed.add_field(name="<:chanwhite:1018545884646088824> **Channels**", value=f"`{text_channels}`", inline=False)
          embed.add_field(name="<:ChannelVC:1018545842682073139> **Voice Channels**", value=f"`{voice_channel}`", inline=False)
          embed.set_author(name=guild.name, url=guild.icon.url)
          embed.set_thumbnail(url=guild.icon.url)
          await ctx.reply(embed=embed)

      except Exception as e:
        print(e)


    @commands.command(aliases=['ui', 'userinfo'])
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def whois(self, ctx, member: discord.Member = None):
      if not member:  # if member is no mentioned
          member = ctx.message.author  # set member as the author

      roles = [role for role in member.roles]

      if member.status == discord.Status.dnd:
          status = "<:dnd:1026587711882149929>"
      elif member.status == discord.Status.idle:
          status = "<:idle:1041010236540076073>"
      elif member.status == discord.Status.online:
          status = "<:enabled:1021007058369261648>"
      elif member.status == discord.Status.offline:
          status = "<:offline:1041010265690484767>"

      embed = discord.Embed(colour=color, timestamp=ctx.message.created_at, title=f"{member}")
      embed.set_thumbnail(url=member.display_avatar)
      embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=f"{ctx.author.display_avatar}")
      embed.add_field(name="Username", value=member.display_name)
      embed.add_field(name='Status', value=f'{status}')
      embed.add_field(name="User ID", value=f'`{member.id}`')
      embed.add_field(name="Created Account", value=f'```{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```')
      embed.add_field(name="Joined", value=f'```{member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}```')
      embed.add_field(name="Roles", value="".join([role.mention for role in roles]))
      embed.add_field(name="Highest Role", value=f'{member.top_role.mention}')
      embed.add_field(name="Boosting", value=f'`{member.premium_since}`')
      button = Button(label='Avatar', url=f'{member.display_avatar}', style=discord.ButtonStyle.gray)
      view = View()
      view.add_item(button)
      await ctx.reply(embed=embed, view=view)



    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def poll(self, ctx, *, message):
      await ctx.message.delete()
      message = await ctx.reply(f"```{message} | {ctx.message.author}```")
      await message.add_reaction('<:successful:995036527220510802>')
      await message.add_reaction('<:error:995036612897554442>')

    @commands.command(aliases=['mc'])
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def membercount(self, ctx):
      embed = discord.Embed(description=f"<:user:1062798992397832282> `{ctx.guild.name}` **has** `{ctx.guild.member_count}` **members**", color=color)
      await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def emoji(self, ctx, emoji: discord.Emoji):
      if emoji == None:
        await ctx.reply(embed=discord.Embed(description="", color=self.error))
      else:
        await ctx.reply(embed=discord.Embed(description="**Emoji:** %s\n**ID:**  `%s`" % (emoji, emoji.id), color=color))
    

    @commands.command(aliases=["invs"])
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def invites(self, ctx, member: discord.Member = None):
        totalInvites = 0
        if member == None:
            member = ctx.author
        for i in await ctx.guild.invites():
            if i.inviter == member:
                totalInvites += i.uses
        if member == ctx.author:
             embed = discord.Embed(description="<:user:1062798992397832282> **you've invited** `%s` **member(s) to the server**" % (totalInvites), color=color)
        else:
            embed = discord.Embed(description="<:user:1062798992397832282> `%s` **has invited** `%s` **member(s) to the server**" % (member.name, totalInvites), color=color)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
      await member.add_roles(role)
      await ctx.reply(embed=discord.Embed(description=f"<:successful:995036527220510802> **succesfully added** `{role.name}` **to** `{member.name}`", color=color))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def derole(self, ctx, member: discord.Member, role: discord.Role):
      await member.remove_roles(role)
      await ctx.reply(embed=discord.Embed(description=f"<:successful:995036527220510802> **succesfully removed** `{role.name}` **from** `{member.name}`", color=color))

    @commands.command(aliases=["eadd"])
    @commands.cooldown(1, 3, commands.BucketType.channel)
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
                    return await ctx.reply(embed=discord.Embed(description="<:successful:995036527220510802> **succesfully added** %s" % (emote), color=color))
                except Exception:
                    return await ctx.reply(embed=discord.Embed(description=f"<:error:995036612897554442> **failed to add emoji**", color=color))
            else:
                return await ctx.reply(embed=discord.Embed(description=f"<:error:995036612897554442> **invalid emoji**", color=color))
        except Exception:
            return await ctx.reply(embed=discord.Embed(description=f"<:error:995036612897554442> **failed to add emoji**", color=color))



    @commands.command()
    async def afk(self, ctx, mins, reason=None):
      current_nick = ctx.author.nick
      await ctx.send(embed=discord.Embed(color=color, description="{0.author.mention} **has gone afk for** `{1}` **minutes(s)**.".format(ctx, mins)))
      await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")

      counter = 0
      while counter <= int(mins):
          counter += 1
          await asyncio.sleep(60)

          if counter == int(mins):
              await ctx.author.edit(nick=current_nick)
              await ctx.reply(embed=discord.Embed(color=color, description=f"{ctx.author.mention} **is no longer AFK*"))
              break

    @commands.command(aliases=["ri"]) 
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def roleinfo(self, ctx, *, role: discord.Role=None):
        if role == None:
          embed=discord.Embed(description="<:error:995036612897554442> **input a role**", color=color)
          await ctx.send(embed=embed)
        perms = role.permissions
        members = len([x for x in ctx.guild.members if role in x.roles])
        if perms.value == 0: 
            msg = f"{role.name} **has no permissions**"
        else:
            msg = " ".join([x[0].replace("_", " ").title() for x in filter(lambda p: p[1] == True, perms)])
        if role.hoist:
            hoist = "yes"
        else:
            hoist = "no"
        if role.mentionable:
            mention = "yes"
        else:
            mention = "no"
        embed=discord.Embed(color=color)
        embed.set_author(name=f"{role.name} info", icon_url=ctx.guild.icon.url)
        embed.add_field(name="mentionable", value=f'`{mention}`')
        embed.add_field(name="role color", value=f'`{role.colour}`')
        embed.add_field(name="user count", value=f'`{members}`')
        embed.add_field(name="hoisted", value=f'`{hoist}`')
        embed.add_field(name="role ID", value=f'`{role.id}`')
        embed.add_field(name="role perms", value=f'```{msg}```', inline=False)
        await ctx.reply(embed=embed)


    @commands.command(aliases=["perms"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def permissions(self, ctx, *, user: discord.Member=None):
        author = ctx.message.author
        if not user:
            user = author
        perms = "\n".join([x[0].replace("_", " ").title() for x in filter(lambda p: p[1] == True, user.guild_permissions)])
        embed=discord.Embed(description=f'```{perms}```', color=color)
        embed.set_author(name="{}'s permissions".format(user.name), icon_url=user.avatar.url)
        await ctx.reply(embed=embed)


    @commands.command()
    async def spotify(self, ctx, user: discord.Member = None):
      try:
        if user == None:
            user = ctx.author
        if user.activities:
            for activity in user.activities:
                if isinstance(activity, Spotify):
                    embed = discord.Embed(
                        title = f"{user.name}'s Spotify",
                        description = f"Listening to **{activity.title}**",
                        color = color)
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.add_field(name="Artist", value=activity.artist)
                    embed.add_field(name="Album", value=activity.album)
                    embed.set_footer(text=f'Song started at {activity.created_at.strftime("%H:%M")}')
                    await ctx.reply(embed=embed)
        else:
          embed = discord.Embed(color=self.successclr, description=f'`{user.name}` **is not listening to anything**')
          await ctx.reply(embed=embed)
      except Exception as e:
        print(e)


    @commands.command(aliases=["m", "module"])
    @commands.cooldown(1,10, commands.BucketType.user) 
    @commands.has_permissions(administrator=True)
    async def modules(self, ctx):
        embed = discord.Embed(title='**wraths modules**', description=   f'''
```
・tickets [soon]
・moderation
・fun
・utility
・wrath
・welcome
・economy
```''',color=color)

        embed.set_thumbnail(url=self.av)
        await ctx.reply(embed = embed) 

async def setup(bot):
  await bot.add_cog(utility(bot))
