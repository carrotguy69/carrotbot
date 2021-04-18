import discord, resources
from discord.ext import commands

class stars(commands.Cog):
	def __init__(self, client):
		self.client = client
    
	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		print("a")
		starboard = resources.channels.grab_channel("Starboard")

		if payload.emoji.name == "⭐":
			msg = await self.client.get_channel(payload.channel.id).fetch_message(payload.message_id)

			if msg.content:
				embed = discord.Embed(description = f"{msg.content}\n[Jump!](msg.jump_url)", colour = discord.Colour(0xff8b00))
				embed.set_author(name = msg.author.name, icon_url = msg.author.avatar_url)
				embed.set_footer(f"🌟 New starred message ⭐")

				if len(msg.attatchments):
					embed.set_image(url = msg.attatchments[0].url)

	
			else:
				embed = discord.Embed(colour = discord.Colour(0xff8b00))
				embed.set_image(url = msg.attatchments[0].url)
				embed.set_footer(f"⭐ New starred message 🌟")

				await starboard.send(embed = embed)
			
			await starboard.send(embed = embed)

def setup(client):
	client.add_cog(stars(client))
