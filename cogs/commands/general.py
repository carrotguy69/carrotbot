# do not deploy till bitly credentials are removed

import discord 
import random
import requests
import urllib.request
import re
from discord.ext import commands
from bs4 import BeautifulSoup
from urllib.request import urlopen
from .res import funcs as f

prefix = "^"

class general(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["av", "pfp"])
    async def avatar(self, ctx, user):
        adjectives = ["beautiful", "ugly", "hot", " wonderful", "gross", "gay", "cute", "disgusting"]
        
        u = await f.is_user(ctx, user)

        if not u:
            embed = discord.Embed(title = "{}'s {} avatar!".format(ctx.author, random.choice(adjectives)), color = ctx.author.colour)
            embed.set_image(url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        
        else:
            embed = discord.Embed(title = "{}'s {} avatar!".format(u, random.choice(adjectives)), color = u.colour)
            embed.set_image(url = u.avatar_url)
            await ctx.send(embed = embed)
    
    @commands.command(aliases = ["old", "archived", "oldvideo"])
    async def oldvid(self, ctx):
        archives = ["https://www.youtube.com/watch?v=Xxx7u0sUdUw", "https://www.youtube.com/watch?v=Udw2CroGsmk", "https://www.youtube.com/watch?v=8gDWg0_EXrU", "https://www.youtube.com/watch?v=i6rUTD0G5HA", "https://www.youtube.com/watch?v=MW8F0-9diu8", "https://www.youtube.com/watch?v=PGzoSpB3V58", "https://www.youtube.com/watch?v=sxBjqANiU_A", "https://www.youtube.com/watch?v=2X35scjhZXo", "https://www.youtube.com/watch?v=enb6oARRI-o", "https://www.youtube.com/watch?v=SBixbuj82JQ", "https://www.youtube.com/watch?v=dpanxlDHt0M", "https://www.youtube.com/watch?v=qbJz9qYBcKg", "https://www.youtube.com/watch?v=KDt-7j6aQrQ", "https://www.youtube.com/watch?v=c-USlHvcc3k"]
        await ctx.send("Here is your random video: " + random.choice(archives))

    @commands.command(aliases = ["staff"])
    async def apply(self, ctx):
        await ctx.send("Here is the link to try out our staff team. Good Luck!\nhttps://forms.gle/s2qnKWdkLyak3EJe6")
    
    @commands.command(aliases = ["shortenurl", "shorturl", "url", "link"])
    async def bitly(self, ctx, link = None):
        username = ""
        password = ""

        auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth = (username, password))
        
        if auth_res.status_code == 200:
            access_token = auth_res.content.decode()

        headers = {"Authorization": f"Bearer {access_token}"}

        groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers = headers)
        
        if groups_res.status_code == 200:
            groups_data = groups_res.json()['groups'][0]
            guid = groups_data['guid']
        
        url = link

        shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers = headers)
        
        if shorten_res.status_code == 200:

            link = shorten_res.json().get("link")
            await ctx.send("Shortened URL: {}".format(link))

    @commands.command(aliases = ["channel", "textchannel"])
    async def channelinfo(self, ctx, channel : discord.TextChannel = None):
        
        if channel:
            embed = discord.Embed(title = f"#{channel.name}", description = f"Showing info for <#{channel.id}>.", color = ctx.author.colour)
            embed.add_field(name = "Name", value = channel.name)
            embed.add_field(name = "ID", value = channel.id)
            embed.add_field(name = "Category", value = channel.category)
            embed.add_field(name = "Creation date", value = channel.created_at.strftime("%x"))
            msg = await channel.fetch_message(channel.last_message_id)
            embed.add_field(name = "Last message", value = f'**[Jump!]({msg.jump_url})**')
            embed.add_field(name = "Members", value = len(channel.members))
            embed.add_field(name = "Position", value = channel.position)
            embed.add_field(name = "Slowmode delay", value = channel.slowmode_delay)
            embed.add_field(name = "Topic", value = channel.topic)
            await ctx.send(embed = embed)

        if not channel:
            embed = discord.Embed(title = f"#{ctx.channel.name}", description = f"Showing info for <#{ctx.channel.id}>.", color = ctx.author.colour)
            embed.add_field(name = "Name", value = ctx.channel.name)
            embed.add_field(name = "ID", value = ctx.channel.id)
            embed.add_field(name = "Category", value = ctx.channel.category)
            embed.add_field(name = "Creation date", value = ctx.channel.created_at.strftime("%x"))
            msg = await ctx.channel.fetch_message(ctx.channel.last_message_id)
            embed.add_field(name = "Last message", value = f'**[Jump!]({msg.jump_url})**')
            embed.add_field(name = "Members", value = len(ctx.channel.members))
            embed.add_field(name = "Position", value = ctx.channel.position)
            embed.add_field(name = "Slowmode delay", value = ctx.channel.slowmode_delay)
            embed.add_field(name = "Topic", value = ctx.channel.topic)
            await ctx.send(embed = embed)

    @commands.command(aliases = ["bot", "info"], invoke_without_command = True)
    async def help(self, ctx):
        await ctx.send(embed = discord.Embed(title = "carrotbot", colour = ctx.author.color, description = "a guild specific, multi-purpose bot made in Python3\n\n**Prefix:** `{}`\n**Developer:** carrot#0890\n**Other Links**: [GitHub](https://github.com/carrotguy69/carrotbot), [Command List](https://carrotguy69.github.io/carrotbot)".format(prefix)))

    @commands.command(aliases = ["search", "web"])
    async def google(self, ctx, *, search_query):
        from googlesearch import search

        msg = await ctx.send("Searching...")
        embed = discord.Embed(title = 'Search results for "{}"'.format(search_query), colour = ctx.author.color)
        
        query = search_query
        resultnum = 0

        try:
            for j in search(query, tld = "co.in", num = 3, stop = 3, pause = 1):
                resultnum += 1
                reqs = requests.get(j)
                soup = BeautifulSoup(reqs.text, 'html.parser')

                for title in soup.find_all('title'):
                    title = title.get_text()

                    embed.add_field(name = f"{title}", value = f"[Follow link!]({j})")
        
        except requests.exceptions.ConnectionError:
            await msg.edit("Connection aborted, RemoteDisconnected (Remote end closed connection without response)") 
            
        
        await msg.edit(embed = embed, content = " ")

    @commands.command(aliases = ["github", "repo"])
    async def git(self, ctx):
        await ctx.send(embed = discord.Embed(title = "Here you go!", description = "[GitHub Repo](https://github.com/carrotguy69/carrotbot)"))

    @commands.command(aliases = ["members", "usercount", "users"])
    async def membercount(self, ctx):
        embed = discord.Embed(title = ctx.guild.name, colour = ctx.author.color)
        embed.add_field(name = "All Users", value = len(ctx.guild.members))
        embed.add_field(name = "Bots", value = len([i for i in ctx.guild.members if i.bot]))
        embed.add_field(name = "Humans", value = len([i for i in ctx.guild.members if not i.bot]))
        await ctx.send(embed = embed)

    @commands.command(aliases = ["latency"])
    async def ping(self, ctx):
        await ctx.send(embed = discord.Embed(title = "Pong!", description = f"`{round(self.client.latency *1000)}` ms", color = ctx.author.color))

    @commands.command(aliases = ["whois", "userinfo", "member", "memberinfo"])
    async def user(self, ctx, user):
        
        user = await await f.is_user(ctx, user)
        
        if not user:
            user = ctx.author
        
        embed = discord.Embed(title = f"{user}", description = f"{user.mention}", colour = user.colour)
        embed.set_author(name = user.name, icon_url = user.avatar_url)
        embed.set_thumbnail(url = user.avatar_url)
        embed.set_footer(text = "User ID: {}".format(user.id))
        pos = sum(m.joined_at < user.joined_at for m in ctx.guild.members if m.joined_at is not None)
        roles = [role.mention for role in user.roles[1:]]
        roles.append('@everyone')
        embed.add_field(name = "Join Date", value = user.joined_at.strftime("%x"))
        embed.add_field(name = "Register Date", value = user.created_at.strftime("%x"))
        
        if user.id == 613402918774636570:
            embed.add_field(name = "Join Position", value = f"1/{len(ctx.guild.members)}")     
        
        if user.id != 613402918774636570:
            embed.add_field(name = "Join Position", value = f"{pos + 2}/{len(ctx.guild.members)}")
        
        embed.add_field(name = "Roles ({})".format(len(roles)), value = " ".join(roles))
        await ctx.send(embed = embed)

    # @commands.command(aliases = ["randomvideo", "randomvid", "vid"])
    # async def video(self, ctx):
    #     vids = ["https://www.youtube.com/watch?v=q1DYYi80xtk",  "https://www.youtube.com/watch?v=qJ7eZKBPv1c", "https://www.youtube.com/watch?v=gWcbF4E0_iU", ]
    #     await ctx.send("Here you go!\n" + random.choice(vids))
    
    @commands.command(aliases = ["yt"])
    async def youtube(self, ctx, *, query):
        
        msg = await ctx.send("Searching...")
        search_keyword = query.replace(" ", "+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        
        url1 = "https://www.youtube.com/watch?v=" + video_ids[0]
        url2 = "https://www.youtube.com/watch?v=" + video_ids[1]
        url3 = "https://www.youtube.com/watch?v=" + video_ids[2]
        url4 = "https://www.youtube.com/watch?v=" + video_ids[3]
        url5 = "https://www.youtube.com/watch?v=" + video_ids[4]

        reqs1 = requests.get(url1)
        soup1 = BeautifulSoup(reqs1.text, 'html.parser')

        for title in soup1.find_all('title'):
            title1 = title.get_text()

        reqs2 = requests.get(url2)
        soup2 = BeautifulSoup(reqs2.text, 'html.parser')

        for title in soup2.find_all('title'):
            title2 = title.get_text()

        reqs3 = requests.get(url3)
        soup3 = BeautifulSoup(reqs3.text, 'html.parser')

        for title in soup3.find_all('title'):
            title3 = title.get_text()

        reqs4 = requests.get(url4)
        soup4 = BeautifulSoup(reqs4.text, 'html.parser')

        for title in soup4.find_all('title'):
            title4 = title.get_text()
        
        reqs5 = requests.get(url5)
        soup5 = BeautifulSoup(reqs5.text, 'html.parser')

        for title in soup5.find_all('title'):
            title5 = title.get_text()

        embed = discord.Embed(title = f'Search results for "{query}"', colour = ctx.author.color, description = f"""
        **1.)** [{title1}]({url1})
        **2.)** [{title2}]({url2})
        **3.)** [{title3}]({url3})
        **4.)** [{title4}]({url4})
        **5.)** [{title5}]({url5})
        """)
        await msg.edit(embed = embed)
    
    @commands.command()
    async def test1(self, ctx):
        msg = await ctx.channel.fetch_message(865800336764436480)
        print(msg.content)


def setup(client):
    client.add_cog(general(client))
