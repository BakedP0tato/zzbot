import os
import random
import discord
from discord.ext import commands

TOKEN=os.environ["DC_TOKEN"]
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the world burning"))

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
    
  else:
    print(f'Unable to load {filename[:-3]}')

@bot.command(help='Checks the bot information')
async def zzbot(ctx):
    await ctx.send('Bot name: Zzbot')
    await ctx.send('Bot programmer: Charcoal#3698')
    await ctx.send('Bot version: v2.1')
    await ctx.send('Date created: 2020-11-23 13:08:08.474000')
    await ctx.send('Primary function: currently undetermined')
    
def check(context):
    def inner_check(message):
        return context.author == message.author and context.channel == message.channel
    return inner_check
    
@bot.command(help='Speaks stuff', pass_context=True)
async def say(ctx, *, sentence):
    if 'zzbot gei' in sentence:
        await ctx.send('NO HAHA')
    else:
        await ctx.message.delete()
        await ctx.send(sentence)

@bot.command(help='Fights someone')
async def fight(ctx, member: discord.Member):
    if member == bot.user:
        await ctx.send('You don\'t get to fight me')
    elif member == ctx.author:
        await ctx.send('You don\'t get to fight yourself.')
    else:
        await ctx.send('in production lol')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try >help ({error})')
    print(error)

bot.run(TOKEN)