import discord
import subprocess
from discord.ext import commands

bot=commands.Bot(command_prefix="ぷりふぇくす")

TOKEN="botのトークン"

username="windowsのusername"

@bot.event()
async def on_ready():
  print(f"{bot.user}が起動しました)

# 起動コマンド
@bot.command
async def start(ctx):
  e=discord.Embed(title="NATION-SERVER-SYSTEM", description="起動中です...")
  m=await ctx.send(embed=e)
  subprocess.run(f"C:\Users\ {username}\Desktop\NATiON\bedrock-server-1.17.11.01", shell=True)
  e=discord.Embed(title="NATION-SERVER-SYSTEM", description="起動しました")
  await m.edit(e=embed)
  
bot.run(TOKEN)
