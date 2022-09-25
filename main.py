from unittest import skip
import discord
from discord.ext import commands, tasks
import pymongo
import ast
from time import sleep
import random
import inspect
import re
import requests
import urllib
import datetime
import asyncio
import os
import json

mongoClient = pymongo.MongoClient('mongodb+srv://sinful:khaleed111@cluster0.i8qcd.mongodb.net/?retryWrites=true&w=majority')
db = mongoClient.get_database("apollo2").get_collection("whitelist")

client = commands.Bot(commands.when_mentioned_or(";"), intents=discord.Intents.all())
client.remove_command("help")

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

color = 0x2f3136
success = 0xA4FF00
error = 0xFF1A1A
baseurl = "http://ws.audioscrobbler.com/2.0/"
apikey = 'c5943b857416a9abc6440b042587c5a5'


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

@client.command(aliases=["h"])
@commands.cooldown(1,5, commands.BucketType.user)
async def help(ctx):
     embed1 = discord.Embed(description=f"""
> __**how-to use**__
use the emojis <:left:1017394327728705596> `&` <:right:1017394325476352032> to navigat through the help menu and to see different pages.
> __**modules**__
```
・anti-nuke
・anti-raid
・moderation
・fun
・utility
・welcome
・lastfm```
""", color=color)
     embed1.set_author(name="home page", icon_url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
     embed1.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")

     
     embed2 = discord.Embed(color=color)
     embed2.add_field(name="<:moderation:1017390327063134308> Moderation", value="""
`・ban [user]` **—** bans the mentioned user
`・kick [user]` **—** kicks the mentioned user
`・lock [channel]` **—** locks the channel
`・unlock [channel]` **—** unlocks the channel
`・mute [user]` **—** mutes the mentioned user
`・unmutes [user]` **—** unmutes the mentioned user
`・jail [user]` **—** jails the mentioned user [soon]
`・purge [amount]` **—** purges number of messages
`・clear [amount]` **—** clears number of messages
`・nuke` **—** recreates the server
`・slowmode [seconds]` **—** sets channel slowmode
`・offslowmode` **—** turns off channel slowmode
`・unban [ID]` **—** unbans the user ID
""")
     embed2.set_footer(text=f"Page 2 - apollo", icon_url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
     embed2.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")

     embed3 = discord.Embed(color=color)
     embed3.add_field(name="<a:Dancing:1017685291559039007> Fun", value="""
`・kiss [user]` **—** kisses the mentioned user
`・slap [user]` **—** slaps the mentioned user
`・hug [user]` **—** hugs the mentioned user
`・coinflip` **—** flips a coin
`・pat [user]` **—** pats the mentioned user
`・feed [user]` **—** feeds the mentioned user
""")
     embed3.set_footer(text=f"Page 3 - apollo", icon_url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
     embed3.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")

     embed4 = discord.Embed(color=color)
     embed4.add_field(name="<:bw_shield:1021067469399523449> Protection `[SOON]`", value="""
`・antinuke bans [limit]` **—** edits limit for antinuke trigger
`・toggle [module]` **—** turns the antinuke module on & off
`・whitelist [user]` **—** whitelists mentioned user
`・whitelisted` **—** shows whitelisted users
`・dewhitelist [user]` **—** removes user from whitelist
`・config` **—** shows the antinuke configuration
`・setup` **—** sets up apollo
""")
     embed4.set_footer(text=f"Page 4 - apollo", icon_url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
     embed4.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")

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
     embed5.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
     embed5.set_footer(text=f"Page 5 - apollo", icon_url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")


     embed6 = discord.Embed(color=color)
     embed6.add_field(name="<a:bearkiss:1018244723472871424> Apollo", value="""
`・invite` **—** sends bot invite links
`・gleave` **—** [`developer command`]
`・guilds` **—** [`developer command`]
`・botinfo` **—** sends apollos information
""") 
     embed6.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
     embed6.set_footer(text=f"Page 6 - apollo", icon_url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")

     embed7 = discord.Embed(color=color)
     embed7.add_field(name="<a:9850bluewelcome:1021087894837928056> Welcome `[SOON]`", value="""
`・welcome` **—** shows welcome information and help
`・welcome variables` **—** sends the welcome variables
`・welcome test` **—** shows what welcome msg would look like
""") 
     embed7.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
     embed7.set_footer(text=f"Page 7 - apollo", icon_url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")



     embed8 = discord.Embed(color=color)
     embed8.add_field(name="<:lastfm:1021442695362773002> LastFM", value="""

""") 
     embed8.set_thumbnail(url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")
     embed8.set_footer(text=f"Last Page - apollo", icon_url="https://media.discordapp.net/attachments/1021045113125871736/1021066452259840000/5f19278fe4d2ce277328fa8ad0449a5e.jpg?width=494&height=494")


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

async def main():
    await load()
    await client.start('MTAxNjQyNDU3ODMyMDQ0NTU3MA.Gpir5b.tUpDkbAvQzKYxrfXPoLwTFhe1h7uItIvvGnSOA')

asyncio.run(main())
