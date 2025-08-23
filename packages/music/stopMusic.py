import discord
import discord
from discord.ext import commands
from discord import app_commands

class StopMusic(commands.Cog): 
    def __init__(self, bot, controller):
        self.bot = bot
        self.controller = controller  

    @app_commands.command(name="stop", description="Para a música, limpa a fila e desconecta do canal de voz.")
    async def stop(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)

        if self.controller.vc and self.controller.vc.is_connected():
            self.controller.vc.stop()
            await self.controller.vc.disconnect()
            self.controller.vc = None

        self.controller.music_queue.clear()
        self.controller.is_playing = False

        embed = discord.Embed(
            color=discord.Color.purple(),
            description="⏹️ A música foi parada, a fila foi limpa e o bot saiu do canal de voz."
        )
        await interaction.followup.send(embed=embed)