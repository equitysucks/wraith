import discord

from discord.ext import commands
from unittest import skip
from discord.ext.commands import cooldown, BucketType


color = 0x2f3136


class help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.av = 'https://cdn.discordapp.com/attachments/1046007816571338792/1063772884914413598/f5c9023ededc5dda88f472d0c37e7fa7.jpg'
        print('[Status] Loaded Cog: Help')



    @commands.group(name='help', aliases=['h'], invoke_without_command=True)
    @commands.cooldown(1,5, commands.BucketType.user)
    async def help(self, ctx):
            embed1 = discord.Embed(description=f"""
        __**how-to use**__
        use the `emojis` <:left:1017394327728705596> `&` <:right:1017394325476352032> to navigate through the help menu to see different pages or you can do `;help [module]`, type `;modules` to see my available modules.
        __**need help ?**__
        if help is needed in any way possible join my support [__**server**__](https://discord.gg/K7F3cGYYkr)
        """, color=color)
            embed1.set_footer(text=f"{len(self.client.commands)} commands")
            embed1.set_author(name="home page", icon_url=self.av)
            
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
        `・nuke` **—** clears the channel
        `・slowmode [seconds]` **—** sets channel slowmode
        `・offslowmode` **—** turns off channel slowmode
        `・unban [ID]` **—** unbans the user ID
        """)
            embed2.set_footer(text=f"page 2 - wrath")
            embed3 = discord.Embed(color=color)
            embed3.add_field(name="<a:Dancing:1017685291559039007> Fun", value="""
        `・kiss [user]` **—** kisses the mentioned user
        `・slap [user]` **—** slaps the mentioned user
        `・hug [user]` **—** hugs the mentioned user
        `・coinflip` **—** flips a coin
        `・pat [user]` **—** pats the mentioned user
        `・feed [user]` **—** feeds the mentioned user
        `・hacks [user]` **—** fake hacks the mentioned user
        `・randnum` **—** sends a random number between 1 - 100
        """)
            embed3.set_footer(text=f"page 3 - wrath")
            embed4 = discord.Embed(color=color)
            embed4 = discord.Embed(color=color)
            embed4.add_field(name="<:tkt:1062796583760056360> Tickets [`SOON`]", value="""
        `・placeholding` **—** placeholding for now
        """)
            embed4.set_footer(text=f"page 4 - wrath")
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
        `・permissions [user]` **—** shows the users perms
        `・modules` **—** shows all of wrath modules
        `・roleinfo [role]` **—** shows the role info
        `・afk [mins]` **—** sets ur afk
        `・emojidelete` **—** deletes emoji
        `・serverbanner` **—** shows the server banner
        `・servericon` **—** shows the servericon
        `・serverid` **—** sends the server id
        `・memberid` **—** sends the mentioned members id
        `・spotify` **—** shows the users spotify activity
        `・commandcount` **—** senjds amount of commands
        """) 
            embed5.set_footer(text=f"page 5 - wrath")
            embed6 = discord.Embed(color=color)
            embed6.add_field(name="<a:bearkiss:1018244723472871424> wrath", value="""
        `・invite` **—** sends bot invite links
        `・gleave` **—** [`developer command`]
        `・guilds` **—** [`developer command`]
        `・botinfo` **—** sends wraths information
        """) 
            embed6.set_footer(text=f"page 6 - wrath")
            embed7 = discord.Embed(color=color)
            embed7.add_field(name="<a:9850bluewelcome:1021087894837928056> Welcome", value="""
        `・welcome` **—** shows welcome information and help
        `・welcome variables` **—** sends the welcome variables
        `・welcome test` **—** shows what welcome msg would look like
        `・welcchan [chan]` **—** sets the welcome channel
        `・welcmsg [msg]` **—** sets the welcome message
        """) 
            embed8 = discord.Embed(color=color)
            embed8.add_field(name="<:bw_cashbag:1021067438521065483> Economy", value="""
        `・balance [user]` **—** shows the mentioned users balance
        `・work` **—** lets you work and gain money
        `・beg` **—** begs for money
        `・gamble [amount]` **—** gambles an amount of money
        `・withdraw [amount]` **—** withdraws an amount of money
        `・deposit [amount]` **—** deposits an amount of money
        """) 
            embed8.set_footer(text=f"last page - wraith")
            pages = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8]
            message = await ctx.reply(embed = embed1) 
        
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
                    reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                    await message.remove_reaction(reaction, user)
                except:
                    pass
                    await message.clear_reaction()



    @help.command(aliases=['mod'])
    async def moderation(self, ctx):
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
    `・nuke` **—** clears the channel
    `・slowmode [seconds]` **—** sets channel slowmode
    `・offslowmode` **—** turns off channel slowmode
    `・unban [ID]` **—** unbans the user ID
    """)
        embed.set_footer(text=f"moderation - wrath")
        await ctx.reply(embed=embed)


    @help.command()
    async def fun(self, ctx):
        embed3 = discord.Embed(color=color)
        embed3.add_field(name="<a:Dancing:1017685291559039007> Fun", value="""
    `・kiss [user]` **—** kisses the mentioned user
    `・slap [user]` **—** slaps the mentioned user
    `・hug [user]` **—** hugs the mentioned user
    `・coinflip` **—** flips a coin
    `・pat [user]` **—** pats the mentioned user
    `・feed [user]` **—** feeds the mentioned user
    `・hacks [user]` **—** fake hacks the mentioned user
    `・randnum` **—** sends a random number between 1 - 100
    """)
        embed3.set_footer(text=f"fun - wrath")
        await ctx.reply(embed=embed3)


    @help.command(aliases=['ticket', 'tkt'])
    async def tickets(self, ctx):
        embed4 = discord.Embed(color=color)
        embed4.add_field(name="<:bw_shield:1021067469399523449> Levels <:9803upvoteicon:1053036284823740616>", value="""
    `・set [module] [limit]` **—** edits limit for antinuke trigger
    `・toggle [module]` **—** turns the antinuke module on & off
    `・whitelist [user]` **—** whitelists mentioned user
    `・punishment [module]` **—** shows the modules punishment
    `・whitelisted` **—** shows whitelisted users
    `・dewhitelist [user]` **—** removes user from whitelist
    `・config` **—** shows the antinuke configuration
    `・setup` **—** sets up wrath
    """)
        embed4.set_footer(text=f"protection - wrath")
        await ctx.reply(embed=embed4)


    @help.command(aliases=['util'])
    async def utility(self, ctx):
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
    `・permissions [user]` **—** shows the users perms
    `・modules` **—** shows all of wrath modules
    `・roleinfo [role]` **—** shows the role info
    `・afk [mins]` **—** sets ur afk
    `・emojidelete` **—** deletes emoji
    `・serverbanner` **—** shows the server banner
    `・servericon` **—** shows the servericon
    `・serverid` **—** sends the server id
    `・memberid` **—** sends the mentioned members id
    `・spotify` **—** shows the users spotify activity
    `・commandcount` **—** sends amount of commands
    """) 
        embed5.set_footer(text=f"utility - wrath")
        await ctx.reply(embed=embed5)


    @help.command()
    async def wrath(self, ctx):
        embed6 = discord.Embed(color=color)
        embed6.add_field(name="<a:bearkiss:1018244723472871424> wrath", value="""
    `・invite` **—** sends bot invite links
    `・gleave` **—** [`developer command`]
    `・guilds` **—** [`developer command`]
    `・botinfo` **—** sends wraths information
    """) 
        embed6.set_footer(text=f"wrath")
        await ctx.reply(embed=embed6)


    @help.command(aliases=['welc'])
    async def welcome(self, ctx):
        embed7 = discord.Embed(color=color)
        embed7.add_field(name="<a:9850bluewelcome:1021087894837928056> Welcome", value="""
    `・welcome` **—** shows welcome information and help
    `・welcome variables` **—** sends the welcome variables
    `・welcome test` **—** shows what welcome msg would look like
    `・welc chan [chan]` **—** sets the welcome channel
    `・welc msg [msg]` **—** sets the welcome message
    """) 
        embed7.set_footer(text=f"welcome - wrath")
        await ctx.reply(embed = embed7)


    @help.command(aliases=['econ'])
    async def economy(self, ctx):
        embed8 = discord.Embed(color=color)
        embed8.add_field(name="<:bw_cashbag:1021067438521065483> Economy", value="""
    `・balance [user]` **—** shows the mentioned users balance
    `・work` **—** lets you work and gain money
    `・beg` **—** begs for money
    `・gamble [amount]` **—** gambles an amount of money
    `・withdraw [amount]` **—** withdraws an amount of money
    `・deposit [amount]` **—** deposits an amount of money
    """) 
        embed8.set_footer(text=f"last page - wrath")
        await ctx.reply(embed=embed8)

async def setup(bot):
  await bot.add_cog(help(bot))