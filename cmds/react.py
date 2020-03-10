import discord
from discord.ext import commands
from core.classes import CogExt
import json 
import random

with open('setting.json', 'r', encoding='utf8') as file:
    data = json.load(file)

class React(CogExt):

    ''' 顯示圖片(隨機) '''
    @commands.command()
    async def show_pic(self, ctx):
        pic = discord.File(random.choice(data['picture']))
        await ctx.send(file=pic)

def setup(bot):
    bot.add_cog(React(bot))