import discord
import re
import json
import os
from fuzzywuzzy import process

async def cleanup_mention(string):
    """Get the ID of a mention."""
    return int(string.replace("@", "").replace("<", "").replace(">", "").replace("&", "").replace("!", ""))

async def is_user(ctx, string):
    """See if a string mentions/names a user."""

    if "@" and "<" and ">" and "!" in string: # there is a mention in the string

        c = await cleanup_mention(string)
        u = discord.utils.find(lambda m: m.id == int(c), ctx.guild.members) # Try and find the member. If there is no member with that ID, find() returns None.

        if u != None: # Make sure that this member exists before returning it.
            return u

    elif re.findall(r'\d+', string): # there are numbers in the string
        u2 = discord.utils.find(lambda m: m.id == int(string), ctx.guild.members) # If this is a user ID pasted, we want to use that.

        if u2 != None: # If it's not a user ID, find() returns None.
            return u2
        
        elif u2 == None: # There must be numbers in the username.
            return process.extractOne(string, ctx.guild.members)[0] # Compare the string argument to all members in the guild.
    
    elif not re.findall(r'\d+', string): # There are not numbers in the string.
        return process.extractOne(string, ctx.guild.members)[0] # Compare the string argument to all members in the guild.

async def time_convert(time):
    """Convert different units of time into raw seconds."""
    times = {"s" : 1, "m" : 60, "h" : 3600, "d" : 86400}
    
    try:
        return int(time[:-1]) * times[time[-1]]
    
    except:
        return time

async def get_bank_data():
    with open(os.path.join(os.path.dirname(__file__), 'bank.json'), "r") as f:
        users = json.load(f)
    
    return users

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["bank"] = 0
    
    with open(os.path.join(os.path.dirname(__file__), 'bank.json'), "w") as f:
        json.dump(users, f)
    
    return True

async def add_money(ctx, userid, amount : int):
    u = discord.utils.find(lambda m: m.id == userid, ctx.guild.members)

    users = await get_bank_data()

    users[str(u.id)]["bank"] += int(amount)

    with open(os.path.join(os.path.dirname(__file__), 'bank.json'), "w") as f:
        json.dump(users, f)

async def take_money(ctx, userid, amount : int):
    u = discord.utils.find(lambda m: m.id == userid, ctx.guild.members)

    users = await get_bank_data()

    users[str(u.id)]["bank"] += int(amount * -1)

    with open(os.path.join(os.path.dirname(__file__), 'bank.json'), "w") as f:
        json.dump(users, f)