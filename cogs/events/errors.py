import discord
from discord.ext import commands

class errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            return await ctx.send("This command cannot be used in private messages!")

def setup(client):
    client.add_cog(errors(client))