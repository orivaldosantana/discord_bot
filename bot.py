import discord
import random 
from discord.ext import commands 

client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print('O bot monitor está pronto!!')


@client.command() 
async def ping(ctx):
    await ctx.send('pong!')

@client.command(aliases=['teste','oi'])
async def bot(ctx, *, input_message ):
    responses = ['Olá!','Tudo bem?','Como vai?','oi','Como posso ajudar?']
    print(input_message) 
    await ctx.send(f'{random.choice(responses) }') 

client.run('Nzg5MjE4NzE1MzEyMDYyNTA4.X9u3NA.4V87Q2ouz5zIA4OhwqLPb_7SQm0')