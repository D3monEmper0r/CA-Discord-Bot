##### Imports #####
import discord
import asyncio
from .__init__ import c
from discord.ext import commands

##### Functions #####
async def move(member, before, after):
    await member.send(f'{member}, {before}, {after}')
    await member.edit(voice_channel=after)

class _Move(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client

    ##### commands #####
    @commands.command()
    async def m(self, ctx, after):
        author = ctx.message.author
        before = ctx.author.voice.channel
        after = self.client.get_channel(int(after))
        await move(author, before, after)

    @commands.command()
    async def mt(self, ctx):
        author = ctx.message.author

        await author.send(channel_list)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        pass

    """
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
                await log.send(f':arrow_right: too many people in {after.channel.name}')
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
                                #await asyncio.sleep(1)  #added little delay
                                await member.edit(voice_channel=ch)
                                #await log.send(f':broom: moved {member} successfully')

                    elif int(ch.user_limit) == 0 and len(member_lst) > 5: #changed after.channel.members into member_lst
                        if ch.name not in c.ignoredChannels:
                            #log
                            await log.send(f':arrow_right: too many people in {after.channel.name}')
                            await log.send(f':arrow_forward: problem solved, channel members moved: {after.channel.name} -> {ch.name}')
                            #move
                            for member in member_lst:
                                #await asyncio.sleep(1)  #added little delay
                                await member.edit(voice_channel=ch)
                                #await log.send(f':broom: moved {member} successfully')
    """
         
##### Finalize and run #####
def setup(client):
    client.add_cog(_Move(client))