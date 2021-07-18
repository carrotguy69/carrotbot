import discord

roles = {
    "Owner" : 806760016513597460,
    "Admin" : 855714737203707905,
    "SeniorMod" : 806758865642586122,
    "Mod" : 806758644791377940,
    "TrialMod" : 806758607545696278
}

async def get_staff_role(ctx, role):
    for key, value in roles.items():
        if key == role:
            return discord.utils.get(ctx.guild.roles, id = int(value))