##### Imports #####
import discord
from .__init__ import c
from discord.ext import commands

class Help(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')

    ##### commands #####
    #@client.group(invoke_without_command)
    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author
        await author.send('test')
   
##### Finalize and run #####
def setup(client):
    client.add_cog(Help(client))