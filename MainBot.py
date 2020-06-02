import discord
from discord.ext import commands
import json
import os

with open('setting.json',mode='r',encoding='utf8') as jFile: #'r' means read
    jdata = json.load(jFile)

newBot = commands.Bot(command_prefix='\\')

@newBot.event
async def on_ready(): #bot start
    print('>> Bot is Online <<')

@newBot.command()
async def load(ctx,extension): 
    newBot.load_extension(F'cmds.{extension}')
    await ctx.send(F'Loaded {extension} done.')

@newBot.command()
async def unload(ctx,extension):
    newBot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'Unloaded {extension} done.')

@newBot.command()
async def reload(ctx,extension):
    newBot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'Reloaded {extension} done.')


for filename in os.listdir('./cmds'): #read the file in the cmds
    if filename.endswith('.py'):
        newBot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == "__main__":
    newBot.run(jdata['TOKEN'])

