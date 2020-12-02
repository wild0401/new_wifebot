#導入模組
import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json','r',encoding='utf8') as jfile:
    jdata =json.load(jfile)

#建置實體(特殊命令字首)
bot = commands.Bot(command_prefix='[')

#裝飾器(@bot:bot底下的.定義)
@bot.event
async def on_ready():       #重新定義on_ready函式
    print(">>Bot is online<<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'Un - Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'Re - Loaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])