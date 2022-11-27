from async_timeout import timeout
from discord.ext import commands
import datetime



class Date(commands.Cog):
    @commands.command(name='time')
    async def name(self, ctx: commands.Context):
        time = datetime.datetime.now()

        time = time.strftime('%d-%m-%Y e são %H:%M:%S')

        user = ctx.author.name

        response = "Olá, (" + user + ") agora é dia " + time

        await ctx.send(response)