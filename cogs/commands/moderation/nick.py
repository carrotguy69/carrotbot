import discord, datetime, asyncio
from discord.ext import commands

class nickname(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nick(self, ctx, obj, *, nickname):
        print(obj)
        if "<" and ">" and "@" in obj:
            
            if "&" in obj:
                roleid = obj.replace("&", "").replace("<", "").replace(">", "").replace("@", "")
                role = discord.utils.find(lambda r: r.id == int(roleid), ctx.guild.roles)
                
                embed = discord.Embed(title = "Working on it...", colour = discord.Colour(0x00FFD0))
                msg = await ctx.send(embed = embed)
                
                updates = 0
                errors = 0

                for user in role.members:
                    try:
                        await user.edit(nick = nickname)
                        updates += 1
                        await msg.edit(discord.Embed(title = "Working on it...", description = f"Updating **{updates}** users... | **{errors}** Error(s)", colour = discord.Colour(0x00FFD0)))
                    
                    except discord.errors.Forbidden:
                        errors += 1
                        return


                await msg.edit(title = "Done!", description = f"**Succesfully updated {updates} users!**", colour = discord.Colour(0x72FF56))
            
            if "!" in obj:
            
                userid = obj.replace("<", "").replace(">", "").replace("@", "")
                user = discord.utils.find(lambda m: m.id == userid, ctx.guild.members)

                embed = discord.Embed(title = "Working on it...", colour = discord.Colour(0x00FFD0))
                msg = await ctx.send(embed = embed)
                
                if nickname != "None" or "none":
                    await user.edit(nick = nickname)
                
                else:
                    await user.edit(nick = None)
                
                await msg.edit(embed = discord.Embed(title = "Done!", description = f"**Succesfully updated {updates} users!**", colour = discord.Colour(0x72FF56)))
        else:
            await ctx.send("**Invalid usage!**\nPlease use the format: `;nick <usermention/rolemention> <nickname>`")

def setup(client):
    client.add_cog(nickname(client))