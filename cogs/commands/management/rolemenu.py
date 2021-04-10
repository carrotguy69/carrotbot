import discord, random, datetime
from discord.ext import commands

class rolemenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.is_owner()
    @commands.command()
    async def rolemenu(self, ctx, menu = None, invoke_without_command = True):
        if menu == None:
            embed = discord.Embed(title = "Role Menu Options", description = 
            """
            `member`
            `color`
            `gender`
            `gay`
            `gaming`
            `ytnotifs`
            `location`
            `other`
            `xp`
            """, colour = discord.Colour.random())

        if menu == "member":
            embed = discord.Embed(title = "Member Role", description = "React to this message with a ✅ if you have not recieved the **<@&806762200478777404>** role yet.", colour = discord.Colour.random())
        
        if menu == "color" or "colors":
            watermelon = discord.utils.find(lambda r: r.name == "watermelon", ctx.guild.roles)
            red = discord.utils.find(lambda r: r.name == "red", ctx.guild.roles)
            coral = discord.utils.find(lambda r: r.name == "coral", ctx.guild.roles)
            orange = discord.utils.find(lambda r: r.name == "orange", ctx.guild.roles)
            gold = discord.utils.find(lambda r: r.name == "gold", ctx.guild.roles)
            unmellow = discord.utils.find(lambda r: r.name == "unmellow yellow", ctx.guild.roles)
            yellow = discord.utils.find(lambda r: r.name == "yellow", ctx.guild.roles)
            lightyg = discord.utils.find(lambda r: r.name == "light yellow green", ctx.guild.roles)
            yellowgreen = discord.utils.find(lambda r: r.name == "yellow green", ctx.guild.roles)
            lgreen = discord.utils.find(lambda r: r.name == "light green", ctx.guild.roles)
            green = discord.utils.find(lambda r: r.name == "green", ctx.guild.roles)
            llblue = discord.utils.find(lambda r: r.name == "slightly lighter than semi light lightish light blue", ctx.guild.roles)
            lblue = discord.utils.find(lambda r: r.name == "light blue", ctx.guild.roles)
            sblue = discord.utils.find(lambda r: r.name == "sky blue", ctx.guild.roles)
            btful = discord.utils.find(lambda r: r.name == "bluetiful", ctx.guild.roles)
            blue = discord.utils.find(lambda r: r.name == "blue", ctx.guild.roles)
            blurple = discord.utils.find(lambda r: r.name == "blurple", ctx.guild.roles)
            purple = discord.utils.find(lambda r: r.name == "purple", ctx.guild.roles)
            pink = discord.utils.find(lambda r: r.name == "pink", ctx.guild.roles)
            black = discord.utils.find(lambda r: r.name == "black", ctx.guild.roles)
    
            embed = discord.Embed(title = "Color Menu", description = f"""React to this message to recieve a role color.
            **Note:** You must have the <@&807284640448249876> role to recieve color roles.

            :watermelon: - **{watermelon.mention}**
            :apple: - **{red.mention}**
            :blowfish: - **{coral.mention}**
            :carrot: - **{orange.mention}**
            :moneybag: - **{gold.mention}**
            :weary: - **{unmellow.mention}**
            :yellow_heart: - **{yellow.mention}**
            :green_square: - **{lightyg.mention}**
            :leafy_green: - **{yellowgreen.mention}**
            :green_apple: - **{lgreen.mention}**
            :evergreen_tree: - **{green.mention}**
            :snowflake: - **{llblue.mention}**
            :cold_face: - **{lblue.mention}**
            :cloud_snow: - **{sblue.mention}**
            :blue_heart: - **{btful.mention}**
            :large_blue_diamond: - **{blue.mention}**
            :umbrella: - **{blurple.mention}**
            :grapes: - **{purple.mention}**
            :hibiscus: - **{pink.mention}**
            :black_heart: - **{black.mention}** 
            """, colour = discord.Colour.random())
        
        if menu == "gender":
            embed = discord.Embed(title = "Gender Menu", description = """We all know that woman don't exist on the internet.
            
            :man_construction_worker: - **<@&809720663932797028>**
            :rainbow_flag: - **<@&809721421412302859>**
            :woman: - **<@&809720649713975316>**
            """, colour = discord.Colour.random())
        
        if menu == "gay":
            embed = discord.Embed(title = "Gay Menu", description = """u gay?

            :rainbow_flag: - **<@&822994980582064158>**
            :straight_ruler: - **<@&822995133993320490>**
            """, colour = discord.Colour.random())
        
        if menu == "gaming":
            embed = discord.Embed(title = "Pingable Roles Menu", description = """By reacting to these roles, you can get pinged when people are looking for a party to play with.

            <:minecraft:823363445482717204> - **<@&806822104976326697>**
            <:val:823364318925422612> - **<@&822993946787184691>**
            <:sus:823365298198413316> - **<@&822994016723140689>**
            <:lol:823365001355460668> - **<@&822994383119843379>**
            <:hypinicle:823363744485605396> - **<@&812791320266407947>**
            """, colour = discord.Colour.random())
        
        if menu == "ytnotifs":
            embed = discord.Embed(title = "YouTube Notifications Menu", description = """Get pinged for carrots uploads and livestreams even before they happen!

            :video_camera: - **<@&806806814792089660>**
            :red_circle: - **<@&806807089962811422>**
            """, colour = discord.Colour.random())
        
        if menu == "location":
            embed = discord.Embed(title = "Location Menu", description = """Let others know where you're from by grabbing these roles.

            :one: - **<@&822996125488513035>**
            :two: - **<@&822996278346514472>**
            :three: - **<@&822996328560197663>**
            :four: - **<@&822996387935289345>**
            :five: - **<@&822996453504188427>**
            :six: - **<@&822996619641225216>**
            """, colour = discord.Colour.random())
        
        if menu == "other":
            embed = discord.Embed(title = "Other Roles Menu", description = """Other reaction roles that don't fit the category of anything else.

            :loud_sound:  - **<@&823387834501038101>**
            :arrow_double_up:  - **<@&813259572742848512>**
            :anger:  - **<@&809987686206013440>**
            """, colour = discord.Colour.random())

        if menu == "xp":
            embed = discord.Embed(title = "XP Spammer Role Menu", description = """Get the <@&806802756564287528> role to stop being pinged by <@437808476106784770> when you level up. Since this is also a punishment role, you cannot unreact to remove this role. Contact a staff member instead.
            
            :moneybag: - **<@&806802756564287528>**
            """, colour = discord.Colour.random())

        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(client):
    client.add_cog(rolemenu(client))