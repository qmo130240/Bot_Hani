import discord
from discord.ext import commands
import json
from core.classes import CogExtension

with open('setting.json',mode='r',encoding='utf8') as jFile: #'r' means read
    jdata = json.load(jFile)

class Event(CogExtension):
    
    @commands.Cog.listener()
    async def on_member_join(self,member): #someone join the discord server
        channel = self.bot.get_channel(int(jdata['ChannelID'])) #bot will get channel's ID
        await channel.send(F"{member} 加入伺服器囉！！！")

    @commands.Cog.listener()
    async def on_member_remove(self,member):#someone leave the discord server
        channel = self.bot.get_channel(int(jdata['ChannelID'])) #bot will get channel's ID
        await channel.send(F"{member} 離開伺服器了～QQ")
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.lower() == 'hey hani' and msg.author != self.bot.user :
            await msg.channel.send(F"{msg.author.name}幹嘛")

    @commands.Cog.listener() #if someone turn on/off his Mic, bot will send message
    async def on_voice_state_update(self,member,before,after):
        channel = self.bot.get_channel(int(jdata['ChannelID']))
        if before.self_mute == False and after.self_mute == True:
            await channel.send(F"{member.name}剛剛關了Mic")
        elif before.self_mute == True and after.self_mute == False:
            await channel.send(F"{member.name}開Mic了")
    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self,channel):
        chl = self.bot.get_channel(int(jdata['ChannelID']))
        await chl.send(F"{channel.name}被刪掉了")
        
    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel):
        chl = self.bot.get_channel(int(jdata['ChannelID']))
        await chl.send(F"{channel.name}被創建了")
   

def setup(bot):
    bot.add_cog(Event(bot))