# https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from wordle import * # allow us to use functions from wordle.py

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

wordlist = loadwordle()

@bot.command(name = "guess", help = "Make a guess of the current Wordle")
async def guess(ctx, input):
    await ctx.message.delete()
    currentword = getcurrentword(wordlist)
    await ctx.send("Your guess: ||" + input + "||\n" + checkguess(currentword, input)) # send output of function

bot.run(TOKEN)
