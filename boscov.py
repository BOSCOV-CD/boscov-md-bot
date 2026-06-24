import discord
from discord.ext import commands
import time
import psutil
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)
start_time = time.time()

def get_uptime():
    uptime_seconds = int(time.time() - start_time)
    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60
    return f"{hours}h {minutes}m"

@bot.event
async def on_ready():
    print(f'𖤓 BOSCOV MD ONLINE ☉\nLogged in as {bot.user}')
   
@bot.command()
async def menu(ctx):
    ram = psutil.Process().memory_info().rss / 1024
    embed = discord.Embed(
        title="𖤓 *𝗕𝗢𝗦𝗖𝗢𝗩 𝗠𝗗* 𖤓",
        description="☉ *The sun is high — BOSCOV stands proud*",
        color=0xFF8C00
    
      )
    embed.add_field(name="☉ *STATUS*", value=f'''

◦ *Version  :* V1 — Sunrise  
◦ *Mode     :* 🔒 Private
◦ *Prefix   :* .
◦ *RAM      :* {ram:.1f} MB
◦ *Uptime   :* {get_uptime()}
''', inline=False)
    embed.set_footer(text='𖤓 "Pride is my sin, loyalty is my virtue."')
    await ctx.send(embed=embed)

@bot.command()
async def hug(ctx, member: discord.Member = None):
    try: await ctx.message.delete()
    except: pass
    if member:
        try:
            await member.send(f"🤗 *BOSCOV* delivers a hug from {ctx.author.display_name}!\n☉ _The sun shines for you._")
        except: pass

bot.run(os.environ['DISCORD_TOKEN'])