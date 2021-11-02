from discord.ext import commands
import discord
import random
import asyncio

def check(context):
    def inner_check(message):
        return context.author == message.author and context.channel == message.channel
    return inner_check

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dice', help='Simulates rolling dice.')
    async def roll_dice(self, ctx, number_of_dice: int=1, number_of_sides: int=6):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

    @commands.command(help="single player highlow")
    async def highlow(self, ctx, highest=100, lowest=1):
        if lowest >= highest:
            raise Exception("Incorrect")
        ran = random.randint(lowest,highest)
        await ctx.send(f'A random number has been chosen from {lowest} to {highest}')
        game = True
        guesscount = 0
        while game:
            await ctx.send(f'Try to guess the number : {lowest} to {highest} (Any non-integer to quit)')
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
                    await ctx.send(f'Took you {guesscount} guess(es).')
                    break
                elif guess > ran:
                    await ctx.send('Too high')
                    highest = guess - 1
                elif guess < ran:
                    await ctx.send('Too low')
                    lowest = guess + 1
            else:
                await ctx.send('Out of range')

    @commands.command(help='recipes from Goodboirtly')
    async def recipe(self, ctx):
        recipe =[
            (
                'Butter cookies recipe 2'
                '\n200g salted butter (use a good quality one for better result)'
                '\n180g potato starch'
                '\n120g plain flour'
                '\n80g powder sugar (can add another 10g if you want sweeter cookies)'
                '\n1/3 tsp salt'
                '\n'
                '\nBeat butter, salt and sugar till smooth but not too fluffy or your cookies will spread too much.'
                '\n'
                '\nAdd the sifted flours all at once and at low speed, mix until a soft dough is achieved. Place into piping bag with your favourite nozzle and pipe out directly onto baking tray. Try to choose a nozzle that doesn’t have too deep petals so that it won’t fold over and flatten too much while baking. You may chill the piped cookies for 5-10 mins before baking. This will also help retain shape of cookies.'
                '\nBake at 150C for 30-40 mins or until lightly brown.'
            ),
            (
                '150g salted butter (soften)'
                '\n135g potato/ tapioca starch (replace 10g with valrhona cocoa powder if making chocolate version)'
                '\n90g plain flour'
                '\n60g – 70g powder sugar'
                '\n1/3 tsp salt'
                '\n'
                '\nCream butter, salt and sugar till well mixed with hand whisk or stand mixer.'
                '\nAdd in sifted starch and flour (and cocoa powder if using), use hand whisk to mix them gently, followed by spatula to mix into dough.'
                '\n'
                '\nPipe out onto baking tray lined with baking paper. You can use a cookie syringe or piping pag. Before baking, send the tray to the fridge to chill for 10 min will also help retain the shape in the oven'
                '\n'
                '\nBake at 160 deg C for 10 min using conventional mode (top and bottom heat, no fan), then at 160 deg C for another 20 – 25 min at fan forced mode till golden. If bottom has brown but top remains pale, bring tray to upper rack, and bake further'
            ),
            'gei',
        ]
        response = random.choice(recipe)
        await ctx.send(response)
    
    @commands.command(help='Lol')
    async def rickroll(self, ctx, * ,member: discord.Member):
        response = 'Zzbot executed {0}'
        if member == self.bot.user:
            response = 'NO HAHA'
        else:
            await ctx.send('you know the rules and so do I')
            await asyncio.sleep(2)
            await ctx.send('say goodbye')
            await asyncio.sleep(1)
        await ctx.send(response.format(member))
        
def setup(bot): # a extension must have a setup function
	bot.add_cog(Fun(bot))