import os
import random
import discord
import time
from discord.ext import commands
import asyncio

TOKEN='NzM3NjU0ODg5NDg3Nzk0MjE3.XyAgpg.me6lFYdGGndCdQcg2BWsZsckmlo'
bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the world burning"))
    
@bot.command(help='Checks the bot information')
async def zzbot(ctx):
    await ctx.send('Bot name: Zzbot')
    await ctx.send('Bot programmer: BakedP0tato#3698')
    await ctx.send('Bot version: v0.8')
    await ctx.send('Date created: 2020-11-23 13:08:08.474000')
    await ctx.send('Primary function: currently undetermined')

@bot.command(help='recipes from Goodboirtly')
async def recipe(ctx):
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
async def fetchServerInfo(ctx):
	await ctx.send(f'Server Name: {ctx.guild.name}')
	await ctx.send(f'Server Size (including bots): {ctx.guild.member_count}')

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
    if member == bot.user:
        await ctx.send('You don\'t get to fight me')
    elif member == ctx.author:
        await ctx.send('You don\'t get to fight yourself.')
    else:
        await ctx.send('OK')

@bot.command(help='Basically a reminder, but it kills you')
async def kill_reminder(ctx):
    await ctx.send('Set timer: hours? (0 to 23)')
    msg = await bot.wait_for('message', check=check(ctx), timeout=30)
    hours = int(msg.content)
    if hours > 23:
        await ctx.send('No')
    else:
        await ctx.send('Set timer: minutes? (0 to 59)')
        msg = await bot.wait_for('message', check=check(ctx), timeout=30)
        minutes = int(msg.content)
        if minutes > 59:
            await ctx.send('No')
        else:
            await ctx.send('Set timer: seconds? (0 to 59)')
            msg = await bot.wait_for('message', check=check(ctx), timeout=30)
            seconds = int(msg.content)
            if seconds > 59:
                await ctx.send('No')
            else:
                sleepfor = seconds+minutes*60+hours*3600
                response = 'Ok, timer set: '+str(hours)+':'+str(minutes)+':'+str(seconds)
                await ctx.send(response)
                await asyncio.sleep(sleepfor)
                await ctx.send('Zzbot killed {}'.format(ctx.author.mention))
                
