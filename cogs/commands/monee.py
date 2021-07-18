import discord
import random
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from .res import funcs as f

class monee(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command(aliases = ["balance", "monee"])
    async def bal(self, ctx, user = None):
        await f.open_account(ctx.author)

        if user:
            u = await f.is_user(ctx, user)

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
    @commands.command(aliases = ["work"])
    async def claim(self, ctx):
        await f.open_account(ctx.author)

        await f.add_money(ctx, ctx.author.id, 200)
        await ctx.send(embed = discord.Embed(description = "💵 You claimed your hourly bonus <:coolandswift:763930720816463883>!\n**+ 200 monee.**", colour = ctx.author.colour))
    
    @claim.error
    async def claim_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("You can only claim monee once every hour!")
    
    @commands.command(aliases = ["bet"])
    async def gamble(self, ctx, amount : int):
        await f.open_account(ctx.author)

        if not amount:
            return await ctx.send("You can't gamble nothing.")
        
        users = await f.get_bank_data()
        balance = users[str(ctx.author.id)]["bank"]

        if abs(amount) > balance:
            return await ctx.send("You do not have enough monee to complete the gamble!")

        result = random.choice([True, False])
        
        if result == True:
            await ctx.send(embed = discord.Embed(description = "💵 Good job, you are now feeding into a severe gambling addiction <:surreal:753369030827573338>!\n**+ {} monee.**".format(amount), colour = discord.Colour(0x1DA300)))
            await f.add_money(ctx, ctx.author.id, abs(amount))
        
        if result == False:
            await ctx.send(embed = discord.Embed(description = "💸 Should've aimed smaller, there goes your lunch money <:sad:753369030831767622>.\n**- {} monee.**".format(amount), colour = discord.Colour(0xFF1000)))
            await f.take_money(ctx, ctx.author.id, abs(amount))

    @commands.command(aliases = ["gift", "give"])
    async def pay(self, ctx, user, amount : int):
        await f.open_account(ctx.author)
        users = await f.get_bank_data()
        balance = users[str(ctx.author.id)]["bank"]
        u = await f.is_user(ctx, user)
        await f.open_account(u)
        
        
        if abs(amount) > balance:
            return await ctx.send("You do not have enough monee to complete the payment!")
        
        if u == ctx.author:
            return await ctx.send("You can't pay yourself silly!")
        
        await f.take_money(ctx, ctx.author.id, abs(amount))
        await f.add_money(ctx, u.id, abs(amount))

        await ctx.send(embed = discord.Embed(description = "You payed **{}** `{}` monee!".format(u.name, amount), colour = u.colour))
        
        try:
            await u.send("**{}** has payed you `{}` monee!".format(ctx.author.name, abs(amount)))
        
        except:
            await ctx.send("{}\n**{}** has payed you `{}` monee!".format(u.mention, ctx.author.name, abs(amount)))

    @commands.command(aliases = ["steal"])
    async def rob(self, ctx, user):
        await f.open_account(ctx.author)
        users = await f.get_bank_data()
        balance = users[str(ctx.author.id)]["bank"]
        u = await f.is_user(ctx, user)
        await f.open_account(u)
        userbal = users[str(u.id)]["bank"]

        if balance < 500:
            return await ctx.send("You'll go broke! You need at least 500 coins to rob someone.")

        if u == ctx.author:
            return await ctx.send("Why would you rob yourself?")
        
        if userbal < 1000:
            return await ctx.send("This user has less than 500 coins. Why would you rob such a poor man?")
        
        result = random.choice([True, False])
        rob_amount = round(userbal/random.randint(10, 30))

        if result == True:
            await ctx.send(embed = discord.Embed(colour = ctx.author.colour, description = f"You successfully robbed **{u.name}** for `{rob_amount}` monee!"))
            await f.take_money(ctx, u.id, rob_amount)
            await f.add_money(ctx, ctx.author.id, rob_amount)
        
        if result == False:
            await ctx.send(embed = discord.Embed(colour = discord.Colour(0x1DA300), description = "Your scheme has failed, {}. The fed bois caught you in the act, and you had to pay 500 monee to escape from prison.".format(ctx.author.display_name)))
            await f.take_money(ctx, u.id, 500)




def setup(client):
    client.add_cog(monee(client))
