import discord
from discord.ext import commands
from core.classes import CogExt
import json 

with open('setting.json', 'r', encoding='utf8') as file:
    data = json.load(file)

class Event(CogExt):

    ''' 成員加入 '''
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(data['channel_lab'])
        await channel.send(f'{member} is join!')

    ''' 成員離開 '''
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(data['channel_lab'])
        await channel.send(f'{member} leave!')

    ''' 關鍵字 '''
    @commands.Cog.listener()
    async def on_message(self, msg):
        word = ['hi', 'hello']
        if msg.content in word and msg.author != self.bot.user:
            await msg.channel.send('hello')

def setup(bot):
    bot.add_cog(Event(bot))