import discord

guild = client.get_guild(726514695523008514)

roles = {
    "Owner" : 806760016513597460,
    "Developer" : 829543207821115483,
    "Admin" : 806758865642586122,
    "Moderator" : 806758644791377940,
    "Helper" : 806758607545696278,
    "Staff" : 806757393378836480,

    "Muted" : 813169496398364723,
    "Spammer" : 806802756564287528,

    "Watermelon" : 812976418031271956,
    "Red" : 812976418291449876,
    "Coral" : 812976418526986240,
    "Orange" : 812976418811019264,
    "Gold" : 812976418811019264,
    "UnmellowYellow" : 812976419377905714,
    "Yellow" : 812976419680157696,
    "LightGreen" :812976420002988092,
    "Lime" : 812976420556374036,
    "PastelGreen" : 812976420686659605,
    "Green" : 812976421358010398,
    "Aqua" : 812976421693554738,
    "SkyBlue" : 812976421973524501,
    "Cyan" : 812976422040633375,
    "Blue" : 812976423038877696,
    "LightBlue" : 812976422699925504,
    "Blurple" : 812976423391854592,
    "Pink" : 812976423836712961,
    "Black" : 821386198198779924,

    "Booster" : 755116692451098737,
    "Patreon" : 830915896951177236,

    "Level50" : 809690979601874947,
    "OG" : 758751899671068672,
    "Level30" : 807286536663203880,
    "Level20" : 807286345398878218,
    "Level10" : 807285434337067059,
    "Level5" : 807284640448249876,
    "Level1" : 807284215565254676,

    "ur_MUUM" : 830107325490528268,
    "living_carrot_advert" : 830094194550243438,

    "Robot" : 806762322998853654,
    "Arcane" : 806788585558376480,
    "Carl" : 806806391217192962,
    "CoolColors" : 812972218598424587,
    "Memer" : 806790082828566569,
    "Dyno" : 806792078427422722,
    "CarrotBot" : 815757090185543711,
    "BumpRemind" : 807157107387924482,
    "Rythym" : 807017708934791189,
    "Rythym2" : 817143623233699871,
    "Mee6" : 817247633801347073,
    "Groovy" : 817247741762732055,
    "DiscordServers" : 812778773983920149,
    "YAGPDBxyz" : 821572812761202689,
    "DiscordMe" : 812779779890610239,
    "DiscordServerList" : 807010403359653889,
    "Hystats" : 832131738716864523,

    "UploadNotifications" : 806806814792089660,
    "LivestreamNotifications" : 806807089962811422,
    "DeadChatNotifications" : 806807089962811422,
    "BumpNotification" : 813259572742848512,
    "HypixelPing" : 812791320266407947,
    "SMPPing" : 806822104976326697,
    "ValorantPing" : 822993946787184691,
    "AmongUsPing" : 822994383119843379,
    "Male" : 809720663932797028,
    "Other" : 809721421412302859,
    "Female" : 809720649713975316,
    "Gay" : 822994980582064158,
    "Straight" : 822995133993320490,
    "NAmerica" : 822996125488513035,
    "SAmerica" : 822996278346514472,
    "Africa" : 822996328560197663,
    "Europe" : 822996453504188427,
    "Asia" : 822996453504188427,
    "Australlia" : 822996619641225216,

    "Member" : 806762200478777404,
    "Everyone" : 726514695523008514
}

def find_role(role):
    for key, value in roles.items():
        if key == role:
            return discord.utils.find(lambda r: r.id == value, guild.roles)