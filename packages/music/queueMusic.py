import discord
from discord.ext import commands
from discord import app_commands

class QueueMusic(commands.Cog): 
    def __init__(self, bot, controller):
        self.bot = bot
        self.controller = controller  

    @app_commands.command(name="queue", description="Mostra as atuais músicas da fila.")
    async def queue(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)

        if self.controller.music_queue:
            texto = "\n".join(
                f"**{i+1} -** {musica[0]['title']}" 
                for i, musica in enumerate(self.controller.music_queue)
            )
            embed = discord.Embed(color=12255232, description=texto)
        else:
            embed = discord.Embed(
                color=discord.Color.purple(), 
                description="Não há músicas na fila no momento."
            )

        await interaction.followup.send(embed=embed)