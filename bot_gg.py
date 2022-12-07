# criar canal temporario e gerar link do canal
# vincular o canal a usuario usando o id de authenticacao
# criar um botao de authenticacao no site gghub
# nome do canal = id do desafio, EX: desafio-29
# apos o fim do desafio excluir canal
# 1° Solucao = criar uma APi que enviar as informações da gghub pro codigo

import discord
from discord.ext import commands
#from time import sleep

client = commands.Bot(intents=discord.Intents.all(), command_prefix="!")

@client.event
async def on_ready():
    print(f'Logado como {client.user}!')

# Cria o Canal de Voz
@client.command()
async def criar(ctx, channelName):
    guild = ctx.guild
    categoria = discord.utils.get(ctx.guild.categories, name="TEST") #1
    mbed = discord.Embed(
        title='Canal de Voz',
        description=f'{channelName} criado com sucesso!',
    )
    if ctx.author.guild_permissions.manage_channels:
        await guild.create_voice_channel(name=channelName, user_limit=2, category=categoria)
        await ctx.send(embed=mbed)
       
# Pega o ID do canal de voz
@client.command()
async def canalid(ctx, *, given_name=None):
    for channel in ctx.guild.channels:
        if channel.name == given_name:
            wanted_channel_id = channel.id

    await ctx.send(wanted_channel_id)
   

# Criar um convite do canal
@client.command(pass_context=True)
async def convite(ctx):
    guild = ctx.guild
    #invitelink = await discord.abc.GuildChannel.create_invite(ctx.message.channel, max_uses=5,max_age=120) #2
    invitelink2 =  await guild.voice_channels[1].create_invite(max_uses=5, max_age=200)
    await ctx.send(invitelink2)

# Exclui o Canal de Voz
@client.command()
async def excluir(ctx, channel: discord.VoiceChannel):
    mbed = discord.Embed(
        title ='Canal de Voz',
        description = f'{channel} foi excluido com sucesso!'
    )
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send(embed=mbed)
        await channel.delete()

client.run('TOKEN')


# comentarios
#1 - o nome da categoria precisar estar com letra maiscula para funcionar
# cria um convite do servidor