@bot.command(name='adv', help='a game')
async def adventure(ctx): 
    #await ctx.send('Choose : 1/2')
    #msg = await bot.wait_for('message', check=check(ctx), timeout=30)
    #if msg.content == '1':
    if ctx.author.id != 586536920763465749:
        await ctx.send('Game under development')
    else:
        def default():
            clue1 = False
            clue2 = False
            clue3 = False
            clue4 = False
            couple = False
            secret_ending = False
            cash = 300
            path = '1'
            path2 = '0'
            main = 'None'
            sub = 'None'
            zom = 300
            name = 'Unnamed'
            kill = True
        clue1 = False
        clue2 = False
        clue3 = False
        clue4 = False
        couple = False
        secret_ending = False
        cash = 300
        path = '1'
        path2 = '0'
        main = 'None'
        sub = 'None'
        zom = 300
        name = 'Unnamed'
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
                    await ctx.send('They saw you, run faster!')
                elif msg.content == '2':
                    await ctx.send('They sniffed, and then walked away, upon exiting the closet, you found a note on the table:')
                    await ctx.send('Mr Roger:'
                                   '\nWe are sincerely concerned about your project, as we live very close to your laboratory. My husband has asked you to exterminate the programme, but you insisted on continuing, shouldn\'t you be worried about the consequences you might face? I know you\'re a confident person, at least in my husband\'s perspective, but this has to stop you are pushing yourself into something you might regret.'
                                   '\nSincerely,'
                                   '\nMrs valrunt'
                                   )
                    await ctx.send('Continue? (any key)')
                    if msg.content == '>adv':
                            default()
                    else:
                        clue1 = True
                        msg = await bot.wait_for('message', check=check(ctx), timeout=40)
                        await ctx.send('You realize you cannot stay any longer as more and more zombies are approaching')
                await ctx.send('You crawled out from the bathroom window and continued running')
                await ctx.send('You can choose to either run with the survivors, or go for a small path at the west? (1/2)')
                msg = await bot.wait_for('message', check=check(ctx), timeout=30)
                if msg.content == '1':
                    path = '4'
                    await ctx.send('You ran south.')
                elif msg.content == '2':
                    path = '2'
                    await ctx.send('You ran west.')
                await ctx.send('Any key to continue')
                msg = await bot.wait_for('message', check=check(ctx), timeout=30)
                if msg.content == '>adv':
                    default()
            elif msg.content == '2':
                await ctx.send('You ran south, together with thousands of survivors')
                path = '4'
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
                path = '2'
            elif msg.content == '3':
                await ctx.send('You headed east. It was a jetty, with some boats.')
                await ctx.send('There are not enough boats for every person you see, so you have to snatch one. However, you saw an axe that can be a weapon, will you risk your time for a decent defense? (1 for getting it/2 for not)')
                msg = await bot.wait_for('message', check=check(ctx), timeout=30)
                if msg.content == '1':
                    hmm = random.randint(1, 7)
                    if hmm == 1:
                        await ctx.send('Too late, all the boats are taken, you have to go south')
                        sub = 'axe'
                        path = '4'
                    else:
                        await ctx.send('You got the axe and you got a boat, press any key to continue')
                        sub = 'axe'
                        msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                        path = '3'
                        if msg.content == '>adv':
                            default()
                elif msg.content == '2':
                    await ctx.send('You gave up the axe and went for the boat, press any key to continue')
                    msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                    path = '3'
                    if msg.content == '>adv':
                        default()
            elif msg.content == '4':
                await ctx.send('You ran south, together with thousands of survivors')
                path = '4'
        if path == '2':
            await ctx.send('After a long and exhausting run, you finally found shelter')
            await ctx.send('But, the zombies are here too')
            await ctx.send('Soldier: Here! Grab a gun!')
            await ctx.send('Soldier: You.. you need it..')
            await ctx.send('Continue? (any key) (You are about to fight zombies)')
            msg = await bot.wait_for('message', check=check(ctx), timeout=30)
            main = 'fabricated_rifle'
            await ctx.send('You grabbed the gun and slided into the barracks, hordes of zombies running towards you, get rid of a few in the front line first or throw a grenade straight away? (1 (skill)/2 (luck))')
            msg = await bot.wait_for('message', check=check(ctx), timeout=40)
            if msg.content == '>adv':
                default()
            else:
                kill = False
                if msg.content == '1':
                    await ctx.send('Quick! Type iskueadh in ten seconds, BE CAREFUL')
                    try:
                        msg = await bot.wait_for('message', check=check(ctx), timeout=11)
                    except asyncio.TimeoutError:
                        await ctx.send('Soldier: You know how to pull the trigger?')
                    if msg.content == 'iskueadh':
                        await ctx.send('You finished off the frontline and threw a grenade to finish the rest.')
                        kill = True
                    else:
                        await ctx.send('Soldier: Try again!')
                        try:
                            msg = await bot.wait_for('message', check=check(ctx), timeout=11)
                        except asyncio.TimeoutError:
                            pass
                        if msg.content == 'iskueadh':
                            await ctx.send('You finished off the frontline and threw a grenade to finish the rest.')
                            kill = True
                        else:
                            await ctx.send('The zombies ate you!')
                if msg.content == '2':
                    hmm = random.randint(1, 7)
                    if hmm == 1:
                        await ctx.send('You blew youself up')
                    else:
                        await ctx.send('The zombies were exterminated')
                        kill = True
                if kill == False:
                    pass
                else:
                    await ctx.send('Oscar: What\'s your name? I\'m Oscar, a soldier of the government to take care of these filthy creatures. (Enter your name)')
                    name = await bot.wait_for('message', check=check(ctx), timeout=360)
                    if msg.content == '>adv':
                        default()
                    else:
                        await ctx.send('Oscar: Oh, ok, so you\'re a civilian, do you want to help us clear these zombies, or stay back in the camps? (1/2) CHOOSE PROPERLY')
                        msg = await bot.wait_for('message', check=check(ctx), timeout=60)
                        if msg.content == '1':
                            await ctx.send('Oscar: I admire your courage, there are some weapons in the garage, you can choose whichever you like.')
                            await ctx.send('Weapon choices: '
                                           '\nFABRICATED RIFLE, your current weapon'
                                           '\nSEMI-AUTO SHOTGUN, the closer the target the higher the damage'
                                           '\nINCINERATING PISTOL, slowly burns the enemy'
                                           '\nDUST-10 CLAWS, extreme speed'
                                           )
                            await ctx.send('Choose (1/2/3/4) You can think slowly as weapon choices HEAVILY IMPACT your story outcomes')
                            msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                            if msg.content == '1':
                                await ctx.send('Oscar: So you want to stick with that, huh?')
                            elif msg.content == '2':
                                await ctx.send('Oscar: Shotgun, make sure you know how to use that')
                                main = 'semi-auto_shotgun'
                            elif msg.content == '3':
                                main = 'incinerator'
                                await ctx.send('Oscar: Good choice, I like that')
                            elif msg.content == '4':
                                main = 'DUST-10_claws'
                                await ctx.send('Oscar: That is Seargent Kevin\'s older claw model, now I think he has DUST-17 or something')
                            mw = 'Main weapon: '+main
                            sw = '\nSecondary weapon: '+sub
                            await ctx.send(mw)
                            await ctx.send(sw)
                            await ctx.send('Let\'s go! (any key)')
                            msg = await bot.wait_for('message', check=check(ctx), timeout=30)
                            if msg.content == '>adv':
                                default()
                            else:
                                await ctx.send('Oscar: Kevin? I thought you guys left the camps')
                                await ctx.send('Kevin: We had to stay back because of a couple of problems')
                                await ctx.send('Kevin: Huh, who are you?')
                                namesay = 'Oscar: '+name.content+', he just joined'
                                await ctx.send(namesay)
                                await ctx.send('Kevin: Hold on, I need this guy')
                                await ctx.send('Oscar: What? Why?')
                                await ctx.send('any key to continue')
                                msg = await bot.wait_for('message', check=check(ctx), timeout=30)
                                if msg.content == '>adv':
                                    default()
                                else:
                                    await ctx.send('Kevin: You don\'t have to understand, Oscar')
                                    await ctx.send('Oscar: Why not? I have the right to')
                                    await ctx.send('Kevin: Nexus Roger said he need this guy, I know nothing else, alright?')
                                    await ctx.send('Kevin: It\'s up to you, soldier! Do you trust me or you don\'t? (1/2) CHOOSE PROPERLY')
                                    msg = await bot.wait_for('message', check=check(ctx), timeout=50)
                                    if msg.content == '1':
                                        await ctx.send('Oscar: Alright, Kevin, take him as you want, and tell Dr. Roger that I said hi')
                                        await ctx.send('Kevin: OK, soldier! Stand up, you are following me to find Nexus Roger')
                                        path2 = 'Kevin'
                                    elif msg.content == '2':
                                        await ctx.send('Kevin: Since you rejected, I won\'t force you, it\'s your own loss')
                                        await ctx.send('Oscar: So you really aren\'t curious, huh?')
                                        path2 = 'Oscar'
                        elif msg.content == '2':
                            await ctx.send('Oscar: Alright then, stay in there, and do NOT get out during night, these things are pretty aggressive without sunlight')
                            search1 = False
                            search2 = False
                            search3 = False
                            search4 = False
                            search5 = False
                            search6 = False
                            search7 = False
                            search8 = False
                            search9 = False
                            search10 = False
                            i = 0
                            async def reject():
                                await ctx.send('Buddy, no going back the same place')
                                i -= 1
                            for i in range(3):
                                await ctx.send('While in the camp, you can search around for some stuff, maybe even weapons, you can search only 3: (1 to 10)')
                                msg = await bot.wait_for('message', check=check(ctx), timeout=30)
                                if msg.content == '1':
                                    if search1 == True:
                                        await reject()
                                    else:
                                        await ctx.send('You found a knife on the ground')
                                        if sub != 'None':
                                            await ctx.send('You currently have a secondary weapon: '+sub+' and you cannot carry two secondary weapons, do you want to switch? (1/2)')
                                            msg = await bot.wait_for('message', check=check(ctx), timeout=60)
                                            if msg.content == '1':
                                                await ctx.send('You got the knife')
                                                sub = 'knife'
                                                mw = 'Main weapon: '+main
                                                sw = '\nSecondary weapon: '+sub
                                                await ctx.send(mw)
                                                await ctx.send(sw)
                                            elif msg.content == '2':
                                                await ctx.send('You left the knife there')
                                                mw = 'Main weapon: '+main
                                                sw = '\nSecondary weapon: '+sub
                                                await ctx.send(mw)
                                                await ctx.send(sw)
                                        else:
                                            await ctx.send('You pick the knife up')
                                            sub = 'knife'
                                            mw = 'Main weapon: '+main
                                            sw = '\nSecondary weapon: '+sub
                                            await ctx.send(mw)
                                            await ctx.send(sw)
                                        search1 = True
                                elif msg.content == '2':
                                    if search2 == True:
                                        await reject()
                                    else:
                                        await ctx.send('You found a stash of money, and you want to keep it, but you see a couple trying to find it, will you be honest? (1/2)')
                                        msg = await bot.wait_for('message', check=check(ctx), timeout=30)
                                        if msg.content == '1':
                                            await ctx.send('Man: Oh thank god and thank you, we need that money for our son.')
                                            await ctx.send('Woman: Young man, we are sincerely sorry that we could do nothing to pay your kindness back. However, we can definitely help you when you need any!')
                                            couple = True
                                        elif msg.content == '2':
                                            await ctx.send('You kept that cash thinking you really need that money')
                                            cash += 1200
                                            coins = 'Current money: '+str(cash)
                                            await ctx.send(coins)
                                        search2 = True
                                elif msg.content == '3':
                                    if search3 == True:
                                        await reject()
                                    else:
                                        await ctx.send('A pile of garbage, nothing more')
                                        search3 = True
                                elif msg.content == '4':
                                    if search4 == True:
                                        await reject()
                                    else:
                                        await ctx.send('You found an ad of a man selling axes, he\'s at location 7')
                                        await ctx.send('You return to the camp, as there was nothing else interesting')
                                        search4 = True
                                elif msg.content == '5':
                                    if search5 == True:
                                        await reject()
                                    else:
                                        await ctx.send('You found a pile of dead zombies, you check thier bodies and found some cash')
                                        cash += 300
                                        coins = 'You have '+ str(cash)+' coins'
                                        await ctx.send(coins)
                                        search5 = True
                                elif msg.content == '6':
                                    if search6 == True:
                                        await reject()
                                    else:
                                        await ctx.send('Some parts to upgrade your rifle')
                                        if main == 'fabricated_rifle':
                                            await ctx.send('You equipped the parts to your rifle')
                                            main = 'fabricated_rifle_lvl2'
                                            mw = 'Main weapon: '+main
                                            sw = '\nSecondary weapon: '+sub
                                            await ctx.send(mw)
                                            await ctx.send(sw)
                                        else:
                                            await ctx.send('You currently have a main weapon: '+main+' and you cannot carry two main weapons, do you want to switch? (1/2)')
                                            msg = await bot.wait_for('message', check=check(ctx), timeout=60)
                                            if msg.content == '1':
                                                await ctx.send('You got the rifle back, and equipped the parts')
                                                main = 'fabricated_rifle_lvl2'
                                                mw = 'Main weapon: '+main
                                                sw = '\nSecondary weapon: '+sub
                                                await ctx.send(mw)
                                                await ctx.send(sw)
                                            elif msg.content == '2':
                                                await ctx.send('You left the parts there')
                                                mw = 'Main weapon: '+main
                                                sw = '\nSecondary weapon: '+sub
                                                await ctx.send(mw)
                                                await ctx.send(sw)
                                        search6 = True
                                elif msg.content == '7':
                                    if search7 == True:
                                        await reject()
                                    else:
                                        await ctx.send('You found a man who wants to sell an axe for 200 coins, do you want to accept the offer? (1/2)')
                                        coins = 'You have '+ cash+' coins'
                                        await ctx.send(coins)
                                        msg = await bot.wait_for('message', check=check(ctx), timeout=60)
                                        if msg.content == '1':
                                            if cash >= 200:
                                                if sub != 'None':
                                                    await ctx.send('You currently have a secondary weapon: '+sub+' and you cannot carry two secondary weapons, do you want to switch? (1/2)')
                                                    msg = await bot.wait_for('message', check=check(ctx), timeout=60)
                                                    if msg.content == '1':
                                                        await ctx.send('You accepted the trade and got an axe for melee protection')
                                                        sub = 'axe'
                                                        cash -= 200
                                                        mw = 'Main weapon: '+main
                                                        sw = '\nSecondary weapon: '+sub
                                                        await ctx.send(mw)
                                                        await ctx.send(sw)
                                                    elif msg.content == '2':
                                                        await ctx.send('You left the axe there')
                                                        mw = 'Main weapon: '+main
                                                        sw = '\nSecondary weapon: '+sub
                                                        await ctx.send(mw)
                                                        await ctx.send(sw)
                                                else:
                                                    await ctx.send('You accepted the trade and got an axe for melee protection')
                                                    sub = 'axe'
                                                    cash -= 200
                                                    mw = 'Main weapon: '+main
                                                    sw = '\nSecondary weapon: '+sub
                                                    await ctx.send(mw)
                                                    await ctx.send(sw)
                                                coins = 'You have '+ str(cash)+' coins'
                                                await ctx.send(coins)
                                            else:
                                                await ctx.send('Buddy, not enough money')
                                        search7 = True
                                elif msg.content == '8':
                                    if search8 == True:
                                        await reject()
                                    else:
                                        await ctx.send('Talk about bad luck, you met bullies. Luckily, you didn\'t lose anything.')
                                        search8 = True
                                elif msg.content == '9':
                                    if search9 == True:
                                        await reject()
                                    else:
                                        await ctx.send('You found a DUST-8 claws')
                                        if main != 'None':
                                            await ctx.send('You currently have a main weapon: '+main+' and you cannot carry two main weapons, do you want to switch? (1/2)')
                                            msg = await bot.wait_for('message', check=check(ctx), timeout=60)
                                            if msg.content == '1':
                                                await ctx.send('You got the claws')
                                                main = 'DUST-8_claws'
                                                mw = 'Main weapon: '+main
                                                sw = '\nSecondary weapon: '+sub
                                                await ctx.send(mw)
                                                await ctx.send(sw)
                                            elif msg.content == '2':
                                                await ctx.send('You left the claws there')
                                                mw = 'Main weapon: '+main
                                                sw = '\nSecondary weapon: '+sub
                                                await ctx.send(mw)
                                                await ctx.send(sw)
                                        else:
                                            await ctx.send('You equipped the claws')
                                            main = 'DUST-8_claws'
                                            mw = 'Main weapon: '+main
                                            sw = '\nSecondary weapon: '+sub
                                            await ctx.send(mw)
                                            await ctx.send(sw)
                                        search9 = True
                                elif msg.content == '10':
                                    if search10 == True:
                                        await reject()
                                    else:
                                        await ctx.send('You got some cash, by selling some stuff')
                                        cash += 500
                                        coins = 'Current money: '+str(cash)
                                        await ctx.send(coins)
                                        search10 = True
                            await ctx.send('Times up (any key to continue)')
                            msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                            if msg.content == '>adv':
                                default()
                            else:
                                await ctx.send('You went back to the camp, and you tried to sleep, but you couldn\'t. Someone poked your head with a branch')
                                await ctx.send('Clara: Hey fella. You couldn\'t sleep, right? How about helping us to take care of the zombies?')
                                await ctx.send('You: Clara? You\'re a soldier?')
                                await ctx.send('Clara: Oh, I\'m so sorry. I saw '+main+' in your hands so I thought you are one.')
                                await ctx.send('You: Nevermind, I couldn\'t sleep either')
                                await ctx.send('You picked up your weapon.')
                                path2 = 'Clara'                   
        elif path == '3':
            await ctx.send('You found some coins on the boat, roughly 200')
            cash += 200
            await ctx.send('You left the cursed lands, and look for the mainland.')
            await ctx.send('Well, your luck pretty much sucks, some unknown creature attack your boat. In a desperate situation, you landed the boat on an island.')
            await ctx.send('And you saw zombies, but they look much more stronger')
            await ctx.send('You are about to continuously type words displayed on the screen (in ten seconds each!) otherwise you will be eaten alive by the zombies')
            gugugaga = ['diwjc','wosci','gofkj','bovkc','weori','dfgrif','eodkss','woerifug','ygfvbergf','trfghuytr']
            kill = True
            await ctx.send('any key to start, you can only make 2 mistakes')
            msg = await bot.wait_for('message', check=check(ctx), timeout=200)
            if msg.content == '>adv':
                default()
            else:
                zom = 3
                for i in range(10):
                    gugu = gugugaga[i]
                    gig = str(zom)+' chance(s) left'
                    await ctx.send(gig)
                    await ctx.send(gugu)
                    try:
                        msg = await bot.wait_for('message', check=check(ctx), timeout=11)
                    except asyncio.TimeoutError:
                        zom -= 1
                        await ctx.send('Oof')
                    if msg.content == gugu:
                        await ctx.send('Nice')
                    else:
                        zom -= 1
                        await ctx.send('Oof')
                    if zom < 1:
                        await ctx.send('The zombies devoured you')
                        kill = False
                        break
                    else:
                        continue
                if kill == False:
                    pass
                else:
                    await ctx.send('You managed to survive the zombie attacks, and someone threw a fire bomb on the cannibals, killing them')
                    await ctx.send('Survivor: Welcome, to umm, an island. These are zombified monsters from the sea called goblins, unlike normal zombified humans, they are much more stronger')
                    await ctx.send('Survivor: Why don\'t you stay inside for a while? I\'ll take care of the rest')
                    await ctx.send('any key to continue')
                    msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                    if msg.content == '>adv':
                        default()
                    else:
                        await ctx.send('Alice: Hi,my name\'s Alice, the shelter is over there if you are new here.')
                        if sub == 'axe':
                            await ctx.send('Alice: Can I have that axe? It would help me a lot, thanks')
                            await ctx.send('Alice: I\'ll return it to you as soon as possible (any key)')
                            msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                            if msg.content == '>adv':
                                default()
                            else:
                                sub = 'None(axe)'
                        else:
                            pass
                        if zom > 100:
                            pass
                        else:
                            await ctx.send('You walked to the shelter and was shocked, all the survivors live in treehouses')
                            await ctx.send('Alice: Oh, ya, I forgot about that, there\'s normal houses, but you have to get use to treehouses as they attack once in a while')
                            if sub == 'None(axe)':
                                await ctx.send('Alice: Here your axe, thank you. I also upgraded a little bit on your axe')
                                sub = 'axe_lvl2'
                                mw = 'Main weapon: '+main
                                sw = '\nSecondary weapon: '+sub
                                await ctx.send(mw)
                                await ctx.send(sw)
                            else:
                                 await ctx.send('Alice: I think you need something to defend yourself, here\'s some fire bombs')
                                 sub = 'fire_bombs'
                                 buy1 = True
                            await ctx.send('You looked around, and saw a shop')
                            coins = 'You have '+ str(cash)+' coins'
                            await ctx.send(coins)
                            buy1 = False
                            await ctx.send('SHOP'
                                           '\nFire bombs: -100coins (Protection against the goblins)'
                                           '\nIce cream: -10coins (Idk, who doesn\'t love ice cream?)'
                                           '\nSell your axe: +50coins or more (If you have any, of course)'
                                           )
                            while True:
                                await ctx.send('1/2/3/4 (4 for continue)')
                                msg = await bot.wait_for('message', check=check(ctx), timeout=60)
                                if msg.content == '1':
                                    if sub != 'None' or sub!= 'fire_bombs':
                                        await ctx.send('You have a secondary weapon for now: '+sub+', so you can\'t buy, unless you sell the axe')
                                    else:
                                        if buy1 == True:
                                            await ctx.send('You have enough fire bombs')
                                        else:
                                            await ctx.send('Show owner: That\'s the old price buddy, new price is 150 coins')
                                            await ctx.send('1: Argue/2: Pay/3: leave')
                                            msg = await bot.wait_for('message', check=check(ctx), timeout=30)
                                            if msg.content == '1':
                                                await ctx.send('You argued with the shop owner. In the end, you won and bought the fire bombs for 100 coins')
                                                cash -= 100
                                                coins = 'You have '+ str(cash)+' coins'
                                                await ctx.send(coins)
                                                sub = 'fire_bombs'
                                                buy1 = True
                                            elif msg.content == '2':
                                                await ctx.send('You paid, like a fool. If a game calls you a fool, you really have to reconsider your life choices')
                                                cash -= 150
                                                coins = 'You have '+ str(cash)+' coins'
                                                await ctx.send(coins)
                                                sub = 'fire_bombs'
                                                buy1 = True
                                            elif msg.content == '3':
                                                await ctx.send('You left')
                                elif msg.content == '2':
                                    await ctx.send('Zzbot: Wait, you serious?')
                                    await ctx.send('Shop owner: Here you go')
                                    await ctx.send('You ate the ice cream')
                                    cash -= 10
                                    coins = 'You have '+ str(cash)+' coins'
                                    await ctx.send(coins)
                                elif msg.content == '3':
                                    if sub == 'axe':
                                        await ctx.send('You sold your axe and got 50 coins')
                                        cash += 50
                                        coins = 'You have '+ str(cash)+' coins'
                                        await ctx.send(coins)
                                    elif sub == 'axe_lvl2':
                                        await ctx.send('You sold your axe and got 100 coins!')
                                        cash += 100
                                        coins = 'You have '+ str(cash)+' coins'
                                        await ctx.send(coins)
                                    else:
                                        await ctx.send('Sorry, you have no axes')
                                elif msg.content == '4':
                                    break
                            await ctx.send('The sun is setting down, and Alice managed to get you a tree house. Do you want to go sleep or stay on the island? (1/2)')
                            msg = await bot.wait_for('message', check=check(ctx), timeout=60)
                            if msg.content == '1':
                                await ctx.send('You went to sleep, and you felt calm')
                                path2 = 'Alice'
                            elif msg.content == '2':
                                await ctx.send('You chose to guard the island from goblins, are you ready? (any key)')
                                gugugaga = ['isjsse','qpowsq','hjckdu','dpoazx','ufdjsa','fyxbzx','tifudj','hgfdgh','vcgdyu','agfhcnx']
                                random.shuffle(gugugaga)
                                kill = True
                                await ctx.send('any key to start, you can only make 4 mistakes')
                                msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                                if msg.content == '>adv':
                                    default()
                                else:
                                    zom = 5
                                    for i in range(10):
                                        gugu = gugugaga[i]
                                        gig = str(zom)+' chance(s) left'
                                        await ctx.send(gig)
                                        await ctx.send(gugu)
                                        try:
                                            msg = await bot.wait_for('message', check=check(ctx), timeout=11)
                                        except asyncio.TimeoutError:
                                            zom -= 1
                                            await ctx.send('Oof')
                                        if msg.content == gugu:
                                            await ctx.send('Nice')
                                        else:
                                            zom -= 1
                                            await ctx.send('Oof')
                                        if zom < 1:
                                            await ctx.send('The goblins devoured you')
                                            kill = False
                                            break
                                        else:
                                            continue
                                    if kill == False:
                                        pass
                                    else:
                                        await ctx.send('You managed to defeat the goblins and guard the island')
                                        await ctx.send('Alice: You did pretty well as the new guy here huh?')
                                        await ctx.send('Alice: As reward to the brave soldiers, we give them 500 coins per duty, here you go,')
                                        cash += 500
                                        coins = 'You have '+ str(cash)+' coins'
                                        await ctx.send(coins)
                                        path2 = 'Alice'
                            elif msg.content == '3':
                                secret_ending = True
                                path2 = 'whoami'
                                await ctx.send('SECRET PATH UNLOCKED')
                                await ctx.send('You looked down at the sea, suddenly a weird creature dragged you into the waters')
                                await ctx.send('You try to sturggle, but it is not helping, you slowly sink into the ocean bed')
                                await ctx.send('Any key')
                                msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                                if msg.content == '>adv':
                                    default()
                                else:
                                    pass
        elif path == '4':
            await ctx.send('You, togther with the survivors, ran, and ran, while the ones left behind were mercilessly devoured by the zombies')
            if sub == 'None':
                await ctx.send('You are in the middle, and the zombies are approximately 300 meters behind you, but you saw an abandoned revolver, do you want to get it? (1/2)')
                msg = await bot.wait_for('message', check=check(ctx), timeout=360)
                if msg.content == '1':
                    sub = 'revolver'
                    mw = 'Main weapon: '+main
                    sw = '\nSecondary weapon: '+sub
                    await ctx.send(mw)
                    await ctx.send(sw)
                    hmm = random.randint(1, 7)
                    if hmm == 1:
                        await ctx.send('You got the revolver, but you tripped. You are now close to the zombies, approximately 100 meters')
                        zom -= 200
                    else:
                        await ctx.send('You got it and got in back in your track, ')
                elif msg.content == '2':
                    await ctx.send('You continued running')
            else:
                pass
            await ctx.send('You are about to continuously type words displayed on the screen (in ten seconds each!) otherwise you and the zombies will be closer')
            gugugaga = ['ydidj','hfnsa','widsf','djkfj','ujdxc','disifj','pudhwns','owskdjc','wuufcsi','fudsjka']
            kill = True
            await ctx.send('any key to start')
            msg = await bot.wait_for('message', check=check(ctx), timeout=200)
            if msg.content == '>adv':
                default()
            else:
                for i in range(10):
                    gugu = gugugaga[i]
                    gig = str(zom)+' meters away from the zombies'
                    await ctx.send(gugu)
                    await ctx.send(gig)
                    try:
                        msg = await bot.wait_for('message', check=check(ctx), timeout=11)
                    except asyncio.TimeoutError:
                        drop = random.randint(10, 40)
                        zom -= drop
                        await ctx.send('Oof')
                    if msg.content == gugu:
                        await ctx.send('Nice')
                    elif msg.content == 'skip':
                        break
                    else:
                        drop = random.randint(10, 40)
                        zom -= drop
                        await ctx.send('Oof')
                    if zom < 10:
                        await ctx.send('The zombies devoured you')
                        kill = False
                        break
                    else:
                        continue
                if kill == False:
                    pass
                else:
                    region = 5
                    zomb = ['1','3']
                    danger = 1
                    seqhuh = ['1','2','3','4','5','6','7','8','9']
                    async def fight():
                        nonlocal danger
                        await ctx.send('Any key to fight')
                        msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                        zom = 3
                        kill = True
                        if sub == 'revolver':
                            goo = 10
                            zom = 10
                        elif sub == 'axe':
                            goo = 5
                        else:
                            goo = 10
                        if msg.content == '1':
                            gugugaga = ['djsfj','tejwi','enfjk','deiwo','uytiw','voajj','fueiw','rikwow','gpaos','tioep']
                            random.shuffle[gugugaga]
                            for i in range(goo):
                                gugu = gugugaga[i]
                                gig = str(zom)+' chances left'
                                await ctx.send(gugu)
                                await ctx.send(gig)
                                try:
                                    msg = await bot.wait_for('message', check=check(ctx), timeout=11)
                                except asyncio.TimeoutError:
                                    zom -= 1
                                    await ctx.send('Oof')
                                if msg.content == gugu:
                                    await ctx.send('Nice')
                                else:
                                    zom -= 1
                                    await ctx.send('Oof')
                                if zom < 1:
                                    await ctx.send('The zombies devoured you')
                                    kill = False
                                    break
                                else:
                                    continue
                            if kill == False:
                                default()
                            else:
                                await ctx.send('You cleared the zombies')
                                danger = 1
                    async def move():
                        if '1' in zomb:
                            moved = random.randint(1,5)
                            if moved == 1:
                                zomb.append('2')
                                zomb.remove('1')
                            elif moved == 2:
                                zomb.append('4')
                                zomb.remove('1')
                            else:
                                pass
                        if '2' in zomb:
                            moved = random.randint(1,5)
                            if moved == 1:
                                zomb.append('1')
                                zomb.remove('2')
                            elif moved == 2:
                                zomb.append('3')
                                zomb.remove('2')
                            else:
                                pass
                        if '3' in zomb:
                            moved = random.randint(1,5)
                            if moved == 1:
                                zomb.append('2')
                                zomb.remove('3')
                            elif moved == 2:
                                zomb.append('6')
                                zomb.remove('3')
                            else:
                                pass
                        if '4' in zomb:
                            moved = random.randint(1,5)
                            if moved == 1:
                                zomb.append('1')
                                zomb.remove('4')
                            elif moved == 2:
                                zomb.append('7')
                                zomb.remove('4')
                            else:
                                pass
                        if '5' in zomb:
                            moved = random.randint(1,5)
                            if moved == 1:
                                zomb.append('2')
                                zomb.remove('5')
                            elif moved == 2:
                                zomb.append('6')
                                zomb.remove('5')
                            else:
                                pass
                        if '6' in zomb:
                            moved = random.randint(1,5)
                            if moved == 1:
                                zomb.append('3')
                                zomb.remove('6')
                            elif moved == 2:
                                zomb.append('9')
                                zomb.remove('6')
                            else:
                                pass
                        if '7' in zomb:
                            moved = random.randint(1,5)
                            if moved == 1:
                                zomb.append('4')
                                zomb.remove('7')
                            elif moved == 2:
                                zomb.append('8')
                                zomb.remove('7')
                            else:
                                pass
                        if '8' in zomb:
                            moved = random.randint(1,5)
                            if moved == 1:
                                zomb.append('1')
                                zomb.remove('8')
                            elif moved == 2:
                                zomb.append('3')
                                zomb.remove('8')
                            else:
                                pass
                        if '9' in zomb:
                            moved = random.randint(1,5)
                            if moved == 1:
                                zomb.append('6')
                                zomb.remove('9')
                            elif moved == 2:
                                zomb.append('8')
                                zomb.remove('9')
                            else:
                                pass

                    async def run():
                        nonlocal region
                        await ctx.send('Choose a region to run to!(1 to 9) You are currently in region '+str(region))
                        msg = await bot.wait_for('message', check=check(ctx), timeout=40)
                        if msg.content == str(region):
                            nonlocal danger
                            if danger >= 6:
                                await ctx.send('Are you dumb? You got eaten, by the way.')
                                kill = False
                            else:
                                await ctx.send('Alright then, you want to stay here, huh?')
                                danger += 1
                        elif msg.content in seqhuh:
                            region = int(msg.content)
                            if str(region) in zomb and danger > 2:
                                await ctx.send('Sadly, you ran into zombies')
                                await fight()
                            else:
                                await ctx.send('No zombies, for now')
                                if str(region) in zomb:
                                    danger += 1
                                else:
                                    lis2 = [0] * 7 + [1] * 4
                                    lis = random.choice(lis2)
                                    if lis == 0:
                                        danger += 1
                                    else:
                                        pass
                                    await move()
                        elif msg.content == '10':
                            path2 == 'Kevin'
                            await ctx.send('You walked through a secret path, and found a few soldiers.')
                            await ctx.send('Soldier: He... he looks exactly like the man in the files earlier!')
                            await ctx.send('Kevin: I am Seargent Kevin, Dr Nexus Roger need to see you')
                            await ctx.send('Kevin: So, do you believe us?')
                            await ctx.send('Soldier: We have no time, Seargent. We must take him')
                            await ctx.send('Kevin: Just trust us, alright? We all have tasks to accomplish')
                            path2 = 'Kevin'
                    async def vortext():
                        if sub == 'None':
                            await ctx.send('Your only choice now is run! Make sure you don\'t run into zombies')
                            run()
                        elif sub =='revolver' or sub == 'revolver_lvl2':
                            await ctx.send('Kill the zombie or run (1 skill/2 luck)')
                            msg = await bot.wait_for('message', check=check(ctx), timeout=40)
                            if msg.content == '1':
                                await fight()
                            elif msg.content == '2':
                                await run()
                    gig = str(zom)+' meters away from the zombies'
                    await ctx.send('READ PROPERLY BEFORE PROCEEDING')
                    await ctx.send('You managed to survive the zombie attacks and ran into a forest')
                    await ctx.send('The sun is setting')
                    await ctx.send('You have to listen for zombies, follow clear paths, and a motion tracker which has limited battery')
                    await ctx.send('If you have a revolver, you can attack zombies at 10m range, if you have an axe, you can attack zombies at 2m range')
                    await ctx.send('Here is a map so that you know how to choose sides: (You are currently on region 5)')
                    await ctx.send('Make sure you don\'t choose alphabets during choices, you will be facing the sky if you choose alphabets (no joke)')
                    await ctx.send('1   2  3')
                    await ctx.send('4  5  6')
                    await ctx.send('7  8  9')
                    await ctx.send('Motion tracker help: Max battery: 5/Use one time (-1 battery)/ Charge (+2 battery every turn and unuseable during charge)')
                    await ctx.send('Ready? (any key)')
                    msg = await bot.wait_for('message', check=check(ctx), timeout=300)
                    if msg.content == '>adv':
                        default()
                    else:
                        battery = 5
                        gege = True
                        motio = 1
                        for i in range(10):
                            if not len(zomb):
                                zomb.append('1')
                                danger = 1
                            await ctx.send('Motion tracker: '+str(battery)+' battery')
                            await ctx.send('Use flashlight on which region? (1 to 9) (you are on region '+str(region)+')')
                            msg = await bot.wait_for('message', check=check(ctx), timeout=200)
                            if msg.content in zomb:
                                if danger == 1:
                                    await ctx.send('You hear mild zombie groans, but they were not close')
                                elif danger == 2:
                                    await ctx.send('Loud zombie groans, do not panic')
                                    danger -= 1
                                elif danger == 3:
                                    await ctx.send('Dead body, nothing else')
                                    danger -= 1
                                elif danger == 4:
                                    await ctx.send('A zombie lying on the ground, looks dead')
                                    danger -= 1
                                elif danger == 5:
                                    await ctx.send('You saw zombie shadows')
                                    danger -= 1
                                elif danger == 6:
                                    await ctx.send('HERE THEY ARE')
                                    await ctx.send('If you have a weapon, it\'s best you attack them here')
                                    await vortext()
                            else:
                                await ctx.send('No signs of danger')
                            if kill == False:
                                default()
                                break
                            else:
                                if motio == 1:
                                    if battery < 1:
                                        await ctx.send('Your motion tracker has run out of battery')
                                    else:
                                        await ctx.send('Do you want to use motion tracker? (-1 battery) (1/2)')
                                        msg = await bot.wait_for('message', check=check(ctx), timeout=40)
                                        if msg.content == '1':
                                            battery -= 1
                                            await ctx.send('Which side? (1 for region 1 2 3 4, 2 for region 5 6 7 8')
                                            msg = await bot.wait_for('message', check=check(ctx), timeout=40)
                                            if msg.content == '1':
                                                motiontrack = ['1','2','3','4']
                                            elif msg.content == '2':
                                                motiontrack = ['5','6','7','8']
                                            mot = list()
                                            hoi = any(item in zomb for item in motiontrack)
                                            for i in range(len(zomb)):
                                                if zomb[i] in motiontrack:
                                                    mot.append(zomb[i])
                                                else:
                                                    continue
                                            if hoi == True:
                                                await ctx.send('Motion detected: Region '+','.join(mot)+ '/Danger level: '+str(danger))
                                                if danger >= 6:
                                                    await ctx.send('HERE THEY ARE')
                                                    await ctx.send('If you have a weapon, it\'s best you attack them here')
                                                    vortext()
                                                else:
                                                    await ctx.send('They are not very close, luckily')
                                            else:
                                                await ctx.send('No motion detected')
                                        elif msg.content == '2':
                                            await ctx.send('You choose to preserve the battery')
                                        if kill == False:
                                            default()
                                            break
                                        else:
                                            if 0 < battery < 5:
                                                await ctx.send('Do you want to charge your motion tracker\'s battery? Charging produces loud noises that might attract zombies, however.')
                                                await ctx.send('(1/2)')
                                                msg = await bot.wait_for('message', check=check(ctx), timeout=40)
                                                if msg.content == '1':
                                                    my_list = [0] * 5 + [1] * 4
                                                    hmm = random.choice(my_list)
                                                    danger += hmm
                                                    await ctx.send('You are charging your motion tracker, you cannot use it until it was fully charged')
                                                    motio = 0
                                                elif msg.content == '2':
                                                    await ctx.send('You refuse to charge')
                                            elif battery == 0:
                                                await ctx.send('You have to charge your motion tracker')
                                            else:
                                                await ctx.send('Your motion tracker has full battery')
                                else:
                                    battery += 2
                                    if battery > 5:
                                        battery = 5
                                        await ctx.send('You fully charged your motion tracker')
                                        motio = 1
                                    else:
                                        await ctx.send('You are still charging your motion tracker')
                                        await ctx.send(str(battery)+'/5')
                                if kill == False:
                                    default()
                                    break
                                else:
                                    await run()
                                    if danger >= 6:
                                        kill = False
                                        await ctx.send('You did not realize the zombies at a certain region, they ate you')
                                        break
                            if path2 == 'Kevin':
                                break
                        if kill == False:
                            default()
                        else:
                            if path2 == 'Kevin':
                                pass
                            else:
                                await ctx.send('After a torturous night, you finally seemed to find the correct path, you find yourself back with the majority of the survivors!')
                                await ctx.send('You cannot continue your journey alone, you will have to find a team to follow. You do not have much time')
                                await ctx.send('1/2/3/4 You can only choose one')
                                msg = await bot.wait_for('message', check=check(ctx), timeout=40)
                                if msg.content == '1':
                                    path2 = 'Josh'
                                elif msg.content == '2':
                                    path2 = 'Gary'
                                elif msg.content == '3':
                                    path2 = 'Felicia'
                                elif msg.content == '4':
                                    path2 = 'Clint'
                        if path2 == 'Oscar':
                            await ctx.send('Any key to continue')
                            msg = await bot.wait_for('message', check=check(ctx), timeout=300)
                            if msg.content == '>adv':
                                default()
                            else:
                                await ctx.send('Oscar: So moving on, we have to go south, that\'s where all the zombies are')
                        elif path2 == 'Kevin':
                            await ctx.send('Any key to continue')
                            msg = await bot.wait_for('message', check=check(ctx), timeout=300)
                            if msg.content == '>adv':
                                default()
                            else:
                                await ctx.send('Kevin: Alright, we are about to go somewhere north, I know, zombies, but most of them aleady went south')
                                await ctx.send('After sleeping through the night and having a long walk, you saw a huge building')
                                await ctx.send('Kevin: Yes, the ACROM main building, you can see a lot of people trying to kill Roger for all the havoc')
                                await ctx.send('You: He... made the zombies?')
                                await ctx.send('Kevin: Not really, he\'s in charge of getting rid of the virus, someone let it out, and this ignorant bastards put all the blame on him')
                                await ctx.send('Any key to continue')
                                msg = await bot.wait_for('message', check=check(ctx), timeout=300)
                                if msg.content == '>adv':
                                    default()
                                else:
                                    
                                    if main == 'incinerator':
                                        await ctx.send('Hey, you got that incinerator, right? Some scumbag let the frostbots out')
                                    else:
                                        await ctx.send('Kevin: Some dipshit let the frostbots out, we can\'t take this way')
                        elif path2 == 'Clara':
                            await ctx.send('Path Clara')
                        elif path2 == 'Alice':
                            await ctx.send('Path Alice')
                        elif path2 == 'whoami':
                            await ctx.send('Path Secret')
                        elif path2 == 'Josh':
                            await ctx.send('Path Josh')
                        elif path2 == 'Gary':
                            await ctx.send('Path Gary')
                        elif path2 == 'Felicia':
                            await ctx.send('Path Felicia')
                        elif path2 == 'Clint':
                            await ctx.send('Path Clint')

#@bot.event
#async def on_command_error(ctx, error):
    #await ctx.send(f'Error. Try >help ({error})')

bot.run(TOKEN)
