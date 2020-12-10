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

    # 處理"指令"發生的錯誤 Error Handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx,error):
        #await ctx.send(ctx.command)
        if hasattr(ctx.command, 'on_error'):
            return
        #上文:...指令觸發了___錯誤server channel msg
        #await ctx.send(error)
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("遺失參數")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("沒這個指令啦!")
        else:
            await ctx.send("發生錯誤")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        #新增反應貼圖獲取身分組
        #判斷反應訊息是否為指定的訊息
        if payload.message_id == 786301223627784202:
            #判斷反應貼圖給予相對應身分組
            if str(payload.emoji) == '💯':
                #print("有近來")
                guild = self.bot.get_guild(payload.guild_id)    #取得當前所在伺服器
                role = guild.get_role(786288390827016222)       #取得伺服器內指定的身分組                     
                await payload.member.add_roles(role)            #給予該成員身分組
                await payload.member.send(f"你取得了{role}身分組!")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        #新增反應貼圖獲取身分組
        if payload.message_id == 786301223627784202:
            #判斷反應貼圖給予相對應身分組
            if str(payload.emoji) == '💯':
                #print("有近來")
                guild = self.bot.get_guild(payload.guild_id)    #取得當前所在伺服器
                user = guild.get_member(payload.user_id)
                role = guild.get_role(786288390827016222)        #取得伺服器內指定的身分組                     
                await user.remove_roles(role)                    #移除該成員身分組
                await user.send(f"你移除了{role}身分組!")
    
    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        counter = 1
        async for audilog in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
            if counter == 1:
                await msg.channel.send(audilog.user.name)
                counter += 1
        #await msg.channel.send("刪除訊息內容 : " + str(msg.content))
        #await msg.channel.send("刪除訊息原本的作者 : " + str(msg.author))

def setup(bot):
    bot.add_cog(Event(bot))