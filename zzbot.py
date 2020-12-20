import os
import random
import discord
import time
from dotenv import load_dotenv
from discord.ext import commands
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the world burning"))
    
@bot.command(help='Checks the bot information')
async def zzbot(ctx):
    await ctx.send('Bot name: Zzbot')
    await ctx.send('Bot programmer: BakedP0tato#3698')
    await ctx.send('Bot version: v0.4')
    await ctx.send('Date created: 2020-11-23 13:08:08.474000')
    await ctx.send('Primary function: currently undetermined')


def check(context):
    def inner_check(message):
        return context.author == message.author and context.channel == message.channel
    return inner_check
    
@bot.command(help='Like a parrot, ya know')
async def repeat(ctx, *, sentence):
    if 'zzbot gei' in sentence:
        await ctx.send('NO HAHA')
    else:
        await ctx.send(sentence)
        
@bot.command(help='Capitalize every letter of the sentence')
async def upper(ctx, *, sentence):
    await ctx.send(sentence.upper())

@bot.command(help='Checks the ping')
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)}ms ')

@bot.command(help='A simple greeting')
async def hi(ctx):
    greetings = [
        'Hello',
        'Greetings',
        'Hi',
    ]
    response = random.choice(greetings)
    await ctx.send(response)

@bot.command(name='dice', help='Simulates rolling dice.')
async def roll_dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(help='Jojo quotes')
async def jojo(ctx):
    jojoquotes = [
        'My name is Yoshikage Kira. I\'m 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don\'t smoke, but I occasionally drink. I\'m in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I\'m trying to explain that I\'m a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn\'t lose to anyone.',
        'After a full revolution of time, a new world appeared! Destiny itself will repeat itself! When a human meets another human it is due to gravity! It happens because it was fated to be that way! And now, Humanity has experienced the future, and has now arrived at this world! For example, five years from now, what could happen? Everyone knows what will happen, now. During the Accelerated time they experienced when every accident, every illness, when their life would end… They already experienced it before arriving here. When will one meet another… and when will they separate… When will one meet another.. And when will they seperate? Who will love, and hate? What kind of child will one bear, and what kind of person will that child become? Who will commit crimes and who will invent, create works of beauty? The spirit, not the mindor body has already experienced and memorized those facts! And that is happiness! Not just one person, but everyone will be able to face their destiny! Ones who are able to face this are the ones who will be happy! You might think that knowing the ill fortunes of the future is despair but… It\'s the opposite! Even if you knew you were going to die tomorrow. It is that resolution that makes one happy! Ones resolution eradicated despair! Humanity will change! This is what is strived for! This is MADE IN HEAVEN!',
        'Suppose that you were sitting down at a table. The napkins are in front of you, which napkin would you take? The one on your ‘left’? Or the one on your ‘right’? The one on your left side? Or the one on your right side? Usually you would take the one on your left side. That is ‘correct’ too. But in a larger sense on society, that is wrong. Perhaps I could even substitute ‘society’ with the ‘Universe’. The correct answer is that ‘It is determined by the one who takes his or her own napkin first.’ …Yes? If the first one takes the napkin to their right, then there’s no choice but for others to also take the ‘right’ napkin. The same goes for the left. Everyone else will take the napkin to their left, because they have no other option. This is ‘society’… Who are the ones that determine the price of land first? There must have been someone who determined the value of money, first. The size of the rails on a train track? The magnitude of electricity? Laws and Regulations? Who was the first to determine these things? Did we all do it, because this is a Republic? Or was it Arbitrary? NO! The one who took the napkin first determined all of these things! The rules of this world are determined by that same principle of ‘right or left?’! In a Society like this table, a state of equilibrium, once one makes the first move, everyone must follow! In every era, this World has been operating by this napkin principle. And the one who ‘takes the napkin first’ must be someone who is respected by all. It’s not that anyone can fulfill this role… Those that are despotic or unworthy will be scorned. And those are the ‘losers’. In the case of this table, the ‘eldest’ or the ‘Master of the party’ will take the napkin first… Because everyone ‘respects’ those individuals.',
    ]

    response = random.choice(jojoquotes)
    await ctx.send(response)

@bot.command(help='Just rps')
async def rps(ctx):
    outcomes = [
        'rock',
        'paper',
        'scissors',
    ]
    
    bot_choice = random.choice(outcomes)
    await ctx.send(bot_choice)

@bot.command(name='server', help='Some info on the server')
async def fetchServerInfo(context):
	guild = context.guild
	
	await context.send(f'Server Name: {guild.name}')
	await context.send(f'Server Size: {len(guild.members)}')

