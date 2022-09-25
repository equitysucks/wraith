import discord
from discord.ext import commands
import random
import requests
import pymongo
from discord.ext.commands import cooldown, BucketType
import aiohttp


color = 0x2f3136
success = 0xA4FF00
errorc = 0xFF1A1A

mongoClient = pymongo.MongoClient('mongodb+srv://sinful:khaleed111@cluster0.i8qcd.mongodb.net/?retryWrites=true&w=majority')
db = mongoClient.get_database("apollo2").get_collection("whitelist")

class system(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(color=errorc, description=f'<:error:995036612897554442> {ctx.author.mention} **you are missing** `{"".join(error.missing_perms)}` **permissions**'))
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=discord.Embed(color=errorc, description=f'<:error:995036612897554442> {ctx.author.mention} **you are on cooldown for** `{round(error.retry_after)}` **second(s)**'))

    @commands.command()
    @commands.cooldown(1,8, commands.BucketType.user)
    async def ping(self, ctx):
        embed = discord.Embed(color=color, description=f'Latency is `{int(self.client.latency * 1000)}` **ms**')
        await ctx.send(embed=embed)



    @commands.command()
    async def status(self, ctx):
        if ctx.author.id == 995021078428663889 or ctx.author.id == 607004065729347606:
            await ctx.send(embed=discord.Embed(description=f"<:server:1018262700561813585> Database is `{'connected' if db.find_one({ 'guild_id': ctx.guild.id })['users'] else 'disconnected'}`", color=color))


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channellol = self.client.get_channel(1017385638871441428)
        haha = f'{len(guild.members)}'
        await channellol.send(embed=discord.Embed(description=f"i have been removed from: {guild.name} — {haha} members", color=color))


    @commands.command(aliases=["botinfo", "bi"])
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def info(self, ctx):
        embed = discord.Embed(color=color)
        embed.set_author(name="apollo")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
        embed.add_field(name="<:ClydeBot:1018545663501414501> Statistics", value=f"```asciidoc\n・Guilds: {len(self.client.guilds)}\n・Users: {len(self.client.users)}```")
        embed.add_field(name="<:6313questionicon:1020011959564902483> Prefix", value=f"```asciidoc\n・Default: ;\n・Alt: @apollo```")
        embed.add_field(name="<:2047blurplelibrary:1020011792904245248> Library", value="```asciidoc\n・Discord.py```")
        embed.add_field(name="<:6947developerbadge:1020008017950953532> Developer", value="```asciidoc\n・kh#1337```")
        embed.add_field(name="<a:crown:1018544927447208069> Owner", value="```asciidoc\n・markus#9999```")
        embed.add_field(name="<:7431theconnectionisexcellent:1020011599085449309> Latency", value=f"```asciidoc\n・ {round(self.client.latency * 1000)}ms```")
        await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(system(bot))