import discord
from discord.ext import commands
from core.classes import CogExt

class Main(CogExt):
    
    ''' 延遲時間 '''
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms')

def setup(bot):
    bot.add_cog(Main(bot))