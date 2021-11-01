from discord.ext import commands
import discord

class Server(commands.Cog):
    @commands.command(name='server', help='Some info on the server')
    async def fetchServerInfo(self, ctx):
        num_members = sum(not member.bot for member in ctx.guild.members)
        #num_bots = sum(member.bot for member in ctx.guild.members)
        num_bots = ctx.guild.member_count - num_members
        await ctx.send(f'Server Name: {ctx.guild.name}')
        await ctx.send(f'Members: {num_members}')
        await ctx.send(f'Bots: {num_bots}')

    @commands.command(help='See some info on a member in the server')
    async def joined(self, ctx, *, member: discord.Member):
        fmt='{0} joined on {0.joined_at} and has {1} roles.'
        await ctx.send(fmt.format(member, len(member.roles)))
    
def setup(bot: commands.Bot): 
    bot.add_cog(Server())