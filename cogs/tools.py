from discord.ext import commands

class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(help='Capitalize every letter of the sentence')
    async def upper(ctx, *, sentence):
        await ctx.send(sentence.upper())

    @commands.command(help='Uncapitalize every letter of the sentence')
    async def lower(ctx, *, sentence):
        await ctx.send(sentence.lower())
    
def setup(bot): 
    bot.add_cog(Tools(bot))