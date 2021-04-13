######################################################################################
#                                                                                    #
#   MIT License                                                                      #
#   Copyright © 2021 The Carrot Cult Developer Team                                  #
#   
#   Permission is hereby granted, free of charge, to any person obtaining a copy     #
#   of this software and associated documentation files (the "Software"), to deal    #
#   in the Software without restriction, including without limitation the rights     #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell        #
#   copies of the Software, and to permit persons to whom the Software is            #
#   furnished to do so, subject to the following conditions:                         #
#   The above copyright notice and this permission notice shall be included in all   #
#   copies or substantial portions of the Software.                                  #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR       #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,         #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE      # 
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER           #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,    #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE    #
#   SOFTWARE.                                                                        #
#                                                                                    #
######################################################################################
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
