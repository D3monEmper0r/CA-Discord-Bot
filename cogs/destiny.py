##### Imports #####
from discord.ext import commands
from .__init__ import c
import requests
import discord
import json

#apiKey = c.apiKey
apiKey = {"X-API-Key":'2a4e11c2d7b54394bbedcc1c42cfae34'}
base = 'https://www.bungie.net/Platform/Destiny2'

##### Functions #####
def getXur():
    xur = requests.get(base + '/Vendors/?components=402', headers=apiKey)
    if xur.status_code == 200:
        return(xur.json())
    else:
        return(xur.status_code, xur.status)

def getXurInventory(xur):
    sales = xur['Response']['sales']['data']['2190858386']['saleItems']
    items = []
    for item in sales:
        items.append(sales[item]['itemHash'])
    return(items)

def getItems(xurInventory):
    url = '/Manifest/DestinyInventoryItemDefinition/'
    items = []
    for item in xurInventory:
        r = requests.get(f'{base}{url}{item}', headers=apiKey).json()
        name = r['Response']['displayProperties']['name']
        image = f'https://www.bungie.net{r["Response"]["displayProperties"]["icon"]}'
        temp = {name: image}
        items.append(temp)
    return(items)

def getItemName(items):
    ls = []
    for item in items:
        ls.append(item[0])
    return(ls)

class Destiny(commands.Cog):
    ##### Initalization #####
    def __init__(self, client):
        self.client = client

    ##### commands #####
    @commands.command()
    async def xur(self, ctx):
        author = ctx.message.author
        items = []
        e = discord.Embed(title='Xur Inventory', color=0xa0089b)
        for item in getItemName(getItems(getXurInventory(getXur()))):
            items.append(f'{item}\n')
        e.add_field(name="Xur Sales", value=items, inline=True)
        #await author.send(embed=e)
        await ctx.send(embed=e)

##### Finalize and run #####
def setup(client):
    client.add_cog(Destiny(client))