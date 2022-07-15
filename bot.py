import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import json
import os

intent = discord.Intents.default()
intent.members = True
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='[', intents=intent)

@bot.event
async def on_ready():
    print(" >> Bot is Online now << ")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"查無指令 ")



@bot.event
async def in_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("查無指令")


@bot.event
async def CheckAnyFailure(checks, errors):
    raise checks


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

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(F'cmds.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
