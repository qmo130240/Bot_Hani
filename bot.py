import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready(): #bot start
    print('>> Bot is Online <<')

@bot.event
async def on_member_join(member): #someone join the discord server
    #print(F'{member} join!')
    channel = bot.get_channel(528522034788171778) #bot will get channel's ID
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):#someone leave the discord server
    #print(F'{member} leave!')
    channel = bot.get_channel(528522034788171778) #bot will get channel's ID
    await channel.send(F'{member} leave QQ')

@bot.command()
async def ping(ctx): #bot's delay
    await ctx.send(F'{round(bot.latency*1000)}(ms)')
    



bot.run('NzE0NDI3ODU0ODIxMTMwMjYw.XsybtQ.r89mYE05qUfIEs3LkGvi8_WmBHY')