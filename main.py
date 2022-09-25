import discord
import random
import inspect
import requests
import urllib
import datetime
import asyncio
import os
import json
import pymongo
import ast


from time import sleep
from discord import app_commands
from discord.ext import commands, tasks
from unittest import skip






mongoClient = pymongo.MongoClient('mongodb+srv://sinful:khaleed111@cluster0.i8qcd.mongodb.net/?retryWrites=true&w=majority')
db = mongoClient.get_database("apollo2").get_collection("whitelist")
color = 0x2f3136
success = 0x44F16A
error = 0xFF1A1A



client = commands.Bot(commands.when_mentioned_or(";"), intents=discord.Intents.all())
client.remove_command("help")




async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
   




def is_owner(ctx):
    return ctx.message.author.id == 995021078428663889

def is_whitelisted(ctx):
    return ctx.message.author.id in db.find_one({ "guild_id": ctx.guild.id })["users"] or ctx.message.author.id == 995021078428663889
    
def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 995021078428663889




@client.event
async def on_ready():
    for i in client.guilds:
            if not db.find_one({ "guild_id": i.id }):
                db.insert_one({
                    "users": [],
                    "guild_id": i.id
                })
    channel = client.get_channel(1017385638871441428)
    await channel.send(embed=discord.Embed(description=f"<:enabled:1021007058369261648> `apollo` is online", color=color))
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.competing,name=f"@apollo help"))
    print("apollo is online")








