import os
import dotenv
import random
import asyncio
import discord

from discord import app_commands
from discord.ext import commands

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(
        command_prefix = ":&:", 
        intents=intents, 
        help_command=None, 
        activity=discord.Streaming(name='/help for more info', url='https://linktr.ee/Narngisa')
)

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            name = f"cogs.{filename[:-3]}"
            try:
                if name in bot.extensions:
                    await bot.reload_extension(name)
                else:
                    await bot.load_extension(name)
                print(f"Successfully: {filename}")
            except Exception as e:
                print(f"ERR: {filename} -> {e}")

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync(guild=GUILD_ID)
    except Exception as e:
        print(f"Exception detected: \n{e}")
    print(f"Synced: {len(synced)} command(s) to Guild ID: {GUILD_ID.id}")
    print(f"Successfully logged in as {bot.user} !!")

@bot.tree.command(name="reload", description="reload all commands in cogs", guild=GUILD_ID)
@app_commands.checks.has_permissions(administrator=True)
async def reload(interaction: discord.Interaction):

    await interaction.response.defer(ephemeral=True)
    
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        await load_cogs()
        synced = await bot.tree.sync(guild=GUILD_ID)
   
        await interaction.followup.send(f"Reloaded successfully! Synced {len(synced)} commands.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Reload failed:\n```{e}```", ephemeral=True)

@reload.error
async def reload_error(ineraction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingPermissions):
        await interaction.response.send_message("You need admin permission to use this.", ephemeral=True)

async def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    await load_cogs()
    await bot.start(TOKEN)

asyncio.run(main())
