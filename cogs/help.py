import os
import dotenv
import discord

from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()

GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Display all commands")
    @app_commands.guilds(GUILD_ID)
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="📖 Help Commands", color=discord.Color.blue())
        
        for command in self.bot.tree.get_commands(guild=GUILD_ID):
            embed.add_field( name=f"/{command.name}", value=command.description or "No description", inline=False )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
