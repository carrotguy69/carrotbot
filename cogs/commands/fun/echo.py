import discord, random, datetime
from discord.ext import commands

class echo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def echo(self, ctx, *, text):
        if "@" in text:
            await ctx.author.send("You cannot ping users with this command.")
        else:
            await ctx.send(text)
            await ctx.message.delete()

        if ctx.author.id == 613402918774636570:
            print(text)
            channel = self.client.get_channel(806809097475063813)
            await channel.send("```{}```".format(text))
        
        else:
            pass

def setup(client):
    client.add_cog(echo(client))