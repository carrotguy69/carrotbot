import discord, datetime, asyncio
from discord.ext import commands
from res.timeconverter import convert

class slowmode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_role("Administrators")
    @commands.command(aliase = ["cooldown", "slow"])
    async def slowmode(self, ctx, slowmode, channel : discord.TextChannel = None):
        
        time = await convert(slowmode)

        if not channel:
            await ctx.channel.edit(slowmode_delay = time)
            await ctx.send(f"Slowmode cooldown in {ctx.channel.mention} set to `{time}` seconds!")
        
        elif channel:
            await channel.edit(slowmode_delay = time)
            await ctx.send(f"Slowmode cooldown in {channel.mention} set to `{time}` seconds!")
        
        


def setup(client):
    client.add_cog(slowmode(client))