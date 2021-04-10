import discord, asyncio, os
from discord.ext import commands

client = commands.Bot(command_prefix=";", intents = discord.Intents.all())
version = "3.0"

@client.event
async def on_ready():
    print(f"* Running carrotbot v.{version}")
    client.remove_command('help')

extensions = ["cogs.commands.fun.echo", "cogs.commands.moderation.mute", "cogs.events.welcome"]

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)
        print("+ loaded extension {}".format(ext))


def read_token():
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, "token.txt")
    tfile = open(filename)
    token = tfile.readlines()
    return token[0].strip()

token = read_token()

client.run(token, bot = True, reconnect = True)