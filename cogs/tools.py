from discord.ext import commands

class Tools(commands.Cog):

    @commands.command(help='Capitalize every letter of the sentence')
    async def upper(self, ctx, *, sentence):
        await ctx.send(sentence.upper())

    @commands.command(help='Uncapitalize every letter of the sentence')
    async def lower(self, ctx, *, sentence):
        await ctx.send(sentence.lower())
    
def setup(bot: commands.Bot): 
    bot.add_cog(Tools())