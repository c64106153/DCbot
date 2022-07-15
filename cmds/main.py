import discord
from discord.ext import commands
from core.classes import Cog_Extension

intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')


    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(ctx,num:int):
        await ctx.channel.purge(limit=num+1)
    


def setup(bot):
    bot.add_cog(Main(bot))