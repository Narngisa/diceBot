import os
import dotenv
import random
import discord

from typing import Literal
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
async def help(interaction: discord.Interaction):
    await interaction.response.send_message("Help ??")

@bot.tree.command(name="ping", description="Pong ?")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong : {latency} ms")

@bot.tree.command(name="dice", description="Roll a dice")
async def dice(interaction: discord.Interaction, amount: int , roll: Literal[2, 3, 4, 6, 8, 10, 12, 20, 100]):
    
    if amount <= 0:
        await interaction.response.send_message("Pls take a number greater than zero.")
        return

    result = [random.randint(1, roll) for _ in range(amount)]
    total = sum(result)

    embed = discord.Embed(title=f"You rolled {amount}d{roll}", color=discord.Color.green())
    embed.add_field(name=f"Result", value=f"{result}")
    embed.add_field(name=f"Total", value=f"{total}")
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="dice_negative", description="Roll a dice negative")
async def dice_negative(interaction: discord.Interaction, roll: int):
    
    if roll == 0:
        await interaction.response.send_message("Pls take a number other than zero.")
        return

    if roll < 0:
        roll_negative = roll * -1

    result = random.randint(1, roll_negative)
    
    if roll < 0:
        result = result * -1

    await interaction.response.send_message(f"You rolled: {result}")

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
