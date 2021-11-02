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
                guess = int(round(msg.content))
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

    @commands.command(help='Jojo quotes')
    async def jojo(ctx, choice=100):
        jojoquotes = [
            'My name is Yoshikage Kira. I\'m 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don\'t smoke, but I occasionally drink. I\'m in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I\'m trying to explain that I\'m a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn\'t lose to anyone.',
            'After a full revolution of time, a new world appeared! Destiny itself will repeat itself! When a human meets another human it is due to gravity! It happens because it was fated to be that way! And now, Humanity has experienced the future, and has now arrived at this world! For example, five years from now, what could happen? Everyone knows what will happen, now. During the Accelerated time they experienced when every accident, every illness, when their life would end… They already experienced it before arriving here. When will one meet another… and when will they separate… When will one meet another.. And when will they seperate? Who will love, and hate? What kind of child will one bear, and what kind of person will that child become? Who will commit crimes and who will invent, create works of beauty? The spirit, not the mindor body has already experienced and memorized those facts! And that is happiness! Not just one person, but everyone will be able to face their destiny! Ones who are able to face this are the ones who will be happy! You might think that knowing the ill fortunes of the future is despair but… It\'s the opposite! Even if you knew you were going to die tomorrow. It is that resolution that makes one happy! Ones resolution eradicated despair! Humanity will change! This is what is strived for! This is MADE IN HEAVEN!',
            'Suppose that you were sitting down at a table. The napkins are in front of you, which napkin would you take? The one on your ‘left’? Or the one on your ‘right’? The one on your left side? Or the one on your right side? Usually you would take the one on your left side. That is ‘correct’ too. But in a larger sense on society, that is wrong. Perhaps I could even substitute ‘society’ with the ‘Universe’. The correct answer is that ‘It is determined by the one who takes his or her own napkin first.’ …Yes? If the first one takes the napkin to their right, then there’s no choice but for others to also take the ‘right’ napkin. The same goes for the left. Everyone else will take the napkin to their left, because they have no other option. This is ‘society’… Who are the ones that determine the price of land first? There must have been someone who determined the value of money, first. The size of the rails on a train track? The magnitude of electricity? Laws and Regulations? Who was the first to determine these things? Did we all do it, because this is a Republic? Or was it Arbitrary? NO! The one who took the napkin first determined all of these things! The rules of this world are determined by that same principle of ‘right or left?’! In a Society like this table, a state of equilibrium, once one makes the first move, everyone must follow! In every era, this World has been operating by this napkin principle. And the one who ‘takes the napkin first’ must be someone who is respected by all. It’s not that anyone can fulfill this role… Those that are despotic or unworthy will be scorned. And those are the ‘losers’. In the case of this table, the ‘eldest’ or the ‘Master of the party’ will take the napkin first… Because everyone ‘respects’ those individuals.',
        ]
        try:
            choice = int(round(choice)) - 1
        except ValueError:
            await ctx.send("Must be a number")
        if 0 <= choice < len(jojoquotes):
            response = jojoquotes[choice]
        elif choice == 99:
            response = random.choice(jojoquotes)
        else:
            response = "Not in list"
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