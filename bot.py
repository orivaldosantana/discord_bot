import discord
import random 
from discord.ext import commands 

import basico_nlp as m_nlp
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Stemmer 
pStemmer = PorterStemmer()
# 'stopwords' em português  
pt_stopwords = stopwords.words('portuguese') 

import pandas as pd
base_dados = pd.read_csv('https://raw.githubusercontent.com/ect-info/ml/master/dados/perguntas_e_respostas.tsv', delimiter = '\t', quoting = 3)
print(  base_dados.head() )  


import pickle
Xload = pickle.load(open("X.pickel", "rb"))
countV = pickle.load(open("CountVectorizer.pickle", "rb"))



## Criação do bot 
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

@client.command()
async def pergunta(ctx, *, input_message ):
    r = m_nlp.encontra_pergunta(2,input_message,pStemmer,Xload,pt_stopwords, base_dados, countV  )
    print(r) 
    await ctx.send(r)  

client.run('Nzg5MjE4NzE1MzEyMDYyNTA4.X9u3NA.4V87Q2ouz5zIA4OhwqLPb_7SQm0')