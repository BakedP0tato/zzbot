from discord.ext import commands
from random import randint

def check(context):
    def inner_check(message):
        return context.author == message.author and context.channel == message.channel
    return inner_check

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def highlow(self, ctx, highest=100, lowest=1):
        ran = randint(1,highest)
        await ctx.send(f'A random number has been chosen from {lowest} to {highest}')
        game = True
        guesscount = 0
        while game:
            await ctx.send(f'Try to guess the number :{lowest} to {highest} (Any non-integer to quit)')
            msg = await self.bot.wait_for(event='message', check=check(ctx), timeout=60)
            try:
                guess = int(msg.content)
            except ValueError:
                await ctx.send('Game quitted')
                break
            if lowest <= guess <= highest:
                guesscount += 1
                if guess == ran:
                    await ctx.send('Bravo, you got it')
                    break
                elif guess > ran:
                    await ctx.send('Too high')
                    highest = guess - 1
                elif guess < ran:
                    await ctx.send('Too low')
                    lowest = guess + 1
            else:
                await ctx.send('Bro')
        await ctx.send(f'Took you {guesscount} guess(es).')
        
def setup(bot): # a extension must have a setup function
	bot.add_cog(Fun(bot))