@client.group(name='help', aliases=['h'], invoke_without_command=True)
@commands.cooldown(1,5, commands.BucketType.user)
async def help(ctx):
     embed1 = discord.Embed(description=f"""
__**how-to use**__
use the `emojis` <:left:1017394327728705596> `&` <:right:1017394325476352032> to navigate through the help menu and to see different pages or you can do ;help `[module]`

__**need help ?**__
if help is needed in any way possible join my support [__**server**__](https://google.com) or dm <@995021078428663889>.
""", color=color)
     embed1.set_footer(text=f"apollo {len(client.commands)} commands")
     embed1.set_author(name="home page", icon_url='https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg')
     embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")

     
     embed2 = discord.Embed(color=color)
     embed2.add_field(name="<:moderation:1017390327063134308> Moderation", value="""
`・ban [user]` **—** bans the mentioned user
`・kick [user]` **—** kicks the mentioned user
`・lock [channel]` **—** locks the channel
`・unlock [channel]` **—** unlocks the channel
`・mute [user]` **—** mutes the mentioned user
`・unmutes [user]` **—** unmutes the mentioned user
`・jail [user]` **—** jails the mentioned user
`・unjail [user]` **—** unjails the mentioned user
`・purge [amount]` **—** purges number of messages
`・clear [amount]` **—** clears number of messages
`・nuke` **—** recreates the server
`・slowmode [seconds]` **—** sets channel slowmode
`・offslowmode` **—** turns off channel slowmode
`・unban [ID]` **—** unbans the user ID
""")
     embed2.set_footer(text=f"Page 2 - apollo")
     embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")

     embed3 = discord.Embed(color=color)
     embed3.add_field(name="<a:Dancing:1017685291559039007> Fun", value="""
`・kiss [user]` **—** kisses the mentioned user
`・slap [user]` **—** slaps the mentioned user
`・hug [user]` **—** hugs the mentioned user
`・coinflip` **—** flips a coin
`・pat [user]` **—** pats the mentioned user
`・feed [user]` **—** feeds the mentioned user
""")
     embed3.set_footer(text=f"Page 3 - apollo")
     embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")

     embed4 = discord.Embed(color=color)
     embed4.add_field(name="<:bw_shield:1021067469399523449> Protection `[SOON]`", value="""
`・antinuke bans [limit]` **—** edits limit for antinuke trigger
`・toggle [module]` **—** turns the antinuke module on & off
`・whitelist [user]` **—** whitelists mentioned user
`・punishment [module]` **—** shows the modules punishment
`・whitelisted` **—** shows whitelisted users
`・dewhitelist [user]` **—** removes user from whitelist
`・config` **—** shows the antinuke configuration
`・setup` **—** sets up apollo
""")
     embed4.set_footer(text=f"Page 4 - apollo")
     embed4.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")

     embed5 = discord.Embed(color=color)
     embed5.add_field(name="<:bw_utility:1021068556718321744> Utility", value="""
`・serverinfo` **—** shows the serverinfo
`・avatar [user]` **—** shows the users avatar
`・userinfo [user]` **—** shows the userinfo of user
`・membercount` **—** shows membercount 
`・invites [user]` **—** shows amount of invites
`・addrole [user]` **—** adds role to user
`・emoji [emoji]`   **—** shows information on the emoji
`・emojiadd [emoji]` **—** adds emoji to server
`・emojidelete` **—** deletes emoji
`・serverbanner` **—** shows the server banner
`・servericon` **—** shows the servericon
""") 
     embed5.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     embed5.set_footer(text=f"Page 5 - apollo")


     embed6 = discord.Embed(color=color)
     embed6.add_field(name="<a:bearkiss:1018244723472871424> Apollo", value="""
`・invite` **—** sends bot invite links
`・gleave` **—** [`developer command`]
`・guilds` **—** [`developer command`]
`・botinfo` **—** sends apollos information
""") 
     embed6.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     embed6.set_footer(text=f"Page 6 - apollo")

     embed7 = discord.Embed(color=color)
     embed7.add_field(name="<a:9850bluewelcome:1021087894837928056> Welcome `[SOON]`", value="""
`・welcome` **—** shows welcome information and help
`・toggle` **—** toggles the specified module
`・welcome variables` **—** sends the welcome variables
`・welcome test` **—** shows what welcome msg would look like
""") 
     embed7.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     embed7.set_footer(text=f"Page 7 - apollo")



     embed8 = discord.Embed(color=color)
     embed8.add_field(name="<:lastfm:1021442695362773002> LastFM `[SOON]`", value="""
`・placeholder` **—** shows the placholder placeholding
`・placeholder` **—** shows the placholder placeholding
`・placeholder` **—** shows the placholder placeholding
""") 
     embed8.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     embed8.set_footer(text=f"Last Page - apollo")


     pages = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8]
     message = await ctx.send(embed = embed1) 
   
     await message.add_reaction('<:left:1017394327728705596>')
     await message.add_reaction('<:right:1017394325476352032>')

     def check(reaction, user):
        return user == ctx.author

     i = 0
     reaction = None

     while True:
          if str(reaction) == '<:left:1017394327728705596>':
              if i > 0:
                  i -= 1
                  await message.edit(embed=pages[i])
          if str(reaction) == '<:right:1017394325476352032>':
              if i < 7:
                  i += 1
                  await message.edit(embed=pages[i])


          try:  
              reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
              await message.remove_reaction(reaction, user)
          except:
              pass

              await message.clear_reaction()


@help.command(aliases=['mod'])
async def moderation(ctx):
     embed = discord.Embed(color=color)
     embed.add_field(name="<:moderation:1017390327063134308> Moderation", value="""
`・ban [user]` **—** bans the mentioned user
`・kick [user]` **—** kicks the mentioned user
`・lock [channel]` **—** locks the channel
`・unlock [channel]` **—** unlocks the channel
`・mute [user]` **—** mutes the mentioned user
`・unmutes [user]` **—** unmutes the mentioned user
`・jail [user]` **—** jails the mentioned user
`・purge [amount]` **—** purges number of messages
`・clear [amount]` **—** clears number of messages
`・nuke` **—** recreates the server
`・slowmode [seconds]` **—** sets channel slowmode
`・offslowmode` **—** turns off channel slowmode
`・unban [ID]` **—** unbans the user ID
""")
     embed.set_footer(text=f"moderation - apollo")
     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     await ctx.send(embed=embed)


