import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# --- slash commands go here ---
@bot.tree.command(name="hello", description="Say hello to the bot")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}! 👋")

# --- event handlers ---
@bot.event
async def on_ready():
    print(f"-- Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"-- Commands loaded before sync: {[cmd.name for cmd in bot.tree.get_commands()]}")
    try:
        synced = await bot.tree.sync()
        print(f"-- Synced {len(synced)} global command(s)")
    except Exception as e:
        print(f"-- Error syncing commands: {e}")

bot.run(TOKEN)
