##### Imports #####
import discord
from .__init__ import c
from discord.ext import commands

class Misc(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client

    ##### commands #####
    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test')
    @commands.command(aliases=['clear'])
    async def purge(self, ctx, amount = 100):
        log = self.client.get_channel(c.logChannel)
        await ctx.channel.purge(limit = amount)
        await log.send(f':arrow_forward: succsessfully purged {amount} messages in #{ctx.channel.name}')

    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test', 'Café Antik')
    @commands.command()
    async def ping(self, ctx):
        ping = ctx.message
        log = self.client.get_channel(c.logChannel)
        pong = await ctx.send('**:ping_pong:** Pong!')
        latency = pong.created_at - ping.created_at
        latency = int(latency.total_seconds() * 1000)
        await pong.edit(content=f':ping_pong: Pong! ({latency} ms)')
        await log.send(f':arrow_forward: succsessfully executed ping command in #{ctx.channel.name}')
        #print(f'Pong! ({latency} ms)')

    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test')
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

    ##### commands #####
    @commands.command(aliases=['quit', 'kill'], hidden=True)
    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test')
    async def logout(self, ctx):
        await ctx.channel.purge(limit = 1)
        await ctx.send(f':arrow_right: Bot successfully killed by {ctx.author}')
        await self.client.logout()
        sys.exit(0)

##### Finalize and run #####
def setup(client):
    client.add_cog(Misc(client))