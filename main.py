##### Imports #####
import configs.loadconfig as c
import discord
import yaml
import sys
import os
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = c.prefix, intents=intents)
#client.remove_command('help')

##### load extensions #####
@commands.has_any_role('Jonnys Bot test')
@client.command()
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'loaded {extension} successfull')
    except Exception as error:
        await ctx.send(error)

##### unload extensions #####
@commands.has_any_role('Jonnys Bot test')
@client.command()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'unloaded {extension} successfull')
    except Exception as error:
        await ctx.send(error)
        
##### reload extensions #####
@commands.has_any_role('Jonnys Bot test')
@client.command()
async def reload(ctx, extension):
    try:
        client.reload_extension(f'cogs.{extension}')
        await ctx.send(f'reloaded {extension} successfull')
    except Exception as error:
        await ctx.send(error)

##### read extensions in #####
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and '__init__' not in filename:
        client.load_extension(f'cogs.{filename[:-3]}')

##### backup shutdown #####
@client.command(hidden=True, aliases=['quit_backup'])
@commands.has_any_role('Jonnys Bot test')
async def shutdown(ctx):
    await client.logout()
    sys.exit(0)
        
##### Finalize and run #####
client.run(c.token)