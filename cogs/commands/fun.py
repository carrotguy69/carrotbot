from discord.ext import commands
from .res import funcs as f

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def echo(self, ctx, *, echo):
        if "@" not in echo:
            await ctx.message.delete()
            await ctx.send(echo)
        
        else:
            return

def setup(client):
    client.add_cog(moderation(client))