import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
x = 'b!'
modrole = 'unset'
joinmsg = 0
answers = {
    1:'It is certain',
    2:'It is decidedly so',
    3:'Without a doubt',
    4:'Yes - definitely',
    5:'You may rely on it',
    6:'As I see it, yes',
    7:'Most likely',
    8:'Outlook good',
    9:'Yes',
    10:'Signs point to yes',
    11:'Reply hazy, try again',
    12:'ASk again later',
    13:'Better not tell you now',
    14:'Cannot predict now',
    15:'Concentrate and ask again',
    16:"Don't count on it",
    17:'My reply is no',
    18:'My sources say no',
    19:'Outlook not so good',
    20:'Very doubtful'

}
delmsg = []
bot = commands.Bot(command_prefix=x)
client = discord.Client()
@bot.event
async def on_ready():
    print('Ready')
    print('Running on {}'.format(bot.user.name))
    print('With the id of {} '.format(bot.user.id))
    await bot.change_presence(game=discord.Game(name='{}help for help'.format(x)))


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say('Pong!')

@bot.command(pass_context=True)
async def eightball(ctx):
    answer = random.randint(0,len(answers))
    await bot.say('{}, '.format(answers[answer]) + ctx.message.author.name)
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say('Cya {}'.format(user))
    await bot.kick(user)
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.display_name),description="Here's some info",color=0x00ffff)
    embed.add_field(name='Username',value=user,inline=True)
    embed.add_field(name='ID',value=user.id,inline=True)
    embed.add_field(name='Status',value=user.status)
    embed.add_field(name='Highest Role',value=user.top_role)
    embed.add_field(name='Joined at',value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def serverinfo(ctx):
    response = discord.Embed(title="{}'s info".format(ctx.message.server.name),description="Here's what I could find",color=0x00ffff)
    response.add_field(name="Server Name",value=ctx.message.server.name)
    response.add_field(name="Server ID",value=ctx.message.server.id)
    response.add_field(name="Server Roles",value=len(ctx.message.server.roles))
    response.add_field(name="Server Members",value=len(ctx.message.server.members))
    response.set_thumbnail(url=ctx.message.server.icon_url)
    response.set_footer(text='Brought to you by {}'.format(bot.user.display_name))
    await bot.say(embed=response)
@bot.command(pass_context=True)
async def say(ctx,message,text='',msg='',m1='',m2='',m3='',m4='',m5='',m6='',m7=''):
    await bot.delete_message(ctx.message)
    await bot.say(message + ' ' + text + ' ' + msg + ' ' + m1 + ' ' + m2 + ' ' + m3 + ' ' + m4 + ' ' + m5 + ' ' + m6 + ' ' + m7)
@bot.command(pass_context=True)
async def dice(ctx,text):
    text = eval(text)
    a = random.randint(0,text)
    await bot.say('You rolled {}'.format(a))
@bot.command(pass_context=True)
async def clear(ctx,amount=100):
    channel = ctx.message.channel
    async for message in bot.logs_from(channel,limit=int(amount)):
        delmsg.append(message)
    await bot.delete_messages(delmsg)



bot.run(Insert Token Here)
