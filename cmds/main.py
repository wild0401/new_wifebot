import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata =json.load(jfile)

class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(F'{round(self.bot.latency*1000)}(ms)')

    @commands.command()    
    async def hi(self, ctx):
        await ctx.send('ABCD123456789')

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="title", url="https://www.twitch.com", description="description", color=0xd4ff00,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="author name", url="https://www.twitch.com", icon_url="https://www.twitch.com/1.gif")
        embed.add_field(name="1", value="11", inline=False)
        embed.add_field(name="2", value="22", inline=False)
        embed.add_field(name="3", value="33", inline=True)
        embed.add_field(name="4", value="44", inline=True)
        embed.set_footer(text="測試二二二")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

    #@commands.command()
    #async def rand_squad(self, ctx):
    #    online = []
    #    for member in ctx.guild.members:
    #        if member.raw_status == 'online' and member.bot == False:
    #            online.append(member.name)
    #    random_online = random.sample(online,k=2)

    #    for cho1 in range(4)
    #        team = random.sample(random_online,k=1)
    #        await ctx.send(f"{cho1+1}小隊:" + str(team))
    #        for name in team:
    #        random_online.remove(name)
    #    for i in random_offline:
    #        print(i)

    @commands.group()
    async def codetest(self, ctx):
        #await ctx.send("Group")
        pass

    @codetest.command()
    async def python(self, ctx):
        await ctx.send("Python")

    @codetest.command()
    async def javascript(self, ctx):
        await ctx.send("Javascript")

    @codetest.command()
    async def cpp(self, ctx):
        await ctx.send("C++")

    @commands.command()
    async def cmdA(self, ctx,num:float):
        await ctx.send(num)
    
    @commands.command()
    async def cmdB(self, ctx,num):
        await ctx.send(num)

    #指令個別專用的錯誤處理
    @cmdB.error
    async def cmdB_error(self, ctx,error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("請輸入參數")

    @commands.command()
    async def cmdC(self, ctx,num:str):
        try:
            await ctx.sens(int(num))
        except Exception as e:
            await ctx.send(e)


def setup(bot):
    bot.add_cog(Main(bot))