@bot.command(help='See some info on a member in the server')
async def joined(ctx, *, member: discord.Member):
    fmt='{0} joined on {0.joined_at} and has {1} roles.'
    await ctx.send(fmt.format(member, len(member.roles)))

@bot.command(help='Lol')
async def rickroll(ctx, * ,member: discord.Member):
    response = 'Zzbot executed {0}'
    if member == bot.user:
        response = 'NO HAHA'
    else:
        await ctx.send('you know the rules and so do I')
        time.sleep(2)
        await ctx.send('say goodbye')
        time.sleep(1)
    await ctx.send(response.format(member))

@bot.command(help='Fights someone')
async def fight(ctx, member: discord.Member):   
    result=[
        '{0} tries to attack your leg, but you jumped and stepped on their head, victory!',
        'You make your first move by choking {0}, but they kicked your nuts, if you have any, and threw you with your legs. However, you still managed to pin them down by kicking their head, victory!',
        '{0} gobbles you up, defeat.',
        'You punched, but they blocked, then they punched, and you blocked too. In the end {0} kicked your head, defeat.',
        'None of you won because you both fainted, gg',
        '{0} grabs your head and smashed it into the wall, defeat.',
        'You grabbed a f****** machine gun and blasted everywhere, and you died too, gg',
        '{0} kicked your chest, and you grabbed their leg. You threw them into a car, victory!',
        'You drove your car and smashed into {0}, victory!',
        'You had a heart attack while in the fight, defeat.',
        '{0} brought a gun, and they shot themselves, victory!',
    ]
    if member == bot.user:
        await ctx.send('You don\'t get to fight me')
    elif member == ctx.author:
        await ctx.send('Sorry, you don\'t get to fight yourself.')
    else:
        response = random.choice(result)
        await ctx.send(response.format(member))

@bot.command(name='adv', help='a game')
async def adventure(ctx):
    await ctx.send('Choose : 1/2')
    msg = await bot.wait_for('message', check=check(ctx), timeout=30)
    if msg.content == '1':
        await ctx.send('Zombie apocalypse, everyone was running, which path do you choose? the road or the tunnel? (1/2)')
        msg = await bot.wait_for('message', check=check(ctx), timeout=30)
        if msg.content == '1':
            await ctx.send('You ran across the highway, you looked back and saw zombies devouring people, but you kept running.')
            await ctx.send('While you were running, you saw a wooden house, do you want to hide inside or continue running? (1/2)')
            msg = await bot.wait_for('message', check=check(ctx), timeout=30)
            if msg.content == '1':
                await ctx.send('You hid in a closet, a few zombies entered the house, run or stay? (1/2)')
                msg = await bot.wait_for('message', check=check(ctx), timeout=30)
                if msg.content =='1':
                    await ctx.send('They smelled you, run faster!')
                elif msg.content == '2':
                    await ctx.send('They smelled you, run!')
                await ctx.send('You crawled out from the bathroom window and continued running')
            elif msg.content == '2':
                await ctx.send('You ran south, together with thousands with survivors')
            await ctx.send('To be continued')
        elif msg.content == '2':
            await ctx.send('You crawled through the nasty tunnel and ends up in a burning village, you see soldiers walking around, interact with them or not? (1/2)')
            msg = await bot.wait_for('message', check=check(ctx), timeout=30)
            if msg.content == '1':
                await ctx.send('You talked to the leader')
                await ctx.send('Leader: Don\'t go near this area, you\'re a civilian, right? Go west, I believe there\'s some shelter.')      
            elif msg.content == '2':
                await ctx.send('You choose not to interact with them.')
            await ctx.send('Now, the zombies are coming from north, which direction do you choose? (1 for North, 2 for West, 3 for East, 4 for South)')
            msg = await bot.wait_for('message', check=check(ctx), timeout=30)
            if msg.content == '1':
                await ctx.send('You ran against the zombies! And you got eaten, the end')
            elif msg.content == '2':
                await ctx.send('You walked through a small path at the west, very few zombies chased this way, you probably chose the right path')
            elif msg.content == '3':
                await ctx.send('East is an ocean. Luckily, there are some boats. You quickly set off and left the cursed lands.')
            elif msg.content == '4':
                await ctx.send('You ran south, together with thousands with survivors')
            if msg.content == '2' or msg.content == '3' or msg.content == '4':
                await ctx.send('To be continued')
                
    elif msg.content == '2':
        await ctx.send('Test is succesful')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try >help ({error})')

bot.run(TOKEN)
