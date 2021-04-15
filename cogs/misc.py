##### Imports #####
import discord
from .__init__ import c
from datetime import datetime
from discord.ext import commands

class Misc(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client

    ##### commands #####
    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['clear'])
    async def purge(self, ctx, amount = 100):
        log = self.client.get_channel(c.logChannel)
        await ctx.channel.purge(limit = amount)
        await log.send(f':arrow_forward: succsessfully purged {amount} messages in #{ctx.channel.name}')

    @commands.has_any_role(c.adminRole, c.managmentRole, c.memberRole)
    @commands.command()
    async def ping(self, ctx):
        ping = ctx.message
        log = self.client.get_channel(c.logChannel)
        pong = await ctx.send('**:ping_pong:** Pong!')
        latency = pong.created_at - ping.created_at
        latency = int(latency.total_seconds() * 1000)
        await pong.edit(content=f':ping_pong: Pong! ({latency} ms)')
        await log.send(f':arrow_forward: succsessfully executed ping command in #{ctx.channel.name}')

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command()
    async def dcInfo(self, ctx):
        g = self.client.get_guild(c.serverId)
        await ctx.send(':bangbang: **Member: **')
        for member in g.members:
            await ctx.send(f':arrow_right: {member}')
        await ctx.send(f':white_check_mark: {len(g.members)}')
        await ctx.send(':bangbang: **Roles: **')
        for r in g.roles:
            if str(r) != '@everyone':
                await ctx.send(f':arrow_right: {r}')
        await ctx.send(f':white_check_mark: {len(g.roles)}')

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['quit', 'kill'], hidden=True)
    async def logout(self, ctx):
        await ctx.channel.purge(limit = 1)
        await ctx.send(f':arrow_right: Bot successfully killed by {ctx.author}')
        await self.client.logout()
        sys.exit(0)

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['j'], hidden=True)
    async def join(self, ctx):
        v = ctx.author.voice
        if not v:
            await ctx.send("You need to be connected in a voice channel to use this command!")
        else:
            channel = ctx.author.voice.channel
            await ctx.send(channel)
            await channel.connect()

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['jU'], hidden=True)
    async def joinUser(self, ctx, usr):
        v = await self.client.fetch_user(usr)
        g = self.client.get_guild(c.serverId)
        if not v:
            await ctx.send("You need to specify a userID to use this command!")
        else:
            channel = g.get_member(v.id).voice.channel
            await ctx.send(channel)
            await channel.connect()

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['l'], hidden=True)
    async def leave(self, ctx):
        await ctx.guild.voice_client.disconnect()

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['tm'], hidden=True)
    async def testmove(self, ctx, new):
        g = self.client.get_guild(c.serverId)
        new = self.client.get_channel(int(new))
        v = ctx.author.voice
        if not v:
            await ctx.send("You need to be connected in a voice channel to use this command!")
        else:
            channel = v.channel
            for m in channel.members:
                await m.edit(voice_channel=new)
        
        
        #await ctx.send(channel)
        #await ctx.send(role)

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['uInfo'], hidden=True)
    async def usrInfo(self, ctx, usr):
        g = self.client.get_guild(c.serverId)
        member = await self.client.fetch_user(usr)
        member = g.get_member(member.id)
        if member != None:
            await ctx.send(f'Member: ```{member}```')
            await ctx.send(f'Activity: ```{member.activities}```')
            if len(member.activities) != 0:
                await ctx.send(f'Base: ```{member.activities[2]}```')
            if len(member.activities) > 1:
                await ctx.send(f'Spotify: ```{member.activities[1]}```')
            await ctx.send(f'voiceState: ```{member.voice}```')
            if member.voice != None:
                await ctx.send(f'stream?: ```{member.voice.self_stream}```')
            else:
                await ctx.send(f'stream?: ```False```')

    @commands.has_any_role(c.memberRole)
    @commands.command()
    async def botInfo(self, ctx):
        await ctx.channel.purge(limit = 1)
        embed = discord.Embed(title='CA-Discord-Bot', url='https://github.com/D3monEmper0r/CA-Discord-Bot/tree/main', description='Source Code here.', color=0xa0089b)
        embed.set_author(name='GitHub', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Github-desktop-logo-symbol.svg/1024px-Github-desktop-logo-symbol.svg.png')
        await ctx.send(embed=embed)

##### Finalize and run #####
def setup(client):
    client.add_cog(Misc(client))