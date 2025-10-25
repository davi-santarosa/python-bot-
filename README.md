# 🎶 Discord Bot em Python

Um bot completo desenvolvido em **Python** com a biblioteca **discord.py**, capaz de:
- 🎮 Criar times aleatórios entre os membros (`!team`)
- 🧑‍💻 Exibir informações detalhadas de usuários (`!userinfo`)
- 🎵 Tocar músicas diretamente do **YouTube**, usando **FFmpeg** e uma **API de extração de áudio**

---

## 🚀 Funcionalidades

### 🧩 `!team`
Cria **dois times aleatórios** com base nos membros mencionados.  
- 🔸 Divide automaticamente em `Time RED` e `Time BLUE`.  
- 🔸 Exibe o resultado em um **embed estilizado**.  
- 🔸 Garante que pelo menos dois membros sejam mencionados.

---

### 🧑‍💻 `!userinfo`
Mostra informações detalhadas sobre um usuário.  
- 🆔 ID do usuário  
- 📛 Nome e apelido  
- 🟢 Status  
- 📅 Data de criação da conta  
- 🔓 Data de entrada no servidor  
- 🎭 Lista de cargos  

---

### 🎵 `!play <nome da música ou link>`
Reproduz músicas diretamente de vídeos do **YouTube**.  
- Utiliza **FFmpeg** para processar o áudio.  
- Faz uso de uma biblioteca (como `yt_dlp` ou similar) para obter o áudio via **API do YouTube**.  
- Suporta links diretos ou busca por nome.  
- Se já houver música tocando, adiciona a nova na fila.  
- Inclui comandos como:
  - `!pause` → pausa a reprodução  
  - `!resume` → retoma a reprodução  
  - `!skip` → pula para a próxima música  
  - `!stop` → para tudo e limpa a fila  

---

## ⚙️ Requisitos

- Python **3.10+**
- [discord.py](https://pypi.org/project/discord.py/)
- [FFmpeg](https://ffmpeg.org/download.html) instalado no sistema
- [yt-dlp](https://pypi.org/project/yt-dlp/) ou biblioteca similar para extrair áudio do YouTube
- Token de bot válido do [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications)

