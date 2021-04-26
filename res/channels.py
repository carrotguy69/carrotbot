import discord
from discord.ext import commands

Channels = {
    "Welcome" : 806744726509322280,
    "Rules" : 806739928469209140,
    "Roles" : 809720168238415882,
    "Announcements" : 806729953516847104,
    "Uploads" : 806744613183684629,
    "Git" : 806801435844280381,
    "Starboard" : 831394922540040274,

    "General" : 806735939762257920,
    "Bots" : 806738009931776010,
    "Memes" : 806737887076941824,
    "Adverts" : 807153854277222420,
    "Parties" : 812791065748439060,
    "Hell" : 835989628036055121,

    "VCChat" : 818908744196292659,
    "LargeBoi" : 808250201026330645,
    "MediumBoi" : 808250719948898306,
    "TinyBoi" : 808251375188312104,

    "Staff" : 806799145717202994,
    "Admins" : 808043476838252555,
    "Trello" : 813858891049205800,
    "StaffRules" : 806803004262318102,
    "Invites" : 813150420104118343,
    "Logs" : 806809097475063813,
    "Notes" : 744366589868245032,
    "StaffVC" : 815781718270148670
}

def grab_channel(channel):
    """An easy way to get guild channels!"""
    for key, value in Channels.items():
        if key == Channels:
            return self.client.get_channel(value)
