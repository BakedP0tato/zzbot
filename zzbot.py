import os
import random
import discord
import time
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
    await ctx.send('Bot version: v2.0')
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

@bot.command(help='Jojo quotes')
async def jojo(ctx, choice=100):
    jojoquotes = [
        'My name is Yoshikage Kira. I\'m 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don\'t smoke, but I occasionally drink. I\'m in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I\'m trying to explain that I\'m a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn\'t lose to anyone.',
        'After a full revolution of time, a new world appeared! Destiny itself will repeat itself! When a human meets another human it is due to gravity! It happens because it was fated to be that way! And now, Humanity has experienced the future, and has now arrived at this world! For example, five years from now, what could happen? Everyone knows what will happen, now. During the Accelerated time they experienced when every accident, every illness, when their life would end… They already experienced it before arriving here. When will one meet another… and when will they separate… When will one meet another.. And when will they seperate? Who will love, and hate? What kind of child will one bear, and what kind of person will that child become? Who will commit crimes and who will invent, create works of beauty? The spirit, not the mindor body has already experienced and memorized those facts! And that is happiness! Not just one person, but everyone will be able to face their destiny! Ones who are able to face this are the ones who will be happy! You might think that knowing the ill fortunes of the future is despair but… It\'s the opposite! Even if you knew you were going to die tomorrow. It is that resolution that makes one happy! Ones resolution eradicated despair! Humanity will change! This is what is strived for! This is MADE IN HEAVEN!',
        'Suppose that you were sitting down at a table. The napkins are in front of you, which napkin would you take? The one on your ‘left’? Or the one on your ‘right’? The one on your left side? Or the one on your right side? Usually you would take the one on your left side. That is ‘correct’ too. But in a larger sense on society, that is wrong. Perhaps I could even substitute ‘society’ with the ‘Universe’. The correct answer is that ‘It is determined by the one who takes his or her own napkin first.’ …Yes? If the first one takes the napkin to their right, then there’s no choice but for others to also take the ‘right’ napkin. The same goes for the left. Everyone else will take the napkin to their left, because they have no other option. This is ‘society’… Who are the ones that determine the price of land first? There must have been someone who determined the value of money, first. The size of the rails on a train track? The magnitude of electricity? Laws and Regulations? Who was the first to determine these things? Did we all do it, because this is a Republic? Or was it Arbitrary? NO! The one who took the napkin first determined all of these things! The rules of this world are determined by that same principle of ‘right or left?’! In a Society like this table, a state of equilibrium, once one makes the first move, everyone must follow! In every era, this World has been operating by this napkin principle. And the one who ‘takes the napkin first’ must be someone who is respected by all. It’s not that anyone can fulfill this role… Those that are despotic or unworthy will be scorned. And those are the ‘losers’. In the case of this table, the ‘eldest’ or the ‘Master of the party’ will take the napkin first… Because everyone ‘respects’ those individuals.',
    ]
    choice -= 1
    if 0 <= choice < len(jojoquotes):
        response = jojoquotes[choice]
    elif choice == 100:
        response = random.choice(jojoquotes)
    else:
        response = "Not in list"
    await ctx.send(response)

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

bot.run(TOKEN)