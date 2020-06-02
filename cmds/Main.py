import discord
from discord.ext import commands
from core.classes import CogExtension

class Main(CogExtension):

    @commands.command()
    async def ping(self,ctx): #show bot's delay
        await ctx.send(F'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def say(self,ctx,*,msg): #repeat the message user saied
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def purge(self,ctx,num:int): #purge the message, num is the number of message that u wanna purge
        await ctx.channel.purge(limit=num+1)

    
    
def setup(bot):
    bot.add_cog(Main(bot))