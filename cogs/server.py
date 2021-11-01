from discord.ext import commands
import discord

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='server', help='Some info on the server')
    async def fetchServerInfo(ctx):
        num_members = sum(not member.bot for member in ctx.guild.members)
        #num_bots = sum(member.bot for member in ctx.guild.members)
        num_bots = ctx.guild.member_count - num_members
        await ctx.send(f'Server Name: {ctx.guild.name}')
        await ctx.send(f'Members: {num_members}')
        await ctx.send(f'Bots: {num_bots}')

    @commands.command(help='See some info on a member in the server')
    async def joined(ctx, *, member: discord.Member):
        fmt='{0} joined on {0.joined_at} and has {1} roles.'
        await ctx.send(fmt.format(member, len(member.roles)))
    
def setup(bot): 
    bot.add_cog(Server(bot))