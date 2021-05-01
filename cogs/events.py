##### Imports #####
import discord
from .__init__ import c
from discord.ext import commands

class Event(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client

    ##### events #####
    @commands.Cog.listener()
    async def on_ready(self):
        #set log channel
        log = self.client.get_channel(c.logChannel)
        finalChannel = self.client.get_channel(c.finalChannel)
        #print online messages
        print('Bot is now online.')
        await log.send(':white_check_mark: Bot is now online.')
        #set Status
        await self.client.change_presence(status=discord.Status.dnd)
        #define vars for tracked channels
        g = self.client.get_guild(c.serverId)
        #print tracked channels for auto move
        for channel in g.channels:
            if str(c.channelPart) in str(channel.name) and str(channel.name) not in c.ignoredChannels:
                await log.send(f':arrow_right:  tracked channel found: {channel}')
        #reminder to check full channel informations if needed
        await log.send(f':arrow_right: final channel found: {finalChannel}')
        await log.send(f':passport_control: if you need more detailed information please use the <cTRackedInfo> command')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            print(ctx.command.name + ' was used incorrectly!')
            print(error)
            await ctx.send(error)
        except (AttributeError):
            pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        g = self.client.get_guild(c.serverId)
        log = self.client.get_channel(c.logChannel)
        joinRole = discord.utils.get(g.roles, id=c.joinRole)
        await member.add_roles(joinRole)
        await log.send(f':arrow_forward: gave {member}: {joinRole}')

#tmp hardcoded, will be removed later
    @commands.Cog.listener()
    async def on_message(self, message):
        #print(message.channel.id, message.author.id)
        trusted = [206512931590897664, 206459837188407296, 285140174432763904, 769074797123469343]
        if message.channel.id == 823913121663549440 and message.author.id not in trusted:
            print(f'Message in rollen: {message}, \nSend by: {message.author.name}')
            await message.delete()

##### Finalize and run #####    
def setup(client):
    client.add_cog(Event(client))