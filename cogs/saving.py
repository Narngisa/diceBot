import os
import random
import dotenv
import discord
from typing import Literal

from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()

GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))

class SavingThrow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="saveing", description="Saving Throw with ability modifier")
    @app_commands.guilds(GUILD_ID)
    async def saving(self, interaction: discord.Interaction, ability: Literal["STR", "DEX", "INT", "CON", "WIS", "CHA"], modifiers: int):
    
        result = random.randint(1, 20)
        total = result + modifiers

        mod_txt = f"+{modifiers}" if modifiers >= 0 else f"{modifiers}"

        embed = discord.Embed(title=f"You saving throw: {ability}", description=f"Modifiers: {mod_txt}", color=discord.Color.green())
        embed.add_field(name=f"Result", value=f"{result}")
        embed.add_field(name=f"Total", value=f"{total}")

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(SavingThrow(bot))
