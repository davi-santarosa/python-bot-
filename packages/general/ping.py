import discord
from discord.ext import commands

#classe para verificar a latencia em ms do bot 
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'Pong! Latência {latency}ms')