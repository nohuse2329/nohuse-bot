import os
import threading
import discord
from discord.ext import commands
from flask import Flask

# --- Render用のダミーWebサーバー設定 ---
app = Flask('')


@app.route('/')
def home():
  return 'Bot is alive!'


def run_flask():
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)


threading.Thread(target=run_flask).start()
# ----------------------------------------

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_member_join(member: discord.Member):
  channel = member.guild.get_channel(1557345458777628683)
  if not channel:
    return

  embed = discord.Embed(color=0x3498DB)
  embed.set_author(name=member.name)
  embed.add_field(name='名前', value=member.mention, inline=False)
  embed.add_field(name='ID', value=f'`{member.id}`', inline=False)
  embed.add_field(
      name='サーバー参加日',
      value=(
          member.joined_at.strftime('%Y年%m月%d日 %H時%M分')
          if member.joined_at
          else '不明'
      ),
      inline=False,
  )
  embed.add_field(
      name='アカウント作成日',
      value=member.created_at.strftime('%Y年%m月%d日 %H時%M分'),
      inline=False,
  )
  embed.set_thumbnail(url=member.display_avatar.url)
  embed.set_footer(text=f'実行者: {bot.user.name}')

  await channel.send(embed=embed)


token = os.getenv('DISCORD_TOKEN')
bot.run(token)
