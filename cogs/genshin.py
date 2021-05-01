##### Imports #####
import discord
from .__init__ import c
from datetime import datetime
from discord.ext import commands
from bs4 import BeautifulSoup as bs
import requests
from tabulate import tabulate

#scrape promo codes table
page = requests.get('https://www.gensh.in/events/promotion-codes').text
soup = bs(page, 'lxml')
tbody = soup.find('tbody')
#table = [['Date Added', 'Rewards', 'Expired', 'EU', 'NA', 'SEA']]
table = []

#genarate table as list
for item in tbody.find_all('tr'):
    row = []
    for i in item:
        i = str(i).replace('<td> ', '').replace('</td>', '')
        row.append(i)
    table.append(row)

#functions
def makeEu(t):
    ls = []
    for item in t:
        ls.append([str(item[0]), str(item[1]), str(item[2]), str(item[3])])
    return(ls)

def makeNa(t):
    ls = []
    for item in t:
        ls.append([str(item[0]), str(item[1]), str(item[2]), str(item[4])])
    return(ls)

def makeSea(t):
    ls = []
    for item in t:
        ls.append([str(item[0]), str(item[1]), str(item[2]), str(item[5])])
    return(ls)
    
def activeOnly(ls):
    result = []
    for item in ls:
        check = str(item[2]).replace(' ', '')
        if check != 'Yes':
            result.append(item)  
    return(result)

class Genshin(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client

    ##### commands #####
    """
    #@commands.has_any_role(c.memberRole)
    @commands.command()
    async def promo(self, ctx, region):
        if region == 'eu':
            await ctx.send(tabulate(activeOnly(makeEu(table)), headers='firstrow'))
        elif region == 'na':
            await ctx.send(tabulate(activeOnly(makeNa(table)), headers='firstrow'))
        elif region == 'sea':
            await ctx.send(tabulate(activeOnly(makeSea(table)), headers='firstrow'))
        elif region is None:
            await ctx.send('please sepecify a region: You can use eu, na, sea')
    """

    @commands.command()
    async def euPromo(self, ctx):
        date = ''
        rewards = ''
        codes = ''
        e = discord.Embed(title='Genshin Promo Codes', description=f'Region: EU', color=0xa0089b)
        for item in activeOnly(makeEu(table)):
            date = f'{date}\n{item[0]}'
            rewards = f'{rewards}\n{item[1]}'
            codes = f'{codes}\n{item[3]}'
        e.add_field(name="Date Added", value=date, inline=True)
        e.add_field(name="Rewards", value=rewards, inline=True)
        e.add_field(name="Code", value=codes, inline=True)
        await ctx.send(embed=e)

    @commands.command()
    async def naPromo(self, ctx):
        date = ''
        rewards = ''
        codes = ''
        e = discord.Embed(title='Genshin Promo Codes', description=f'Region: NA', color=0xa0089b)
        for item in activeOnly(makeNa(table)):
            date = f'{date}\n{item[0]}'
            rewards = f'{rewards}\n{item[1]}'
            codes = f'{codes}\n{item[4]}'
        e.add_field(name="Date Added", value=date, inline=True)
        e.add_field(name="Rewards", value=rewards, inline=True)
        e.add_field(name="Code", value=codes, inline=True)
        await ctx.send(embed=e)

    @commands.command()
    async def seaPromo(self, ctx):
        date = ''
        rewards = ''
        codes = ''
        e = discord.Embed(title='Genshin Promo Codes', description=f'Region: SEA', color=0xa0089b)
        for item in activeOnly(makeSea(table)):
            date = f'{date}\n{item[0]}'
            rewards = f'{rewards}\n{item[1]}'
            codes = f'{codes}\n{item[5]}'
        e.add_field(name="Date Added", value=date, inline=True)
        e.add_field(name="Rewards", value=rewards, inline=True)
        e.add_field(name="Code", value=codes, inline=True)
        await ctx.send(embed=e)

##### Finalize and run #####
def setup(client):
    client.add_cog(Genshin(client))