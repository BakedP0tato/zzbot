from discord.ext import commands
from discord.errors import NotFound
import discord
import asyncio

from discord.ext.commands.bot import Bot

def check(context):
    def inner_check(message):
        return context.author == message.author and context.channel == message.channel
    return inner_check

class Tools(commands.Cog):

    @commands.command(help='Capitalize every letter of the sentence')
    async def upper(self, ctx, *, sentence):
        await ctx.send(sentence.upper())

    @commands.command(help='Uncapitalize every letter of the sentence')
    async def lower(self, ctx, *, sentence):
        await ctx.send(sentence.lower())

    @commands.command(help='boom')
    async def bomb(self, ctx):
        await ctx.send('Set timer: hours? (0 to 23)')
        msg = await commands.Bot.wait_for('message', check=check(ctx), timeout=30)
        hours = int(msg.content)
        if 0 > hours > 23:
            await ctx.send('No')
        else:
            await ctx.send('Set timer: minutes? (0 to 59)')
            msg = await commands.Bot.wait_for('message', check=check(ctx), timeout=30)
            minutes = int(msg.content)
            if 0 > minutes > 59:
                await ctx.send('No')
            else:
                await ctx.send('Set timer: seconds? (0 to 59)')
                msg = await commands.Bot.wait_for('message', check=check(ctx), timeout=30)
                seconds = int(msg.content)
                if 0 > seconds > 59:
                    await ctx.send('No')
                else:
                    message = await ctx.send(f"Timer: {hours}:{minutes}:{seconds}")
                    while True:
                        seconds -= 1
                        if seconds <= 0 and minutes > 0:
                            minutes -= 1
                            seconds = 59
                        elif seconds <= 0 and minutes <= 0 and hours > 0:
                            hours -= 1
                            minutes = 59
                            seconds = 59
                        elif seconds <= 0 and minutes <= 0 and hours <= 0:
                            try:
                                await message.edit(content="Ended!")
                            except NotFound:
                                pass
                            break
                        try:
                            await message.edit(content=f"Timer: {hours}:{minutes}:{seconds}")
                        except NotFound:
                            await ctx.send('Timer not found, do you want it to continue? y/n')
                            msg = await commands.wait_for('message', check=check(ctx), timeout=30)
                            if (msg.content).lower() == 'y':
                                message = await ctx.send(f"Timer: {hours}:{minutes}:{seconds}")
                            else:
                                break
                        await asyncio.sleep(1)
                    await ctx.send('{} was exploded'.format(ctx.author.mention))
    
def setup(bot: commands.Bot): 
    bot.add_cog(Tools())