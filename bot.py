import discord
from discord.ext import commands
import json 
import random

with open('setting.json', 'r', encoding='utf8') as file:
    data = json.load(file)

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print("Bot is online!")

''' 成員加入 '''
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(data['channel_lab'])
    await channel.send(f'{member} is join!')

''' 成員離開 '''
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(data['channel_lab'])
    await channel.send(f'{member} leave!')

''' 延遲時間 '''
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')

''' 顯示圖片(隨機) '''
@bot.command()
async def show_pic(ctx):
    pic = discord.File(random.choice(data['picture']))
    await ctx.send(file=pic)

bot.run(data['token'])