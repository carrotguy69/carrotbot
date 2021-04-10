import discord, random, datetime
from discord.ext import commands

class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_any_role("Moderator", "Admin", "owner guy")
    @commands.command(aliases = ["ban"])
    async def banish(self, ctx, user : discord.Member, *, reason = None):
        staffrole = discord.utils.find(lambda r: r.id == 806757393378836480, ctx.guild.roles)

        if user.top_role.position => ctx.author.top_role.position:
            embed = discord.Embed(description = "You can't use that on **{}**, they're cooler than you!".format(user.name), colour = discord.Colour(0xFF4759))
            await ctx.send(embed = embed)
            return
        
        else:
            
            embed = discord.Embed(description = "On behalf of the cult leaders, you have been hereby banished from The Carrot Cult due to `{}`.".format(reason), colour = discord.Colour(0xFF4759))
            embed.add_field(value = "[Invite](https://discord.gg/QaPsH2c8kC)")
            embed.add_field(value = "[Appeal](https://forms.gle/Z7J2XgdgV4HHRRbP9)")
            
			try:
                await user.send(embed = embed)
				
            except:
                return
            
            await user.ban(reason = "Banned by {} | ".format(ctx.author, reason))
			await ctx.send("User Banned!")


def setup(client):
    client.add_cog(ban(client))