@help.command()
async def fun(ctx):
     embed3 = discord.Embed(color=color)
     embed3.add_field(name="<a:Dancing:1017685291559039007> Fun", value="""
`・kiss [user]` **—** kisses the mentioned user
`・slap [user]` **—** slaps the mentioned user
`・hug [user]` **—** hugs the mentioned user
`・coinflip` **—** flips a coin
`・pat [user]` **—** pats the mentioned user
`・feed [user]` **—** feeds the mentioned user
""")
     embed3.set_footer(text=f"fun - apollo")
     embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     await ctx.send(embed=embed3)


@help.command(aliases=['protect', 'anti'])
async def protection(ctx):
     embed4 = discord.Embed(color=color)
     embed4.add_field(name="<:bw_shield:1021067469399523449> Protection `[SOON]`", value="""
`・antinuke bans [limit]` **—** edits limit for antinuke trigger
`・toggle [module]` **—** turns the specified module on or off
`・punishment [module]` **—** shows the modules punishment
`・whitelist [user]` **—** whitelists mentioned user
`・whitelisted` **—** shows whitelisted users
`・dewhitelist [user]` **—** removes user from whitelist
`・config` **—** shows the antinuke configuration
`・setup` **—** sets up apollo
""")
     embed4.set_footer(text=f"protection - apollo")
     embed4.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     await ctx.send(embed=embed4)


@help.command(aliases=['util'])
async def utility(ctx):
     embed5 = discord.Embed(color=color)
     embed5.add_field(name="<:bw_utility:1021068556718321744> Utility", value="""
`・serverinfo` **—** shows the serverinfo
`・avatar [user]` **—** shows the users avatar
`・userinfo [user]` **—** shows the userinfo of user
`・membercount` **—** shows membercount 
`・invites [user]` **—** shows amount of invites
`・addrole [user]` **—** adds role to user
`・emoji [emoji]`   **—** shows information on the emoji
`・emojiadd [emoji]` **—** adds emoji to server
`・emojidelete` **—** deletes emoji
`・serverbanner` **—** shows the server banner
`・servericon` **—** shows the servericon
""") 
     embed5.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     embed5.set_footer(text=f"utility - apollo")
     await ctx.send(embed=embed5)


@help.command()
async def apollo(ctx):
     embed6 = discord.Embed(color=color)
     embed6.add_field(name="<a:bearkiss:1018244723472871424> Apollo", value="""
`・invite` **—** sends bot invite links
`・gleave` **—** [`developer command`]
`・guilds` **—** [`developer command`]
`・botinfo` **—** sends apollos information
""") 
     embed6.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     embed6.set_footer(text=f"apollo")
     await ctx.send(embed=embed6)


@help.command(aliases=['welc'])
async def welcome(ctx):
     embed7 = discord.Embed(color=color)
     embed7.add_field(name="<a:9850bluewelcome:1021087894837928056> Welcome `[SOON]`", value="""
`・welcome` **—** shows welcome information and help
`・welcome variables` **—** sends the welcome variables
`・toggle` **—** toggles the specified module
`・welcome test` **—** shows what welcome msg would look like
""") 
     embed7.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     embed7.set_footer(text=f"welcome - apollo")
     await ctx.send(embed = embed7)


@help.command(aliases=['lfm'])
async def lastfm(ctx):
     embed8 = discord.Embed(color=color)
     embed8.add_field(name="<:lastfm:1021442695362773002> LastFM `[SOON]`", value="""
`・placeholder` **—** shows the placholder placeholding
`・placeholder` **—** shows the placholder placeholding
`・placeholder` **—** shows the placholder placeholding
""") 
     embed8.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
     embed8.set_footer(text=f"Last Page - apollo")
     await ctx.send(embed=embed8)




 

