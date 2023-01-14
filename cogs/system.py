import discord
from discord.ext import commands
import random
import requests
import pymongo
from discord.ext.commands import cooldown, BucketType
import aiohttp
import os


color = 0x2f3136

class system(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.error = '<:error:995036612897554442>'
        self.success = '<:successful:995036527220510802>'
        self.color = 0x2f3136
        self.successclr = 0x43d764
        self.errorclr = 0xFF1A1A
        self.av = 'https://cdn.discordapp.com/attachments/1046007816571338792/1063772884914413598/f5c9023ededc5dda88f472d0c37e7fa7.jpg'
        print('[Status] Loaded Cog: System')


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(color=color, description=f'{self.error} {ctx.author.mention} **you are missing** `{"".join(error.missing_perms)}` **permissions**'))
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=discord.Embed(color=color, description=f'{self.error} {ctx.author.mention} **you are on cooldown for** `{round(error.retry_after)}` **second(s)**'))

    @commands.command(aliases=['p', 'lat ', 'latency'])
    @commands.cooldown(1,8, commands.BucketType.user)
    async def ping(self, ctx):
        try:
            lat = int(self.client.latency * 1000)
            if lat > 100:
                emoji = '<:8920theconnectionisbad:1045747873595281408>'
            elif lat < 30:
                emoji = '<:7431theconnectionisexcellent:1020011599085449309>'
            embed = discord.Embed(color=color, description=f'{emoji} **Latency is** `{lat}` **ms**')
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        chan = self.client.get_channel(1017385638871441428)
        mem = f'{len(guild.members)}'
        await chan.send(embed=discord.Embed(description=f"**i have been removed from** {guild.name} `—` {mem} **members**", color=color))


    @commands.command(aliases=["botinfo", "bi"])
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def stats(self, ctx):
        embed = discord.Embed(color=color, description=f"""

**counts**
> **guilds** `{len(self.client.guilds)}`
> **users** `{len(self.client.users)}`
> **commands** `{len(self.client.commands)}`

**prefix**
> **default** `;`
> **alt** <@1027627566963621898>

**misc**
> **ping** `{int(self.client.latency * 1000)}ms`
> **library** `discord.py {discord.__version__}`
> **developers** `{self.client.get_user(995021078428663889)}`
        """)
        embed.set_author(name='wrath', icon_url=self.av)
        embed.set_thumbnail(url=self.av)
        await ctx.send(embed=embed)

    @commands.command(aliases=["inv"])
    @commands.cooldown(1,5, commands.BucketType.user)
    async def invite(self, ctx):
        embed = discord.Embed(color=color, description=
    f'''
    > **Invite me** [__**here**__](https://discord.com/api/oauth2/authorize?client_id=1027627566963621898&permissions=8&scope=bot)
    > **Join my support** [__**server**__](https://discord.gg/K7F3cGYYkr)''')
        embed.set_author(name='wrath', icon_url=self.av)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        embed = discord.Embed(colour=color)
        embed.add_field(name="<:moderation:1017390327063134308> Cogs", value="```cpp\nSyncing...```", inline = False)
        m = await ctx.reply(embed=embed)
        cogs = 0

        try:
          for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and not filename.startswith('System'):
              await self.client.reload_extension(f'cogs.{filename[:-3]}')
              cogs += 1
          posem = discord.Embed(colour=color)
          posem.add_field(name="<:moderation:1017390327063134308> Cogs", value=f"```cpp\nSynced {cogs} cogs Successfully!```", inline = False)
          await m.edit(embed=posem)

        except:
            failem = discord.Embed(colour=color)
            failem.add_field(name="<:moderation:1017390327063134308> Cogs", value=f"```cpp\nFailed to sync all cogs. Check console for error.```", inline = False)
            await m.edit(embed=failem)
            


async def setup(bot):
  await bot.add_cog(system(bot))