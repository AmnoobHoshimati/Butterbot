import discord
from discord.ext import commands
import random, string
import time

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>')
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
 print("Ready for ya service")

snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(15)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@bot.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: 
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color = 0x57e5a8)
        em.set_footer(text = f"快點舔我:P {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: 
        await ctx.send(f"沒有被刪除的訊息uwu #{channel.name}")

@bot.event
async def on_member_join(member):
 channel = bot.get_channel(731856127372951635)
 await channel.send(f'{member} Joined')

@bot.event
async def on_member_remove(member):
 channel = bot.get_channel(731856127372951635)
 await channel.send(f'{member} Leaved')


@bot.command(pass_context = True)
async def gayrate(ctx):
 await ctx.send(random.randint(0,100))

@bot.command(pass_context = True)
async def simprate(ctx):
 await ctx.send(random.randint(0,100))
    
@bot.command(pass_context = True)
async def ping(ctx):
 await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def sayd(ctx,*,msg):
   await ctx.message.delete()
   await ctx.send(msg)

@bot.listen()
async def on_message(msg):
    if msg.content == 'h':
       await msg.channel.send('no jj ez')

@bot.command()
async def clean(ctx, num:int):
    await ctx.channel.purge(limit = num+1)
    await ctx.send("清理完成owo")

@bot.listen()
async def on_message(msg):
    if msg.content == 'goodbot':
       await msg.channel.send('thanks ouo')

@bot.listen()
async def on_message(msg):
    if msg.content == 'good':
       await msg.channel.send('good good')

@bot.listen()
async def on_message(msg):
    if msg.content == 'bad':
       await msg.channel.send('bad bad')













bot.run('')
