import discord 
import os 
from discord.ext import commands
from dotenv import load_dotenv
from yt_dlp import YoutubeDL 
from packages.music.searchMusic import SearchMusic
from packages.music.playMusic import PlayMusic
from packages.music.queueMusic import QueueMusic
from packages.music.skipMusic import SkipMusic
from packages.music.stopMusic import StopMusic
from packages.general.infoCommands import AllCommands
from packages.general.divisionTeam import DivisionTeam
from packages.general.joinMember import JoinMember
from packages.general.userInfo import UserInfo
from packages.general.ping import Ping

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix='!', 
    intents=intents, 
    )

@bot.event

async def on_ready(): 
    controller = SearchMusic(bot)

    await bot.add_cog(controller)
    await bot.add_cog(PlayMusic(bot, controller))
    await bot.add_cog(QueueMusic(bot, controller))
    await bot.add_cog(SkipMusic(bot, controller))
    await bot.add_cog(StopMusic(bot, controller)) 

    await bot.add_cog(Ping(bot))
    await bot.add_cog(AllCommands(bot))
    await bot.add_cog(DivisionTeam(bot))
    await bot.add_cog(JoinMember(bot))
    await bot.add_cog(UserInfo(bot))
    await bot.tree.sync()

    print('bot inicializado com sucesso')
    
bot.run(TOKEN)
