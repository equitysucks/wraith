import discord
import sqlite3
import colorama

from colorama import Fore
from discord.ext import commands



class welcome(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.av = 'https://media.discordapp.net/attachments/1046007816571338792/1062785924796272650/97c434fb8916fe35c113103bbd142277.jpg'
        self.error = '<:error:995036612897554442>'
        self.success = '<:successful:995036527220510802>'
        self.color = 0x2f3136
        self.successclr = 0x2f3136
        self.errorclr = 0xFF1A1A
        print(f'{Fore.GREEN}[Status] Loaded Cog: Welcome{Fore.RESET}')


    @commands.group(invoke_without_command=True, aliases=["welc"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def welcome(self,ctx):
        embed = discord.Embed(color=self.color)
        embed.set_author(name='wraths welcome module', icon_url=self.av)
        embed.add_field(name="usage", value="```・welcome message {message}\n・welcome channel {channel}\n・welcome test\n・welcome variables```", inline=False)
        embed.add_field(name="info", value="```・welcome message - sets the welcome message\n・welcome channel - sets the welcome channel\n・welcome test - shows the welcome message\n・welcome variables - shows the welcome variables```", inline=False)
        embed.add_field(name="vars", value="```・{members} - sends the amount of members\n・{user} - sends the members name\n・{mention} - sends the users name and tag\n・{guild} - sends the server name```", inline=False)
        await ctx.send(embed=embed)




    @welcome.command(aliases=["channel"])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def chan(self, ctx, channel: discord.TextChannel = None):
      if channel == None:
        embed = discord.Embed(color=self.error,description=f'{self.error} **input a channel**')
        await ctx.send(embed=embed)
      
      else:
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {ctx.guild.id}")
        result = cursor.fetchone()
        if result is None:
          sql = ("INSERT INTO main(guild_id, channel_id) VALUES(?,?)")
          val = (ctx.guild.id, channel.id)
          embed = discord.Embed(description=f'{self.success} **succesfully set the** `welcome channel` **to** `{channel.name}`', color=self.successclr)
          await ctx.send(embed=embed)
        elif result is not None:
          sql = ("UPDATE main SET channel_id = ? WHERE guild_id = ?")
          val = (channel.id, ctx.guild.id)
          embed = discord.Embed(description=f'{self.success} **succesfully updated the** `welcome channel` **to** `{channel.name}`', color=self.successclr)
          await ctx.send(embed=embed)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()



    @welcome.command(aliases=["message"])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def msg(self, ctx, *, text = None):
      if text == None:
        embed = discord.Embed(color=self.error,description=f'{self.error} **input a message**')
        await ctx.send(embed=embed)
      
      else:
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {ctx.guild.id}")
        result = cursor.fetchone()
        if result is None:
          sql = ("INSERT INTO main(guild_id, msg) VALUES(?,?)")
          val = (ctx.message.guild.id, text)
          embed = discord.Embed(description=
          f'{self.success} **succesfully set the** `welcome message` **to**\n```{text}```',color=self.successclr)
          await ctx.send(embed=embed)
        elif result is not None:
          sql = ("UPDATE main SET msg = ? WHERE guild_id = ?")
          val = (text, ctx.message.guild.id)
          embed = discord.Embed(description=
          f'{self.success} **succesfully updated the** `welcome message` **to**\n```{text}```',color=self.successclr)
          await ctx.send(embed=embed)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
    

    @commands.Cog.listener()
    async def on_member_join(self, member):
      try:
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {member.guild.id}")
        result =  cursor.fetchone()
        if result is None:
            return
        else:
            cursor.execute(f"SELECT msg FROM main WHERE guild_id = {member.guild.id}")
            result1 = cursor.fetchone()

            members = len(list(member.guild.members))
            mention = member.mention
            user = member.name
            guild = member.guild

            embed = discord.Embed(color=self.color, description=str(result1[0]).replace('{members}', str(members)).replace('{mention}', str(mention)).replace('{user}', str(user)).replace('{guild}', str(guild)))
            channel = self.client.get_channel(int(result[0]))
            await channel.send(embed=embed)
      except Exception as e:
        print(e)



    @welcome.command()
    async def test(self, ctx):
      try:
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {ctx.guild.id}")
        result =  cursor.fetchone()
        if result is None:
            return
        else:
            cursor.execute(f"SELECT msg FROM main WHERE guild_id = {ctx.guild.id}")
            result1 = cursor.fetchone()

            members = len(list(ctx.guild.members))
            mention = ctx.author.mention
            user = ctx.author.name
            guild = ctx.guild.name


            embed = discord.Embed(color=self.color, description=str(result1[0]).replace('{members}', str(members)).replace('{mention}', str(mention)).replace('{user}', str(user)).replace('{guild}', str(guild)))
            await ctx.reply(embed=embed)
      except Exception as e:
        print(e)


    @welcome.command(aliases=['var', 'vars'])
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def variables(self, ctx):
       embed = discord.Embed(description="```・{members} - sends the amount of members\n・{user} - sends the members name\n・{mention} - sends the users name and tag\n・{guild} - sends the server name```", color=self.color)
       embed.set_author(name='wraths welcome variables', icon_url=self.av)
       await ctx.send(embed=embed)


async def setup(bot):
  await bot.add_cog(welcome(bot))
