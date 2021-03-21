##### Imports #####
import discord
import asyncio
from .__init__ import c
from discord.ext import commands

class Move(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client

    ##### events #####
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        #vars
        channel_lst = []
        g = self.client.get_guild(c.serverId)
        log = self.client.get_channel(c.logChannel)
        #channel stuff
        for channel in g.channels:
            if str(c.channelPart) in str(channel.name) or str(c.finalChannel) == str(channel.id):
                channel_lst.append(channel)
        #main task
        if after.channel != None:
            member_lst = []
            for user in after.channel.members:
                member_lst.append(user)
            if len(after.channel.members) > after.channel.user_limit and int(after.channel.user_limit) != 0:
                await log.send(f':arrow_right: too many people: ')
                for m in after.channel.members:
                    await log.send(f':warning: {m}')
                await log.send(f':arrow_forward: waiting {c.sleepTime} seconds until move...')
                await asyncio.sleep(c.sleepTime)
            if len(after.channel.members) > after.channel.user_limit and int(after.channel.user_limit) != 0:
                #reload member list
                member_lst = []
                for user in after.channel.members:
                    member_lst.append(user)
                #next channel select
                for ch in channel_lst:
                    #print(ch.user_limit)
                    if ch.user_limit == len(member_lst) and int(ch.user_limit) != 0: #changed after.channel.members into member_lst
                        if ch.name not in c.ignoredChannels:
                            #log
                            await log.send(f':arrow_right: too many people in {after.channel.name}')
                            await log.send(f':arrow_forward: problem solved, channel members moved: {after.channel.name} -> {ch.name}')
                            #move
                            for member in member_lst:
                                await member.edit(voice_channel=ch) 
                    elif int(ch.user_limit) == 0 and len(member_lst) > 5: #changed after.channel.members into member_lst
                        if ch.name not in c.ignoredChannels:
                            #log
                                                                                                                            #await log.send(f':arrow_forward: too many people in {after.channel.name}: problem solved')
                            await log.send(f':arrow_right: too many people in {after.channel.name}')
                            await log.send(f':arrow_forward: problem solved, channel members moved: {after.channel.name} -> {ch.name}')
                            #move
                            for member in member_lst:
                                await member.edit(voice_channel=ch)       

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['voiceinfo', 'voiceInfo'])
    async def vInfo(self, ctx):
        #g = self.client.get_guild(c.serverId)
        channel = self.client.get_channel(812057228739084288)
        await ctx.send('----------\nvMember:\n----------')
        for m in channel.members:
            await ctx.send(m)

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['channeltrackedinfo', 'channelTrackedInfo', 'cTrackedinfo'])
    async def cTrackedInfo(self, ctx):
        g = self.client.get_guild(c.serverId)
        log = self.client.get_channel(c.logChannel)
        channel_lst = []
        await ctx.send('----------\nTracked Channels:\n----------')
        for channel in g.channels:
            if str(c.channelPart) in str(channel.name) or str(c.finalChannel) == str(channel.id):
                if str(channel.name) not in c.ignoredChannels:
                    channel_lst.append(channel)
        channel_lst = '[\n' + str(channel_lst).replace('>, <', '>, \n<').strip('[').strip(']') + '\n]'
        await log.send(channel_lst)

    @commands.has_any_role(c.adminRole, c.managmentRole)
    @commands.command(aliases=['ignoredinfo', 'ignoredInfo'])
    async def iInfo(self, ctx):
        for channel in c.ignoredChannels:
            await ctx.send(f':arrow_forward: {channel}')

##### Finalize and run #####    
def setup(client):
    client.add_cog(Move(client))