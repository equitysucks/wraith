import discord
from discord.ext import commands
import pymongo


color = 0x2f3136
success = 0xA4FF00
error = 0xFF1A1A

mongoClient = pymongo.MongoClient('mongodb+srv://sinful:khaleed111@cluster0.i8qcd.mongodb.net/?retryWrites=true&w=majority')
db = mongoClient.get_database("apollo").get_collection("welcome")

class welcome(commands.Cog):
    def __init__(self, client):
        self.client = client



    '''@commands.group(invoke_without_command=True, aliases=["welc"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def welcome(self,ctx):
        embed = discord.Embed(title="welcome module", color=color)
        embed.add_field(name="Usage", value="```・welcome message {message}\n・welcome channel {channel}\n・welcome test\n・welcome variables```", inline=False)
        embed.add_field(name="Info", value="```welcome message - sets the welcome message\nwelcome channel - sets the welcome channel\nwelcome test - shows the welcome message\nwelcome variables - shows the welcome variables```", inline=False)
        embed.add_field(name="Variables", value="```{user.name} - sends the users name\n{user.mention} - mentions the user\n{user} - sends the users name and tag\n{user.tag} - sends the users tag | discriminator\n{server} - sends the servers name```", inline=False)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
        await ctx.send(embed=embed)

    @welcome.command(aliases=["channel"])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def chan(self, ctx, channel: discord.TextChannel = None):
      if channel == None:
        embed = discord.Embed(color=error,description=f'<:error:995036612897554442> **input a channel**')
        await ctx.send(embed=embed)
      else:
        db.update_one({"guild_id": ctx.guild.id},{"$set": {f"welcomechannel": f'{channel.id}'}})
        embed = discord.Embed(description=f'<:successful:995036527220510802> **succesfully set the** `welcome channel` **to** `{channel.name}`', color=success)
        await ctx.send(embed=embed)

    @welcome.command(aliases=["message"])
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def msg(self, ctx, *, msg=None):
      if msg == None:
        embed = discord.Embed(color=error,description=f'<:error:995036612897554442> **input a message**')
        await ctx.send(embed=embed)
      else:
        db.update_one({"guild_id": ctx.guild.id},{"$set": {f"welcomemessage": f'{msg}'}})
        embed = discord.Embed(description=
		    f'<:successful:995036527220510802> **succesfully set the** `welcome message` **to**\n```{msg}```',color=success)
        await ctx.send(embed=embed)
        
    @welcome.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def test(self, ctx):

       welcmsg = db.find_one({ "guild_id": ctx.guild.id})['welcomemessage']
       if welcmsg == None or welcmsg == "off":
         embed = discord.Embed(color=error,description=f'<:error:995036612897554442> **no welcome** `message` **set**')
         await ctx.send(embed=embed)

       else:
            welcmsg = welcmsg.replace("{server}", ctx.guild.name)
            welcmsg = welcmsg.replace("{user.mention}", ctx.author.mention)
            welcmsg = welcmsg.replace("{user.name}", ctx.author.name)
            welcmsg = welcmsg.replace("{user}", str(ctx.author))
            welcmsg = welcmsg.replace("{user.tag}", str(ctx.author.discriminator))
            embed = discord.Embed(color=color,description=f'{welcmsg}')
            embed.set_author(name=f'welcome to {ctx.guild.name}')
            embed.set_footer(text=f'{ctx.guild.member_count} members | {ctx.guild.name}')
            embed.set_thumbnail(url=f'{ctx.author.avatar.url}')
            await ctx.send(ctx.author.mention, embed=embed)
            embed=discord.Embed(color=success,description=f'<:successful:995036527220510802> **successfuly tested the** `welcome message`')
            await ctx.send(embed=embed)
            
    @welcome.command(aliases=['var', 'vars'])
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def variables(self, ctx):
       embed = discord.Embed(title = "apollo", description="```{user.name} - sends the users name\n{user.mention} - mentions the user\n{user} - sends the users name and tag\n{user.tag} - sends the users tag | discriminator\n{server} - sends the servers name```", color=color)
       embed.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
       await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_join(self, ctx):
      welcmsg = db.find_one({ "guild_id": ctx.guild.id})['welcomemessage']
      welcchan = db.find_one({ "guild_id": ctx.guild.id})['welcomechannel']
      embed = discord.Embed(color=color, description=welcmsg)
      await self.client.get.channel(welcchan).send(embed=embed)'''


async def setup(bot):
  await bot.add_cog(welcome(bot))
