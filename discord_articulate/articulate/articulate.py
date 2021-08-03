#this is an archive of what is on OracleCloud, this will be uploaded to GitHub.

import os

from discord.ext import commands
from dotenv import load_dotenv

'''
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
'''

bot = commands.Bot(command_prefix='!')
#sia = SentimentIntensityAnalyzer()

load_dotenv()
token = os.environ.get("token")

mCount = 0
totString = ''

#add current pingbot stuff here

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    channel = bot.get_channel(863235613465509888)
    await channel.send('I have awoken.')

'''
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!9875798893207758492098'):
        channel = bot.get_channel(860697230285340684)
        for i in range(1,100000):
            await channel.send('<@!679516527690776646>')
            time.sleep(0.5)
'''

@bot.command(name='pyramid')
async def triangle(ctx, arg):
    await ctx.send(arg)
    await ctx.send(arg+arg)
    await ctx.send(arg+arg+arg)
    await ctx.send(arg+arg+arg+arg)
    await ctx.send(arg+arg+arg+arg+arg)
    await ctx.send(arg+arg+arg+arg)
    await ctx.send(arg+arg+arg)
    await ctx.send(arg+arg)
    await ctx.send(arg)

#below works, but just inaccurate sentiment detection since uses lexicon, so cannot detect sarcasm that well.
    '''
@bot.event
async def on_message(message):
    global mCount
    global totString

    if message.author == bot.user:
        return

    if (mCount <= 5):
        totString = totString + ". " + message.content
        mCount += 1

    if (mCount > 5):
        polarity = sia.polarity_scores(totString)
        if (polarity['neg'] > polarity['pos']):
            channel = bot.get_channel(863235613465509888)
            await channel.send("Overall negative for past 5 messages. Difference " + str(polarity['neg']-polarity['pos']) + ".")
        if (polarity['pos'] > polarity['neg']):
            channel = bot.get_channel(863235613465509888)
            await channel.send("Overall positive for past 5 messages. Difference " + str(polarity['pos']-polarity['neg']) + ".")
            
        totString = ''
        mCount = 0

    await bot.process_commands(message)
'''

bot.run(token)
