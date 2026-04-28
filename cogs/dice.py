import os
import random
import dotenv
import discord

from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()

GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="dice", description="Dice a roll")
    @app_commands.guilds(GUILD_ID)
    @app_commands.choices(dice=[
        app_commands.Choice(name="1d2", value=2),
        app_commands.Choice(name="1d3", value=3),
        app_commands.Choice(name="1d4", value=4),
        app_commands.Choice(name="1d6", value=6),
        app_commands.Choice(name="1d8", value=8),
        app_commands.Choice(name="1d10", value=10),
        app_commands.Choice(name="1d12", value=12),
        app_commands.Choice(name="1d20", value=20),
        app_commands.Choice(name="1d100", value=100),
    ])
    async def dice(self, interaction: discord.Interaction , dice: app_commands.Choice[int], modifiers: int):
    
        result = random.randint(1, dice.value)

        mods = f"+{modifiers}" if modifiers >= 0 else f"{modifiers}"

        embed = discord.Embed(title=f"🎲 You rolled {dice.name}", description=f"Modifiers: {mods}", color=discord.Color.green())

        crit_high = { 20: 20, 100: 100 }
        crit_low = { 20: 1, 100: 1 }

        if result == crit_high.get(dice.value) :
            embed.title=f"👑 Critical Success!!"
            embed.color=discord.Color.gold()
        elif result == crit_low.get(dice.value):
            embed.title=f"💀 Critical Fail..."
            embed.color=discord.Color.red()                              

        embed.add_field(name=f"Result", value=str(result))
        embed.add_field(name=f"Total", value=str(result + modifiers))
    
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Dice(bot))
