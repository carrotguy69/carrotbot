import discord, asyncio, os
from discord.ext import commands
from discord import Activity, ActivityType

client = commands.Bot(command_prefix=";", intents = discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print(f"* Online")
    await client.change_presence(status =  discord.Status.online, activity = Activity(type = ActivityType.watching, name = "Type ;help"))
    
extensions = [
            "cogs.commands.fun.echo", 
            "cogs.commands.moderation.mute", 
            "cogs.events.welcome", 
            "cogs.commands.moderation.nick", 
            "cogs.commands.info.git",
            "cogs.commands.info.helpcmd",
            "cogs.events.errors"
            ]

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)
        print("+ loaded extension {}".format(ext))


def read_token():
    token = open(os.path.join(os.path.dirname(__file__), "token.txt")).readlines()
    return token[0].strip()

token = read_token()

client.run(token, bot = True, reconnect = True)
