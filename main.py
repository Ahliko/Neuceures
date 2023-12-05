from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='config')

intents = discord.Intents.default()
intents.message_content = True
prefix = ''

bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


@bot.command()
async def echo(ctx, *kwargs):  # !hello
    if not kwargs:
        await ctx.send("Précise un argument")
    else:
        await ctx.send(' '.join(kwargs))


@bot.command()
async def whoareu(ctx):
    await ctx.send("grr grrr je suis bastien et je suis pas content grrrrrrr <@407940245108293635>")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    for i in bot.all_commands:
        if message.content.startswith(i):
            await bot.process_commands(message)


bot.run(os.getenv('TOKEN'))
