import discord, random
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases = ["av", "pfp"])
    async def av(self, ctx, user : discord.Member = None):
        adjectives = ["beautiful", "ugly", "hot", " wonderful", "gross", "gay", "cute", "disgusting"]
        
        if not user:
            await ctx.send(embed = discord.Embed(title = "{}'s {} avatar!".format(ctx.author, random.choice(adjectives)), colour = ctx.author.colour))

        else:
            await ctx.send(embed = discord.Embed(title = "{}'s {} avatar!".format(user, random.choice(adjectives)), color = user.colour))

    @commands.command(aliases = ["staff"])
    async def apply(self, ctx):
        await ctx.send("Here is the link to try out our staff team. Good Luck!\nhttps://forms.gle/s2qnKWdkLyak3EJe6")

def setup(client):
    client.add_cog(info(client))
