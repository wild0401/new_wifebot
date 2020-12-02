import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata =json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(F'{member} join!')       #F字串:非特定字串使用

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(F'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):                            #關鍵字觸發
        keyword = jdata['keyword']                   #關鍵字清單
        if msg.content == 'gg' and msg.author != self.bot.user: #完全符合字串完全符合字串
            await msg.channel.send('gg')
        if msg.content.endswith('apple'):                       #條件符合條件符合
            await msg.channel.send('hi')
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('生物')

def setup(bot):
    bot.add_cog(Event(bot))