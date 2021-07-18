import discord
import json
import os
import random
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from .res import funcs as f

class monee(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command(aliases = ["balance", "monee"])
    async def bal(self, ctx, *args):
        await f.open_account(ctx.author)

        if len(args) >> 0:
            u = await f.is_user(ctx, " ".join(args))

        else:
            u = ctx.author

        await f.open_account(u)

        users = await f.get_bank_data()

        balance = users[str(u.id)]["bank"]
        
        if u == ctx.author:
            await ctx.send(embed = discord.Embed(description = "You currently have **{}** monee!".format(balance), colour = u.colour))
        
        else:
            await ctx.send(embed = discord.Embed(description = "{} currently has **{}** monee!".format(u.mention, balance), colour = u.colour))

    @commands.cooldown(1, 3600, BucketType.user)
    @commands.command()
    async def claim(self, ctx):
        await f.open_account(ctx.author)

        await f.add_money(ctx, ctx.author.id, 200)
        await ctx.send(embed = discord.Embed(description = "You claimed **200** monee!", colour = ctx.author.colour))
    
    @claim.error
    async def claim_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("You can only claim monee once every hour!")
    
    @commands.command(aliases = ["bet"])
    async def gamble(self, ctx, amount : int):
        await f.open_account(ctx.author)

        if not amount:
            return await ctx.send("You can't gamble nothing.")
        
        await f.open_account(ctx.author)
        users = await f.get_bank_data()
        balance = users[str(ctx.author.id)]["bank"]

        if abs(amount) > balance:
            return await ctx.send("You do not have enough monee to complete the gamble!")

        result = random.choice([True, False])
        
        if result == True:
            await ctx.send("💵 Good job, you are now feeding into a severe gambling addiction <:surreal:753369030827573338>!\n\t\t**+ {} monee.**".format(amount))
            await f.add_money(ctx, ctx.author.id, abs(amount))
        
        if result == False:
            await ctx.send("💸 Should've aimed smaller, there goes your lunch money <:sad:753369030831767622>.\n\t\t**- {} monee.**".format(amount))
            await f.take_money(ctx, ctx.author.id, abs(amount))

def setup(client):
    client.add_cog(monee(client))