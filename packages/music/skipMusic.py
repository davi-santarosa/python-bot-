import discord
from discord.ext import commands
from discord import app_commands

class SkipMusic(commands.Cog): 
    def __init__(self, bot, controller):
        self.bot = bot
        self.controller = controller  

    @app_commands.command(name="skip", description="Pula a atual música que está tocando.")
    @app_commands.default_permissions(manage_channels=True)
    async def skip(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)

        if self.controller.vc:
            self.controller.vc.stop()

        await self.controller.play_music()

        embed = discord.Embed(
            color=1646116,
            description="⏭️ Você pulou a música."
        )
        await interaction.followup.send(embed=embed)