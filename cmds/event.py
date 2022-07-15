import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    @bot.event
    async def on_member_join(self,member):
        channel= bot.get_channel(jdata['Channel'])
        await channel.send(f"{member}join!")
            

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel= bot.get_channel(jdata['Channel'])
        await channel.send(f"{member}leave!")
def setup(bot):
    bot.add_cog(Event(bot))
