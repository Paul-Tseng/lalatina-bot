import discord
from discord.ext import commands
import json 
import random
import os

if __name__ == "__main__":
    with open('setting.json', 'r', encoding='utf8') as file:
        data = json.load(file)

    bot = commands.Bot(command_prefix='%')

    @bot.event
    async def on_ready():
        print("Bot is online!")

    path = "cmds"

    ''' 載入模組 '''
    @bot.command()
    async def load(ctx, ext):
        bot.load_extension(f'{path}.{ext}') 
        await ctx.send(f'loaded {ext}')
        
    ''' 卸載模組 '''
    @bot.command()
    async def unload(ctx, ext):
        bot.unload_extension(f'{path}.{ext}') 
        await ctx.send(f'unloaded {ext}')

    ''' 重載模組 '''
    @bot.command()
    async def reload(ctx, ext):
        bot.reload_extension(f'{path}.{ext}') 
        await ctx.send(f'reloaded {ext}')

    for filename in os.listdir(path):
        if filename.endswith('.py'):
            name = filename[:-3]
            bot.load_extension(f'{path}.{name}')

    bot.run(data['token'])