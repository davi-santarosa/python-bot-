import discord
from discord.ext import commands

class JoinMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        
        #cria o embed para ser mostrado no servidor
        if guild.system_channel:
        
            embed_welcome = discord.Embed(
                title='Bem-vindo ao servidor',
                description=f'Olá, {member.mention}, bem-vindo ao **{guild.name}**',
                color=discord.Color.purple(),
            )
            embed_welcome.set_thumbnail(url=member.avatar.url if member.avatar else self.bot.user.avatar.url)
            await guild.system_channel.send(embed=embed_welcome)