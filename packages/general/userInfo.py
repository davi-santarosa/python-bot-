import discord
from discord.ext import commands


class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userinfo', description='Mostra info dos usuários que estão no servidor')
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        roles = [role.mention for role in member.roles if role != ctx.guild.default_role]
        roles_str = ", ".join(roles) if roles else "Nenhum cargo"
    #cria e mostra o embed no servidor 
        embed = discord.Embed(
            title=f"🔍 Informações de {member.display_name}",
            color=member.color if member.color.value else discord.Color.purple()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.add_field(name="🆔 ID", value=member.id, inline=True)
        embed.add_field(name="📛 Nome", value=member.name, inline=True)
        embed.add_field(name="🏷️ Apelido", value=member.nick or "Nenhum", inline=True)
        embed.add_field(name="🟢 Status", value=str(member.status).title(), inline=True)
        embed.add_field(name="📅 Conta criada em", value=member.created_at.strftime("%d/%m/%Y %H:%M"), inline=True)
        embed.add_field(name="🔓 Entrou no servidor", value=member.joined_at.strftime("%d/%m/%Y %H:%M"), inline=True)
        embed.add_field(name="🎭 Cargos", value=roles_str, inline=False)
        
        await ctx.send(embed=embed)
