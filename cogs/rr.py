##### Imports #####
import discord
import sqlite3
from .__init__ import c
from discord.ext import commands

def create(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    newDbTable = """CREATE TABLE IF NOT EXISTS
    reactionRole(role TEXT PRIMARY KEY, emote TEXT UNIQUE)"""
    c.execute(newDbTable)

    conn.commit()
    conn.close()

def fill(db, role, emote):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    
    c.execute(f'INSERT INTO reactionRole VALUES ("{role}", "{emote}")')

    conn.commit()
    conn.close()

def delete(db, role):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    
    c.execute(f'DELETE FROM reactionRole WHERE role = "{role}"')

    conn.commit()
    conn.close()

def data(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(f'SELECT * FROM reactionRole')
    result = c.fetchall()

    conn.close()
    return(result)

def search(db, emote):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(f'SELECT * FROM reactionRole WHERE emote = "{emote}"')
    result = c.fetchall()

    conn.close()
    return(result)

class ReactRole(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client

    ##### events #####
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        reactUser = payload.member
        g = self.client.get_guild(c.serverId)
        emoji = payload.emoji
        tmp = search(c.DB, emoji)[0][0]
        for role in await g.fetch_roles():
            if role.mention == tmp:
                r = role

        if r != None and payload.channel_id == c.reactRoleId:
            if reactUser != self.client.user:
                await reactUser.add_roles(r)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        reactUser = discord.utils.get(self.client.get_all_members(), id=payload.user_id)
        g = self.client.get_guild(c.serverId)
        emoji = payload.emoji
        tmp = search(c.DB, emoji)[0][0]
        for role in await g.fetch_roles():
            if role.mention == tmp:
                r = role

        if r != None and payload.channel_id == c.reactRoleId:
            if reactUser != self.client.user:
                await reactUser.remove_roles(r)

    ##### commands #####
    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test')
    @commands.command()
    async def rrCreate(self, ctx):
        create(c.DB)
        await ctx.channel.purge(limit = 1)
        embed = discord.Embed(title='React to give yourself a role.', description='', color=0xa0089b)
        await ctx.send(embed=embed)


    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test')
    @commands.command()
    async def rrAdd(self, ctx, *, reactRole):
        await ctx.channel.purge(limit = 1)
        g = self.client.get_guild(c.serverId)
        role = reactRole.split(' ')[0]
        emoji = reactRole.split(' ')[1]
        fill(c.DB, role, emoji)

    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test')
    @commands.command()
    async def rrUpdate(self, ctx):
        await ctx.channel.purge(limit = 1)
        channel = await self.client.fetch_channel(c.reactRoleId)
        message = await channel.fetch_message(c.reactMsgId)
        desc = ''
        for item in data(c.DB):
            desc += item[0] + ': ' + item[1] + '\n'
        embed = discord.Embed(title='React to give yourself a role.', description=desc, color=0xa0089b)
        await message.edit(embed=embed)
        await message.clear_reactions()
        for item in data(c.DB):
            await message.add_reaction(item[1])

    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test')
    @commands.command()
    async def rrRemove(self, ctx, role):
        await ctx.channel.purge(limit = 1)
        g = self.client.get_guild(c.serverId)
        delete(c.DB, role)
    
    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test')
    @commands.command(aliases=['e'])
    async def get_e(self, ctx):
        g = self.client.get_guild(c.serverId)
        for e in await g.fetch_emojis():
            await ctx.send(e)

    @commands.has_any_role('Café Antik Geschäftsführung', 'Jonnys Bot test')
    @commands.command(aliases=['r'])
    async def get_r(self, ctx, role):
        g = self.client.get_guild(c.serverId)
        print(role)
        for r in await g.fetch_roles():
            print('CA role: ', r.mention)
            if r.mention == role:
                await ctx.send(r.id)

##### Finalize and run #####    
def setup(client):
    client.add_cog(ReactRole(client))