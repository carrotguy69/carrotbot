import discord, random, datetime
from discord.ext import commands

class mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_any_role("Staff", "Helper", "Moderator", "Admin", "owner guy")
    @commands.command()
    async def mute(self, ctx, user : discord.Member, *, reason = None):
        commander = ctx.author
        muterole = discord.utils.find(lambda r: r.id == 813169496398364723, ctx.guild.roles)
        staffrole = discord.utils.find(lambda r: r.id == 806757393378836480, ctx.guild.roles)
        
        if staffrole in user.roles:
            embed = discord.Embed(description = "You can't use that on **{}**, they're immortal!".format(user.name), colour = discord.Colour(0xFF4759))
            await ctx.send(embed = embed)
            return
        
        elif staffrole not in user.roles:

            if user == commander:
                embed = discord.Embed(description = "Why would you want to mute yourself?", colour = discord.Colour(0xFF4759))
                await ctx.send(embed = embed)
            
            if muterole in user.roles:
                await user.remove_roles(muterole)
                await user.add_roles(muterole)
                embed = discord.Embed(description = "**{}** is already muted.".format(user.name), colour = discord.Colour(0xFF4759))
                await ctx.send(embed = embed)
                
                for ctx.channel in ctx.guild.channels:
                    await channel.set_permissions(muterole, send_messages = False, add_reactions = False, connect = False, speak = False)
            
            if muterole not in user.roles:
                await user.add_roles(muterole)

                embed = discord.Embed(description = "**{}** has been muted.".format(user.name), colour = discord.Colour(0x71FF5E))
                await ctx.send(embed = embed)

    @commands.has_any_role("Staff", "Helper", "Moderator", "Admin", "owner guy")
    @commands.command()
    async def unmute(self, ctx, user : discord.Member, *, reason = None):
        commander = ctx.author
        muterole = discord.utils.find(lambda r: r.id == 813169496398364723, ctx.guild.roles)
        
        if muterole in user.roles:
           
            await user.remove_roles(muterole)
            embed = discord.Embed(description = "**{}** has been unmuted.".format(user.name), colour = discord.Colour(0x71FF5E))
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(description = "**{}** is not muted stupid 🤣!!!!".format(user.name), colour = discord.Colour(0xFF4759))
            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(mute(client))