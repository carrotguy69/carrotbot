import discord, random, datetime, asyncio
from discord.ext import commands

class onmsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.guild_only()
    @commands.Cog.listener()
    async def on_message(self, message):
        
        #basically stops you from using dank memer in channels
        if message.content.startswith("pls"):
            if message.channel.id != 806738009931776010:
                await message.channel.send("Hey broski, Dank Memer is disabled in this channel. Try using <#806738009931776010> instead.")
        
        #says hi back
        if message.content.startswith("hi" or "hello"):
            await asyncio.sleep(1)
            hellochat = ["https://tenor.com/view/hello-chat-gif-21073786", "https://tenor.com/view/youtube-twitch-meme-chair-office-gif-19928140", "https://tenor.com/view/hello-chat-big-chungus-meme-roblox-fat-gif-20170607", "https://tenor.com/view/hello-chat-hello-marvel-thanos-portal-gif-20110933", "https://tenor.com/view/hello-chat-phantom-forces-roblox-gif-20662777", "https://tenor.com/view/hello-chat-hello-agent-jonsey-jonsey-fortnite-gif-20110941", "https://tenor.com/view/hello-chat-kin-planet-gif-20744793", "https://tenor.com/view/hi-chat-gif-20883935"]
            await message.channel.send(random.choice(hellochat))
        
        else:
            return

        await self.client.process_commands(message)

def setup(client):
    client.add_cog(onmsg(client))