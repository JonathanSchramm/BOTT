from discord.ext import commands
import valorant
import os
import requests

class Valorant(commands.Cog):
    @commands.command(name='valorant')
    async def valorant(self, ctx):

        key = requests.get('https://pd.{KEY') ##("RGAPI-670ea104-73fa-4352-ac16-f5f00790e32f")
        client = valorant.Client(key, locale=None)

        lb = client.get_leaderboard()

        results = "Top Players in BR" + lb

        await ctx.send(results)
