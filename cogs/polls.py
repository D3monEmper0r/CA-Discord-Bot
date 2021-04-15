##### Imports #####
import discord
from .__init__ import c
from discord.ext import commands
from datetime import datetime, timedelta

numbers = ['<:one:827593616121790534>', '<:two:827593592074797127>', '<:three:827593592935415888>', '<:four:827593593718833172>', '<:five:827593594776322089>', 
            '<:six:827593612854296586>', '<:seven:827593613641908264>', '<:eight:827593614137753681>', '<:nine:827593615307309106>', '<:keycap_ten:827593616121790534>']

class Polls(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client
        self.polls = []

    ##### commands #####
    async def mkPoll(self, ctx, seconds: int, question: str, *options):
        if len(options) > 10:
            print('Max 10 options!')
			#await ctx.send('You can only supply a maximum of 10 options.')
        else:
            embed = Embed(title= "Poll", description= question, color= 0xa0089b, timestamp= datetime.now())


##### Finalize and run #####
def setup(client):
    client.add_cog(Polls(client))