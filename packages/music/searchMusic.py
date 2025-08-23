
import discord
from discord.ext import commands
from discord import app_commands
from yt_dlp import YoutubeDL

class SearchMusic(commands.Cog): 
    def __init__(self, bot,):
        self.bot = bot
        self.is_playing = False
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio[ext=m4a]', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn -loglevel debug'
        }
        self.vc = None

    def search_yt(self, item):
        ydl_opts = self.YDL_OPTIONS
        with YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(f"ytsearch:{item}", download=False)['entries'][0]
                for fmt in info['formats']:
                    if fmt.get('ext') == 'm4a' and fmt.get('acodec') != 'none':
                        url = fmt['url']
                        print("🔊 URL de áudio encontrada:", url)
                        return {'source': url, 'title': info['title']}
            except Exception as e:
                print("Erro ao extrair áudio:", e)

                return False
    def play_next(self):
            if len(self.music_queue) > 0:
                self.is_playing = True
                m_url = self.music_queue[0][0]['source']
                self.music_queue.pop(0)
                self.vc.play(
                    discord.FFmpegPCMAudio(
                        executable="D:\\python bot_discord\\bin\\ffmpeg\\ffmpeg.exe",
                        source=m_url,
                        **self.FFMPEG_OPTIONS
                    ),
                    after=lambda e: self.play_next()
                )
            else:
                self.is_playing = False

    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']
            if self.vc is None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])
            self.music_queue.pop(0)
            self.vc.play(
                discord.FFmpegPCMAudio(
                    executable="D:\\python bot_discord\\bin\\ffmpeg\\ffmpeg.exe",
                    source=m_url,
                    **self.FFMPEG_OPTIONS
                ),
                after=lambda e: self.play_next()
            )
        else:
            self.is_playing = False
            if self.vc:
                await self.vc.disconnect()
