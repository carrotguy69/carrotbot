import discord, os

class automod(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(msg):
        
        bad = ["faggot", "nigga", "nigger", "fag", "n1gga", "nibba", "nibber", "carrot is bad"]

        for i in bad:
            if bad in msg.content.lower:
                await msg.delete

def setup(client):
    client.add_cog(automod(client))