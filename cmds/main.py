import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime

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

def setup(bot):
    bot.add_cog(Main(bot))