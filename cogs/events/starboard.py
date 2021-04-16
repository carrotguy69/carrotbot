import discord
from discord.ext import commands

class starboard(commands.Cog):
  def __init__(self, client):
    self.client = client
    
    @commands.Cog.listener()
    on_raw_reaction_add(self, payload):
      if payload.emoji.name == "⭐":
        msg = payload.message
        
        embed = discord.Embed(title = "Starred Message", description = f"{[msg.content]()}")
        
        # fuck didnt finish
