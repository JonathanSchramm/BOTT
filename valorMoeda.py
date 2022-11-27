from discord.ext import commands
import requests

class Binance(commands.Cog):
    @commands.command(name='binance')
    async def binance(self, ctx, coin, base):
        try:
            response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")

            data = response.json()
            price = data.get('price')

            if price:
                await ctx.send(f"O valor do par da moeda ({coin.upper()}{base.upper()}) é: ({price}{base.upper()})")

            else:
                await ctx.send(f"O valor do par da moeda ({coin}{base}) é: INVÁLIDO")

        except Exception as error:
            await ctx.send("Aconteceu algum erro")