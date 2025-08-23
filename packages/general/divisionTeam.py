import discord
import random
from discord.ext import commands


class DivisionTeam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='team', description='Cria dois times')
    async def team(self, ctx, *members: discord.Member):
# menos de 2 membros mencionados, envia uma mensagem de erro e encerra
        if len(members) < 2:
            await ctx.send("Você precisa mencionar pelo menos 2 membros para formar times!")
            return
        
#cria uma lista com os usuário definidos no argumento da função, dividi e separando em dois times 
        times_sorteio = list(members)
        random.shuffle(times_sorteio)
        metade = len(times_sorteio) // 2
        time_red = times_sorteio[:metade]
        time_blue = times_sorteio[metade:]

#criar um embed para mostrar os times 
        embed = discord.Embed(
            title="🎮 Sorteio de Times",
            description="Times sorteados aleatoriamente!",
            color=discord.Color.purple()
        )
        embed.add_field(name="Time RED 🟥", value="\n".join(m.mention for m in time_red), inline=True)
        embed.add_field(name="Time BLUE 🟦", value="\n".join(m.mention for m in time_blue), inline=True)

        await ctx.send(embed=embed)