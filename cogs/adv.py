import os
import random
import dotenv
import discord
from typing import Literal

from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()

GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))

class Adv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="adv", description="Advantage or Disadvantage")
    @app_commands.guilds(GUILD_ID)
    async def adv(self, interaction: discord.Interaction, dice: Literal["Advantage", "Disadvantage"], modifiers: int):

        result = [random.randint(1, 20) for _ in range(2)]

        mods = f"+{modifiers}" if modifiers >= 0 else f"{modifiers}"
        
        value = max(result) if dice == "Advantage" else min(result)
        text = "High Value" if dice == "Advantage" else "Low Value"

        embed = discord.Embed(title=f"⚔️ {dice} roll", description=f"Modifiers: {mods}", color=discord.Color.green())            

        if value == 20:
            embed.description=f"👑 Critical Success!!"
            embed.color=discord.Color.gold()
        elif value == 1:
            embed.description=f"💀 Critical Fail..."
            embed.color=discord.Color.red()
    
        embed.add_field(name=f"Result", value=", ".join(map(str, result)))
        embed.add_field(name=text, value=str(value))
        embed.add_field(name="Total", value=str(value + modifiers))
    
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Adv(bot))
