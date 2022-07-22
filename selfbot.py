import discord
from discord.ext import commands
from discord.utils import get
import ctypes
import json
import asyncio

##--Simple Dank Memer autofarm selfbot--##

prefix = "!!"

bot = commands.Bot(prefix, self_bot=True)

ctypes.windll.kernel32.SetConsoleTitleW("Made by LiteEagle262 | liteeagle.me")


@bot.event
async def on_ready():
    print(f"""
  ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗     ██████╗ ███╗   ██╗██╗     ██╗███╗   ██╗███████╗██╗
  ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝    ██╔═══██╗████╗  ██║██║     ██║████╗  ██║██╔════╝██║
  ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║       ██║   ██║██╔██╗ ██║██║     ██║██╔██╗ ██║█████╗  ██║
  ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║       ██║   ██║██║╚██╗██║██║     ██║██║╚██╗██║██╔══╝  ╚═╝
  ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║       ╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║███████╗██╗
  ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝        ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝
                                                      Commands:
                         {prefix}dankfarm | Starts Dank memer bot farm in the channel the command was executed

                                     To Power Off the bot Close This terminal
                                  If the bot doesnt work it meens your token is wrong

                                  To start the bot Please insert your token Below

    """)
    token = input("Please Paste your token ->>") 

@bot.command(pass_context=True)
async def dankfarm(ctx):
    await ctx.message.delete()
    await ctx.send('auto dank memer is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(3)
            await ctx.send('pls beg')
            print(f"{Fore.GREEN}succefully begged")
            await ctx.send('pls fish')
            print(f"{Fore.GREEN}succefully fished")
            await ctx.send('pls hunt')
            print(f"{Fore.GREEN}succefully hunt")
            await ctx.send('pls dep all')
            print(f"{Fore.GREEN}succefully deposited all")
            await asyncio.sleep(47)

bot.run(token, bot=False)
