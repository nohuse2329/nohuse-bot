import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！専用Botだよ！")

# 先ほど取得したトークン（" "で囲む）
bot.run("MTU1Njk4ODA1NjM2NjYyMDcyMw.GQDeyI.7Hewng7EjPxhl7GmQb2rgRfcQuDF_5MW5JcGwQ")
