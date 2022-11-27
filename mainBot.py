import asyncio
import discord
from async_timeout import timeout
from discord.ext import commands
from datebot import Date
from musicbot import Music
from valorMoeda import Binance
from valorant import Valorant

bot = commands.Bot('', description='Yet another music bot.', intents=discord.Intents.all())
async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.add_cog(Date(bot))
        await bot.add_cog(Binance(bot))
        await bot.add_cog(Valorant(bot))
        await bot.start('TOKEN-BOT')

@bot.event
async def on_ready():
    print('Logged in as: {0.user.name}'.format(bot))

asyncio.run(main())
