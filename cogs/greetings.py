from discord.ext import commands
import discord
import random

class Greetings(commands.Cog):
    def __init__(self):
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command(help='A simple greeting')
    async def hi(self, ctx):
        greetings = [
            'Hello',
            'Greetings',
            'Hi',
        ]
        response = random.choice(greetings)
        await ctx.send(response)

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}!'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member
    
def setup(bot: commands.Bot): 
    bot.add_cog(Greetings())