import discord
from discord.ext import commands
import keep_alive
import os
import random

global snipemessages
snipemessages = ["your mother died, kid plays roblox at funeral, instantly regrets", "i played roblox at my moms funeral, gets 60000000000 bobux, no virus, clean, heoroione birne called, allah missed call, run, asshole. tich", "No anime support the motherland", "I couldn't think of a good snipe comment, so here", "amoung us sus sniped you OMG", "a trash panda sniped you", "creeper snipe. aw man", "The gay-man aka @j.#2383 sniped you", "wasted", "imagine getting sniped couldn't be me", "snipe", "kid gets sniped, the ending will shock you", "ur mother sniped you", "I have sniped this idiot"]

keep_alive.keep_alive()

token = os.environ['token']

client = commands.Bot(command_prefix=".")

global snipe_message_author
global snipe_message_content
global editsnipe_message_author
global editsnipe_message_content

author_pfp = {}
snipe_message_author = {}
snipe_message_content = {}
editsnipe_message_author = {}
editsnipe_message_content = {}

@client.event
async def on_ready():
    print("Jinxu is gay")

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author.display_name
     snipe_message_content[message.channel.id] = message.content
     author_pfp = message.author.avatar_url

@client.event
async def on_message_edit(message_before, message_after):
    editsnipe_message_author[message_before.channel.id] = message_before.author.display_name
    editsnipe_message_content[message_before.channel.id] = message_before.content

@client.command(brief="Get the ping")
async def ping(ctx):
  await ctx.send(f'Pong! In {(client.latency * 1000)}ms')

@client.command(brief="a command for the owner of this bot to delete the last snipe XD")
@commands.is_owner()
async def delsnipe(ctx):
  global snipe_message_author
  global snipe_message_content
  global editsnipe_message_author
  global editsnipe_message_content

  author_pfp = {}
  snipe_message_author = {}
  snipe_message_content = {}
  editsnipe_message_author = {}
  editsnipe_message_content = {}
  await ctx.send("I have deleted the snipe T_T")

'''
@client.command()
@commands.is_owner()
async def changebotnick(ctx, nick):
  await client.change_own_nick(all, nick)
  await ctx.send(f"Changed nickname to {nick} in {ctx.message.guild.name}")
'''

@client.command(brief="A command to recover the last deleted message")
async def snipe(ctx):
    channel = ctx.channel 
    temp = random.choice(snipemessages)
    try:
        snipeEmbed = discord.Embed(title=f"{temp} #{channel.name}", description = f"{snipe_message_content[channel.id]} - @{snipe_message_author[channel.id]}")
        snipeEmbed.set_footer(text=f"This nerds name is {snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
    except:
        await ctx.send(f"loser, there is nothing to snipe #{channel.name}")

@client.command(brief="A command to learn about the bot")
async def about(ctx):
  await ctx.send(f"snipe bot is a bot made by @{ctx.owner} because snipe is offline XD. Thanks to @j.#2383 for debugging help and help with the custom messages!")

@client.command(brief="A command to recover the last edited message")
async def esnipe(ctx):
    channel = ctx.channel
    temp = random.choice(snipemessages)
    try:
        editsnipeEmbed = discord.Embed(title=f"{temp} #{channel.name}", description = f"{editsnipe_message_content[channel.id]} - @{editsnipe_message_author[channel.id]}")
        editsnipeEmbed.set_footer(text=f"This nerds name is {editsnipe_message_author[channel.id]}")
        await ctx.send(embed = editsnipeEmbed)
    except:
        await ctx.send(f"loser, there is nothing to edit snipe #{channel.name}")

@client.event
async def on_command_error(ctx, error):
        '''
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("You tried to use something that doesn't exist, you failed")
        '''

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Error: missing Arguments")

        elif isinstance(error, commands.NotOwner):
            await ctx.send("idiot, this is a command that only the owner of the bot can run")

        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send("Error: NoPrivateMessage")

        elif isinstance(error, commands.CheckFailure):
            await ctx.send("Error: commands.CheckFailure")
        
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("command on cooldown")

client.run(token)