@client.group(invoke_without_command=True)
@commands.cooldown(1,5, commands.BucketType.user)
async def toggle(ctx,*,module=None):
  if ctx.author.id == ctx.guild.owner.id:
    if module == None:
        embed = discord.Embed(title='toggle', color=color, description=f'```・welcmsg - toggles the welcome message\n・welcchan - toggles the welcome chan\n・welc - toggles entire welcome module```')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg')
        return await ctx.send(embed = embed)

    elif module == "welcchannel" or module == "welcomechannel" or module == "joinchan" or module == "welcome":
      db.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"welcomechannel": None}})

      embed = discord.Embed(color=success, description=f'<:successful:995036527220510802> **succesfully toggled the welcome channel**\n```To turn it back on do ;welcmsg [message]```')
      await ctx.send(embed = embed) 

      return

    elif module == "welcmsg" or module == "joinmsg" or module == "joinmessage":
      db.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"welcomemessage": None}})

      embed = discord.Embed(color=success, description=f'<:successful:995036527220510802> **succesfully toggled the welcome message**\n```To turn it back on do ;welcmsg [message]```')
      await ctx.send(embed = embed) 

      return

    elif module == "welc":
      db.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"welcomemessage": None}})
      db.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"welcomechannel": None}})

      embed = discord.Embed(color=success, description=f'<:successful:995036527220510802> **succesfully toggled the welcome module**\n```To turn it back on do ;welc for more information```')
      await ctx.send(embed = embed)

      return





@client.group(name="punishment", aliases=["punish"], invoke_without_command=True)
@commands.cooldown(1, 8, commands.BucketType.channel)
async def punishment(ctx,*,module=None):
     if module == None:
          embed=discord.Embed(title=f'Punishment', description=f"```・antichannel - shows the antichannel punishment\n・antirole - shows the antiroles punishment\n・antiban - shows the antiban punishments\n・antikick - shows the antikick punishment\n・antiwebhook - shows the antiwebhook punishment```", color=color)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
          await ctx.send(embed=embed)
     if module == 'antiban':
          embed=discord.Embed(title=f'Punishment — {module}', description=f"<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 seconds`\n<:moderation:1017390327063134308> **Punishment**: `Ban User`", color=color)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
          await ctx.send(embed=embed)
     if module == 'antikick':
          embed=discord.Embed(title=f'Punishment — {module}', description=f"<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 seconds`\n<:moderation:1017390327063134308> **Punishment**: `Ban User`", color=color)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
          await ctx.send(embed=embed)
     if module == 'antibot':
          embed=discord.Embed(title=f'Punishment — {module}', description=f"<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 seconds`\n<:moderation:1017390327063134308> **Punishment**: `Ban User & Bot`", color=color)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
          await ctx.send(embed=embed)
     if module == 'antiroleupdate' or module == "roleupdate":
          embed=discord.Embed(title=f'Punishment — {module}', description=f"<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 seconds`\n<:moderation:1017390327063134308> **Punishment**: `Ban User & Reset Roles`", color=color)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
          await ctx.send(embed=embed)
     if module == 'antirole' or module == 'rolecreate' or module == 'roledelete':
          embed=discord.Embed(title=f'Punishment — {module}', description=f"<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 seconds`\n<:moderation:1017390327063134308> **Punishment**: `Ban User`", color=color)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
          await ctx.send(embed=embed)
     if module == 'antichan' or module == 'antichannel' or module == 'chancreate' or module =='channeldelete' or module == 'channeldelete' or module == 'chandel' or module == 'channels':
          embed=discord.Embed(title=f'Punishment — {module}', description=f"<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 seconds`\n<:moderation:1017390327063134308> **Punishment**: `Ban User & Remake | Delete Channel`", color=color)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
          await ctx.send(embed=embed)
     if module == 'antiwebhook':
          embed=discord.Embed(title=f'Punishment — {module}', description=f"<:enabled:1021007058369261648> **Enabled**\n<:y_clock:1021013226718253087> **Rate**: `1`\n<:slowmode:1021013863044481026> **Threshold**: `2 seconds`\n<:moderation:1017390327063134308> **Punishment**: `Ban User`", color=color)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1021045113125871736/1023585476327788544/be7d50fb9c2d5baee38d0b32e3304391.jpg")
          await ctx.send(embed=embed)


async def main(): 
    await load()
    await client.start('MTAxNjQyNDU3ODMyMDQ0NTU3MA.Gpir5b.tUpDkbAvQzKYxrfXPoLwTFhe1h7uItIvvGnSOA')

asyncio.run(main())