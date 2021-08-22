import discord
import subprocess
import mcipc.query
from discord.ext import commands

bot=commands.Bot(command_prefix="ぷりふぇくす")

TOKEN="botのトークン"

username="windowsのusername"

admin=["管理者たちのid"]

def get_status():
    try:
        pt = time.time()
        with mcipc.query.Client(config.host, config.port) as mcbe:
            status = mcbe.stats(full=True)
            ping = (time.time()-pt)*1000
        del mcbe
        return status, ping
    except:
        return None
      
@tasks.loop(seconds=30)
async def server_status_updater():
    await bot.wait_until_ready()
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, get_status)
    if not data:
        return await bot.change_presence(
            status=discord.Status.dnd, activity=discord.Game('サーバーがオフラインです'))
    st = f'サーバーは起動中です {data[0].num_players} / {data[0].max_players} | ping: {data[1]:.1f}ms'
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(st))

@bot.event()
async def on_ready():
  print(f"{bot.user}が起動しました)

# 起動コマンド
@bot.command
async def start(ctx):
  e=discord.Embed(title="NATION-SERVER-SYSTEM", description="起動中です...")
  m=await ctx.send(embed=e)
  subprocess.run(f"C:\Users\ {username}\Desktop\NATiON\bedrock-server-1.17.11.01/bedrock_server.exe", shell=True)
  e=discord.Embed(title="NATION-SERVER-SYSTEM", description="起動しました")
  await m.edit(e=embed)
        
@bot.command
async def stop(ctx):
  e=discord.Embed(title="NATION-SERVER-SYSTEM", description="終了させています")
  m=await ctx.send(embed=e)
  subprocess.run("taskkill /im bedrock_server.exe", shell=True)
  e=discord.Embed(title="NATION-SERVER-SYSTEM", description="終了しました")
  await m.edit(embed=e)
 
# shell command実行
@bot.listen(name="on_message")
async def shell(message):
  if not message.channel.id == 878987174769471518:
    return
  if str(message.author.id) in admin:
    returncode = subprocess.Popen(message.content, shell=True)
    await message.channel.send(returncode)
  else:
    await message.channel.send("権限が足りません")
  
        
bot.run(TOKEN)
