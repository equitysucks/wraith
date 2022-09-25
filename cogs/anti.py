import discord
from discord.ext import commands
import os
import datetime
import pymongo
import time

color = 0x2f3136
success = 0xA4FF00
error = 0xFF1A1A

class anti(commands.Cog):
    def __init__(self, bot):
      self.bot = bot

    mongoClient = pymongo.MongoClient('mongodb+srv://sinful:khaleed111@cluster0.i8qcd.mongodb.net/?retryWrites=true&w=majority')
    db = mongoClient.get_database("apollo2").get_collection("whitelist")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        whitelistedUsers = self.db.find_one({ "guild_id": channel.guild.id })["users"]

        async for entry in channel.guild.audit_logs(
            limit=1,
            after=datetime.datetime.now() - datetime.timedelta(seconds = 2),
            action=discord.AuditLogAction.channel_delete):
            if entry.user.id in whitelistedUsers or entry.user in whitelistedUsers:
                return

            await entry.user.ban(reason="apollo Anti-Nuke: Deleting Channels")
            await channel.create()
            return

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        whitelistedUsers = self.db.find_one({ "guild_id": channel.guild.id })["users"]

        async for entry in channel.guild.audit_logs(
            limit=1,
            after=datetime.datetime.now() - datetime.timedelta(seconds = 2),
            action=discord.AuditLogAction.channel_create):

            if entry.user.id in whitelistedUsers or entry.user in whitelistedUsers:
                return

            await entry.user.ban(reason="apollo Anti-Nuke: Creating Channels")
            await channel.delete()
            return



    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        whitelistedUsers = self.db.find_one({ "guild_id": role.guild.id })["users"]
        async for entry in role.guild.audit_logs(
            limit=1,
            after=datetime.datetime.now() - datetime.timedelta(seconds = 2),
            action=discord.AuditLogAction.role_create):
            if entry.user.bot:
                return
            
            if entry.user.id in whitelistedUsers or entry.user in whitelistedUsers:
                return

            await role.guild.ban(entry.user, reason="apollo Anti-Nuke: Creating Roles")
            return

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        whitelistedUsers = self.db.find_one({ "guild_id": role.guild.id })["users"]
        async for entry in role.guild.audit_logs(
            limit=1,
            after=datetime.datetime.now() - datetime.timedelta(seconds = 2),
            action=discord.AuditLogAction.role_delete):
            if entry.user.bot:
                return

            if entry.user.id in whitelistedUsers or entry.user in whitelistedUsers:
                return

            await role.guild.ban(entry.user, reason="apollo Anti-Nuke: Deleting Roles")
            return

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        whitelistedUsers = self.db.find_one({ "guild_id": after.guild.id })["users"]
        async for entry in after.guild.audit_logs(
            limit=1,
            after=datetime.datetime.now() - datetime.timedelta(seconds = 2),
            action=discord.AuditLogAction.role_update):
            if entry.user.id in whitelistedUsers or entry.user in whitelistedUsers:
                return

            if not before.permissions.ban_members and after.permissions.ban_members:
                await after.guild.ban(entry.user, reason="apollo Anti-Nuke: Updating Roles - Permissions")
                return

            if not before.permissions.kick_members and after.permissions.kick_members:
                await after.guild.ban(entry.user, reason="apollo Anti-Nuke: Updating Roles - Permissions")
                return

            if not before.permissions.administrator and after.permissions.administrator:
                await after.guild.ban(entry.user, reason="apollo Anti-Nuke: Updating Roles - Permissions")
                return

            if entry.target.id == before.guild.id:
                if after.permissions.kick_members or after.permissions.ban_members or after.permissions.administrator or after.permissions.mention_everyone or after.permissions.manage_roles:
                    await after.guild.ban(entry.user)
                    await after.edit(permissions=1166401)
                    
            return


    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        whitelistedUsers = self.db.find_one({ "guild_id": guild.id })["users"]
        async for entry in guild.audit_logs(
            limit=1,
            after=datetime.datetime.now() - datetime.timedelta(seconds = 2),
            action=discord.AuditLogAction.ban):
            if entry.user.id in whitelistedUsers or entry.user in whitelistedUsers:
                return
            
            await entry.user.ban(reason="apollo Anti-Nuke: Banning Users")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        whitelistedUsers = self.db.find_one({ "guild_id": member.guild.id })["users"]
        async for entry in member.guild.audit_logs(
            limit=1,
            after=datetime.datetime.now() - datetime.timedelta(seconds = 2),
            action=discord.AuditLogAction.kick):
            if entry.user.id in whitelistedUsers or entry.user in whitelistedUsers:
                return
                
            if entry.target.id == member.id:
                await entry.user.ban(reason="apollo Anti-Nuke: Kicking Users")
                return


    @commands.Cog.listener()
    async def on_webhooks_update(self, webhook):
        whitelistedUsers = self.db.find_one({ "guild_id": webhook.guild.id })["users"]
        async for entry in webhook.guild.audit_logs(
            limit=1,
            after=datetime.datetime.now() - datetime.timedelta(seconds = 2),
            action=discord.AuditLogAction.webhook_create):
            if entry.user.id in whitelistedUsers or entry.user in whitelistedUsers:
                return

            await entry.user.ban()
            await entry.target.delete(reason="apollo Anti-Nuke: Creating Webhook")
            return


    @commands.Cog.listener()
    async def on_member_join(self, member):
        whitelistedUsers = self.db.find_one({ "guild_id": member.guild.id })["users"]
        if member.bot:
            async for i in member.guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes = 2),
                action=discord.AuditLogAction.bot_add):
                if i.user.id in whitelistedUsers or i.user in whitelistedUsers:
                    return

                await member.ban()
                await i.user.ban()


    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def setup(self, ctx):
        embed = discord.Embed(
        title = "apollo",
        color = 0x2f3136,
        description = f"```apollo anti-nuke is one of the most reliable and safe anti-nukes created. With apollo, you can stop raiders, nukers, and people from harming your server with its key features you can view by viewing the help command and dragging apollo's role above all roles possible. To whitelist a user from apollo's anti-nuke features, you must say `;whitelist [@user]`, but be aware that apollo will take no action towards what they decide to do to and with your server.```")
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/FXNH9kCHQxOWM1EmdItYQxXiCBo52Pe6wzSqrH7mt00/%3Fsize%3D1024/https/cdn.discordapp.com/icons/995022029017329725/b03a23a6114f9ac6b90bca839248ca7b.png?width=494&height=494")
        await ctx.send(embed=embed)
        channel = await ctx.guild.create_text_channel('apollo-logs')
        jail = await ctx.guild.create_text_channel('jail')
        muted = await ctx.guild.create_role(name="Muted")
        await channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
        await channel.send(embed=discord.Embed(description="<:successful:995036527220510802> **succesfully created a logging channel** `BETA`", color=success))


    @commands.command()
    @commands.cooldown(1, 8, commands.BucketType.channel)
    async def configs(self, ctx):
        guild = ctx.message.guild
        embed=discord.Embed(title=f"Anti-Nuke Configuration — {ctx.guild.name}", description="\n**AntiBan**\n<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 mins`\n\n**AntiKick**\n<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 mins`\n\n**AntiSpam**\n<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `Not Measurable`\n<:slowmode:1021013863044481026> **Threshold**: `Not Measurable`\n\n**AntiChannel**\n<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 mins`\n\n**AntiRole**\n<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 mins`\n\n**AntiWebhook**\n<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 mins`", color=color)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
        await ctx.send(embed=embed)


    @commands.command(aliases=["inv"])
    @commands.cooldown(1,5, commands.BucketType.user)
    async def invite(self, ctx):
        embed = discord.Embed(color=color)
        embed.add_field(name='<a:bearkiss:1018244723472871424> apollo', value=
    f'''
    > <:bot_tag:1018570092734332928> **Invite me** [__**here**__](https://discord.com/api/oauth2/authorize?client_id=1016424578320445570&permissions=8&scope=bot)
    > <:z1_badgepartneredserverowner:1019998583023489146> **Join my support** [__**server**__](https://google.com)''')
        await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def gleave(self, ctx):
        if ctx.author.id == 995021078428663889 or ctx.author.id == 607004065729347606:
            await ctx.guild.leave()


async def setup(bot):
  await bot.add_cog(anti(bot))
