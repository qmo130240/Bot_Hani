import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready(): #bot start
    print('>> Bot is Online <<')

@bot.event
async def on_member_join(member): #someone join the discord server
    #print(F'{member} join!')
    channel = bot.get_channel(714691114313056256) #bot will get channel's ID
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):#someone leave the discord server
    #print(F'{member} leave!')
    channel = bot.get_channel(714691155333349387) #bot will get channel's ID
    await channel.send(F'{member} leave QQ')

bot.run('NzE0NDI3ODU0ODIxMTMwMjYw.XsupjA.nPvK0q7yN5d0FeEhf2uH6pwZDs8')

