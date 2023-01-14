import discord
from discord.ext import commands
import random
import pymongo
from unittest import skip
import requests
from discord.ext.commands import cooldown, BucketType
import sqlite3
import colorama
from colorama import Fore


color = 0x2f3136
jobs = ['Youtuber', 'Pornstar', 'Gamer', 'Developer', 'Photographer', 'Graphic Designer', 'Vfx Artist', 'Scammer', 'Drug Dealer', 'Janitor']
giver = ['Mia Khalifa', 'Mr Beast', 'khai', 'Mark Zukerberg', 'Elon Musk', 'Johnny Sins', 'Violet Myers', 'Pablo Escobar']

class economy(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.av = 'https://cdn.discordapp.com/attachments/1046007816571338792/1063772884914413598/f5c9023ededc5dda88f472d0c37e7fa7.jpg'
        print(f'{Fore.GREEN}[Status] Loaded Cog: Economy')


    """@commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS main (
            user_id INTEGER, wallet INTEGER, bank INTEGER
        )''')"""

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        try:
            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT user_id FROM main WHERE user_id = {message.author.id}")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO main(user_id, wallet, bank) VALUES (?, ?, ?)")
                val = (message.author.id, 100, 0)
                cursor.execute(sql, val)

            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print(e)

    @commands.command(aliases=['bal'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def balance(self, ctx, member : discord.Member = None):
        try:
            if member is None:
                member = ctx.author

                db = sqlite3.connect("eco.sqlite")
                cursor = db.cursor()

                cursor.execute(f"SELECT wallet, BANK FROM main WHERE user_id = {member.id}")
                bal = cursor.fetchone()
            try:
                wallet = bal[0]
                bank = bal[1]
            except:
                wallet = 0
                bank = 0

            embed=discord.Embed(color=color, description=f"<:under:1046032440457699428> **Networth:** `${wallet + bank}`\n<:under:1046032440457699428> **Wallet:** `${wallet}`\n<:under:1046032440457699428> **Bank:** `${bank}`")
            embed.set_author(name=f'{ctx.author.name}\'s balance', icon_url=ctx.author.avatar.url)
            await ctx.reply(embed=embed)
        except Exception as e:
            print(e)


    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def work(self, ctx, member : discord.Member = None):
        try:
            member = ctx.author
            earnings = random.randint(1, 600)

            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()

            cursor.execute(f"SELECT wallet FROM main WHERE user_id = {member.id}")
            wallet = cursor.fetchone()

            try:
                wallet = wallet[0]
            except:
                wallet = 0

            sql = ("UPDATE main SET wallet = ? WHERE user_id = ?")
            val = (wallet + int(earnings), member.id)
            cursor.execute(sql, val)

            embed=discord.Embed(color=color, description=f"<:bw_cashbag:1021067438521065483>  **You worked as a**  `{random.choice(jobs)}`  **just earned**  `${earnings}`")
            embed.set_author(name=f'{ctx.author.name}\'s balance', icon_url=ctx.author.avatar.url)
            await ctx.reply(embed=embed)

            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print(e)


    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def beg(self, ctx, member : discord.Member = None):
        try:
            member = ctx.author
            earnings = random.randint(1, 10)

            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()

            cursor.execute(f"SELECT wallet FROM main WHERE user_id = {member.id}")
            wallet = cursor.fetchone()

            try:
                wallet = wallet[0]
            except:
                wallet = 0

            sql = ("UPDATE main SET wallet = ? WHERE user_id = ?")
            val = (wallet + int(earnings), member.id)
            cursor.execute(sql, val)

            embed=discord.Embed(color=color, description=f"<:bw_cashbag:1021067438521065483>  `{random.choice(giver)}`  **gave you**  `${earnings}` 😂")
            embed.set_author(name=f'{ctx.author.name}\'s balance', icon_url=ctx.author.avatar.url)
            await ctx.reply(embed=embed)

            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print(e)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def gamble(self, ctx, amount: int):
        try:
            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()
            cursor.execute(f"SELECT wallet FROM main WHERE user_id = {ctx.message.author.id}")
            wallet = cursor.fetchone()
        
            try:
                wallet = wallet[0]
            except:
                wallet = 0

            if amount < 200:
                return await ctx.reply(embed=discord.Embed(color=color, description="**You need to have at least** `$200` 😂"))
            
            if wallet < amount:
                return await ctx.reply(embed=discord.Embed(color=color, description="**You dont have enough pooron** 😂"))
        
            user_strikes = random.randint(1, 15)
            bot_strikes = random.randint(5, 15)

            if user_strikes > bot_strikes:
                percentage = random.randint(50, 100)
                amount_won = int(amount * (percentage/100))

                cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet + amount_won, ctx.message.author.id))
                db.commit()

                embed = discord.Embed(color=color, description=f'<:under:1046032440457699428>  **Profit** `${amount_won}`\n<:under:1046032440457699428>  **Percentage** `{percentage}%`\n<:under:1046032440457699428>  **New Balance** `${wallet + amount_won}`')
                embed.set_author(name=f'{ctx.author.name} profit', icon_url=ctx.author.avatar.url)

            elif user_strikes < bot_strikes:
                percentage = random.randint(0, 80)
                amount_lost = int(amount * (percentage/100))

                cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet - amount_lost, ctx.message.author.id))
                db.commit()

                embed = discord.Embed(color=color, description=f'<:under:1046032440457699428>  **Loss** `${amount_lost}`\n<:under:1046032440457699428>  **Percentage** `{percentage}%`\n<:under:1046032440457699428>  **New Balance** `${wallet - amount_lost}`')
                embed.set_author(name=f'{ctx.author.name} loss', icon_url=ctx.author.avatar.url)
            
            else:
                embed=discord.Embed(color=color, description=f'<a:baby_slap:1018245289028636672>  **It was a tie**')
            
            embed.add_field(name=f"__{ctx.author.name}__", value=f'`{user_strikes}`')
            embed.add_field(name=f"__{ctx.bot.user.name}__", value=f'`{bot_strikes}`')
            await ctx.reply(embed=embed)

            cursor.close()
            db.close()
        except Exception as e:
            print(e)



    @commands.command(aliases=['dep'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def deposit(self, ctx, amount: int):
        try:
            db = sqlite3.connect("eco.sqlite")
            cursor = db.cursor()
            #cursor.execute(f"SELECT * FROM main WHERE user_id = {ctx.message.author.id}")

            data = cursor.fetchone()
            try:
                wallet = data[1]
                bank = data[2]
            except:
                pass

            if wallet < amount:
                await ctx.reply(embed=discord.Embed(color=color, description='**Insufficient Funds**'))

            else:
                cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank, + amount, ctx.author.id))
                cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet - amount, ctx.author.id))
                await ctx.reply(embed=discord.Embed(color=color, description=f'<:bw_cashbag:1021067438521065483> **You have deposited** `{amount}` **into your bank**'))
            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print(e)



    @commands.command(aliases=['wd'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def withdraw(self, ctx, amount: int):
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM main WHERE user_id = {ctx.message.author.id}")

        data = cursor.fetchone()
        try:
            wallet = data[1]
            bank = data[2]
        except:
            pass

        if bank < amount:
            return await ctx.reply(embed=discord.Embed(color=color, description='**Insufficient Funds**'))

        else:
            cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet + amount, ctx.message.author.id))
            cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank - amount, ctx.message.author.id))
            await ctx.reply(embed=discord.Embed(color=color, description=f'<:bw_cashbag:1021067438521065483> **You have withdrawn** `{amount}` **from your bank**'))
        db.commit()
        cursor.close()
        db.close()

async def setup(bot):
  await bot.add_cog(economy(bot))