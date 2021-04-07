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