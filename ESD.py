import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '?')
Clientdiscord = discord.Client()

@client.event
async def on_member_join(member):
    print(member.name + ' joined the server!')
    await client.send_message(member, 'Hello, '  + member.name + ' and welcome to the unofficial Electric State Discord server, read the rules before chatting in general or any other channel this server has to offer. Have fun! (Bot Prefix: ?)')
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Game(name='1 server', type = 3))
    print('The bot is now online!') 


@client.event
async def on_message(message):
    await client.send_message(message)
    if message.content == '?infofamas':
        await client.send_message(message.channel, 'Famas has 26 bullets in one magazine, its accuracy is good, this gun deals 26 damage per hit (4 shot kill), Famas has the same fire rate as an M4 (fast), the price of this gun is around 13k-15k, the upgrade price is 4k but users charge around 6k, you will also need an M4 to craft it.')
    if message.content == '?infotommygun':
        await client.send_message(message.channel, 'Tommy Gun is the same as Famas, the only differences are it has 25 bullets in one magazine, it is using SMG ammo and the fire rate is slow, the price of this gun is around 25k, the upgrade price is 7.5k but users charge 15k-20k for it, you will also need an M4 to craft it.')
    if message.content == '?infospywatch':
        await client.send_message(message.channel, 'Spy Watch is an item that can make you go invisible until you unequip it, the price is around 100k-200k making it the most expensive item in the whole game, the upgrade price is 100k, you will also need a Recaller to craft it.')
    if message.content == '?infojetpack':
        await client.send_message(message.channel, 'Jetpack is an item that can make you fly, the price of it is 10k-13k, there is also an upgrade which will turn it into a Static variant making it slightly faster and quieter the price of the upgrade is 1.2k, Static variant is 15k-20k.')
    if message.content == '?infogarand':
        await client.send_message(message.channel, 'Garand is a really strong gun it deals 40 damage per hit (3 shot kill), it is a great gun to use if you are shooting someone from far away (really accurate and has a long range), there is only 8 bullets in the magazine, the price of this gun is around 10k-20k, this gun has a slow fire rate, the upgrade price is 7.5k but people charge 10k for it, you will also need an M16 to craft it.')
    if message.content == '?infoxm8':
        await client.send_message(message.channel, 'XM8 is an assault rifle with ammo capacity of 20 bullets in one magazine, this gun deals 30 damage per hit making it a 4 shot kill gun, users are selling this weapon mostly for an average price of 9k, the upgrade price is 4k but users charge 5.5k for it, this gun has a pretty standart fire rate, you will also need an AK to craft this gun.')
    if message.content == '?inforemington':
        await client.send_message(message.channel, 'Remington is a shotgun with ammo capacity of 6 shotgun shells, this gun deals 20 damage per projectile it takes 1 shot to kill a user (short range), Remington is very good for Bounty Hunters, the price of this gun is 10k-15k, the price for the upgrade is 4k but users charge 6.5k for it, this gun has the slowest fire rate in the game, you will also need an M4 to craft it.')
    if message.content == '?infoballisticfist':
        await client.send_message(message.channel, 'Ballistic Fist is probably the best weapon in the game, the ammo capacity of this gun is 15 bullets in one "magazine", this gun deals 26(?) making it 4 shots to kill a user but this gun can shoot 2 shots at once making it only 2 shots to kill a user, the price of this gun is 10k-35k, the price for the upgrade is 10k but users charge 15k for it, you will also need an M4 to craft it.')
    if message.content == '?credits':
        await client.send_message (message.channel, 'Created by BaddyGamingCZ \nContact BaddyGamingCZ#0487 if you have any issues with the bot.')
    if message.content == '?version':
        await client.send_message(message.channel, '-Electric State Database v1.2')
    if message.content == '?rfb':
        await client.send_message(message.channel, 'no anime you fricking weeb')
    if message.content == '?help':
        await client.send_message(message.channel, 'Commands: \nprefix: ?  \ninfofamas \ninfotommygun \ninfospywatch \ninfojetpack \ninfogarand \ninfoxm8 \ninforemington \ninfoballisticfist \nversion \nupdatelog \ncoinflip \ncredits')
    if message.content == '?updatelog':
        await client.process_message(message.channel, 'Update Log: \nAdded coin flip command and credits.')
    if message.content == '?coinflip':
        randomlist = ['Heads', 'Tails']
        await client.process_message(message.channel, (random.choice(randomlist)))

client.run('NTYwMTc2MTk3MzgwNzM0OTk3.D3yvdw.m-6xv6KZlL_LUgH7SFueIYC-_-A')
client.run(os.getenv('TOKEN'))
