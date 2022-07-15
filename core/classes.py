import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

class Cog_Extension(commands.Cog):
     def __init__(self,bot):
        self.bot = bot