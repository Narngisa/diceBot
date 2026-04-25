import os
import dotenv
import random
import discord

from discord import app_commands
from discord.ext import commands

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
        command_prefix = ":&:", 
        intents=intents, 
        help_command=None, 
        activity=discord.Streaming(name='/help for more info', url='https://linktr.ee/Narngisa')
)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(f"Exception detected: \n{e}")
    print(f"Synced: {len(synced)} command(s)")
    print(f"Successfully logged in as {bot.user} !!")

@bot.tree.command(name="help", description="Display all commands")
async def help(interaction=discord.Interaction):
    await interaction.response.send_message("Help ??")

@bot.tree.command(name="ping", description="Pong ?")
async def ping(interaction=discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong : {latency} ms")

@bot.tree.command(name="dice", description="Roll a dice")
async def dice(interaction=discord.Interaction):
    roll = random.randint(1, 20)
    await interaction.response.send_message(f"You rolled: {roll}")


TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
