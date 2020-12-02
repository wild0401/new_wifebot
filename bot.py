#導入模組
import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata =json.load(jfile)

#建置實體(特殊命令字首)
bot = commands.Bot(command_prefix='[')

#裝飾器(@bot:bot底下的.定義)
@bot.event
async def on_ready():       #重新定義on_ready函式
    print(">>Bot is online<<")

@bot.command()
async def 圖片(ctx):
    random_pic=random.choice(jdata['pic'])
    pic=discord.File(random_pic)
    await ctx.send(file=pic)

@bot.command()
async def web(ctx):
    random_pic=random.choice(jdata['url_pic'])
    await ctx.send(random_pic)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(F'{member} join!')   #F字串:非特定字串使用

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(F'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}(ms)')
    
bot.run(jdata['TOKEN'])