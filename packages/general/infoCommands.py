
import discord
from discord.ext import commands

#classe para mostrar os comandos que podem ser executados 
class AllCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='about')
    async def about(self, ctx, member: discord.Member = None):
        member = member or ctx.author
    #cria o embes para ser mostrado para o servidor 
        embed_about = discord.Embed(
            title='Sobre o nosso bot',
            description= f'E aí {member.mention}, tudo certo? 🎧❄️',
            color=discord.Color.purple()
        )
        embed_about.add_field(name='\u200b', value='**📜 Lista de Comandos**', inline=False)
        embed_about.add_field(name='General', value="`!about`, `!ping`, `!team`, `!userinfo @user`", inline=False)
        embed_about.add_field(name='Music', value="`/play`, `/skip`, `/queue`, `/stop`", inline=False)
        
        await ctx.reply(embed=embed_about)
