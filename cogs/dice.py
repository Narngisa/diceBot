import os
import random
import dotenv
import discord
from typing import Literal

from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()

GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="dice", description="Dice a roll")
    @app_commands.guilds(GUILD_ID)
    async def dice(self, interaction: discord.Interaction, amount: int , roll: Literal[2, 3, 4, 6, 8, 10, 12, 20, 100]):
    
        if amount <= 0:
            await interaction.response.send_message("Pls take a number greater than zero.")
            return

        if amount > 100:
            await interaction.response.send_message("Too many rolls (max 100).")
            return

        result = [random.randint(1, roll) for _ in range(amount)]
        total = sum(result)

        embed = discord.Embed(title=f"You rolled {amount}d{roll}", color=discord.Color.green())

        if amount == 1 and roll == 20:
            value = result[0]
            if value == 20:
                embed.title=f"Critical Success!!"
                embed.color=discord.Color.gold()
            elif value == 1:
                embed.title=f"Critical Fail..."
                embed.color=discord.Color.red()
    
        embed.add_field(name=f"Result", value=", ".join(map(str, result)), inline=False)
        embed.add_field(name=f"Total", value=str(total), inline=False)
    
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Dice(bot))
