import discord
from discord.ext import commands
import json
with open('setting.json',mode='r',encoding='utf8') as jFile: #'r' means read
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready(): #bot start
    print('>> Bot is Online <<')

@bot.event
async def on_member_join(member): #someone join the discord server
    #print(F'{member} join!')
    channel = bot.get_channel(int(jdata['ChannelID'])) #bot will get channel's ID
    await channel.send(F'{member} 加入伺服器囉!!!!耶泰尬!!')

@bot.event
async def on_member_remove(member):#someone leave the discord server
    #print(F'{member} leave!')
    channel = bot.get_channel(int(jdata['ChannelID'])) #bot will get channel's ID
    await channel.send(F'{member} 離開伺服器了QQ')

@bot.command()
async def ping(ctx): #bot's delay
    await ctx.send(F'{round(bot.latency*1000)}(ms)')
    



bot.run(jdata['TOKEN'])