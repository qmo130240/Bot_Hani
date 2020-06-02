import discord
from discord.ext import commands
import random
import json
from core.classes import CogExtension

with open('setting.json',mode='r',encoding='utf8') as jFile: #'r' means read
    jdata = json.load(jFile)

class React(CogExtension):

    @commands.command()
    async def nara(self,ctx): #send random local picture
        random_pic = random.choice(jdata['local_pic'])
        pic = discord.File(random_pic)
        await  ctx.send(file=pic)

    @commands.command()
    async def man(self,ctx): #send random online picture
        random_pic = random.choice(jdata['url_pic'])
        await  ctx.send(random_pic)
        

def setup(bot):
    bot.add_cog(React(bot))