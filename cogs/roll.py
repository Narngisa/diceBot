import os
import random
import dotenv
import discord

from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()

GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="roll", description="Multiple dice a roll")
    @app_commands.guilds(GUILD_ID)
    @app_commands.choices(roll=[
        app_commands.Choice(name="d2", value=2),
        app_commands.Choice(name="d3", value=3),
        app_commands.Choice(name="d4", value=4),
        app_commands.Choice(name="d6", value=6),
        app_commands.Choice(name="d8", value=8),
        app_commands.Choice(name="d10", value=10),
        app_commands.Choice(name="d12", value=12),
        app_commands.Choice(name="d20", value=20),
        app_commands.Choice(name="d100", value=100),
    ])
    async def roll(self, interaction: discord.Interaction, amount: int , roll: app_commands.Choice[int], modifiers: int):


        if not (1 <= amount <= 100):
            embed = discord.Embed(title="Pls take a number: (1 - 100)", color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
            return

        mods = f"+{modifiers}" if modifiers >= 0 else f"{modifiers}"

        result = [random.randint(1, roll.value) for _ in range(amount)]
        total = sum(result)

        embed = discord.Embed(title=f":game_die: You rolled {amount}{roll.name}", description=f"Modifiers: {mods}", color=discord.Color.green())            
        embed.add_field(name=f"Result", value=", ".join(map(str, result)))
        embed.add_field(name=f"Total", value=str(total + modifiers))
    
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(Roll(bot))
