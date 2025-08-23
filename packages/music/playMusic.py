import discord
from discord.ext import commands
from discord import app_commands

class PlayMusic(commands.Cog): 
    def __init__(self, bot, controller):
        self.bot = bot
        self.controller = controller 
        
    @app_commands.command(name="play", description="Toca uma música do YouTube.")
    @app_commands.describe(busca="Digite o nome da música no YouTube")
    async def play(self, interaction: discord.Interaction, busca: str):
        await interaction.response.defer(thinking=True)

        # Verifica se o usuário está em um canal de voz
        try:
            voice_channel = interaction.user.voice.channel
        except:
            embedvc = discord.Embed(
                color=discord.Color.purple(),
                description='Para tocar uma música, primeiro se conecte a um canal de voz.'
            )
            await interaction.followup.send(embed=embedvc)
            return

        # Busca a música no YouTube
        song = self.controller.search_yt(busca)

        if not song:
            embedvc = discord.Embed(
                color=discord.Color.purple(),
                description='Algo deu errado! Tente outro nome ou vídeo.'
            )
            await interaction.followup.send(embed=embedvc)
            return

        # Adiciona à fila e tenta tocar
        self.controller.music_queue.append([song, voice_channel])

        embedvc = discord.Embed(
            color=discord.Color.purple(),
            description=f"Você adicionou a música **{song['title']}** à fila!"
        )
        await interaction.followup.send(embed=embedvc)

        if not self.controller.is_playing:
            await self.controller.play_music()