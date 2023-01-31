import discord
from discord.ext import commands
import dice

intents = discord.Intents.all()

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print('Conectado com sucesso!')

@bot.slash_command()
async def teste(ctx, texto=''):
    print(f'Enviado o texto: {texto}!')
    await ctx.respond(f'Comando enviado por: {ctx.author.name}')

@bot.slash_command()
async def dado(ctx, rolagem=''):
    res = dice.calcDices(rolagem.strip())
    await ctx.respond(res['msg'])

@bot.slash_command()
async def help(ctx):
    msg = dice.getExample()
    await ctx.respond(msg)


@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    
    if ctx.content.startswith('!dice'):
        text = ctx.content.replace("!dice", '').strip()
        if len(text) == 0:
            await ctx.channel.send(dice.getExample())
        else:
            try:
                res = dice.calcDices(text)
                if res['status'] == 'ok':
                    msg = res['msg']
                else:
                    msg = res['msg']
            except:
                msg = "Houve um erro"

            await ctx.channel.send(msg)
        
KEY = open('key').read()
bot.run(KEY)


