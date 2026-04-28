import os
import dotenv
import discord

from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()

GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Pong ?")
    @app_commands.guilds(GUILD_ID)
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(title=f"🏓 Pong", description=f"Ping: {latency} ms", color=discord.Color.blurple())
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))
