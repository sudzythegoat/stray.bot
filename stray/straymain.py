import discord
from discord.ext import commands
import requests
import json
bot = commands.Bot(command_prefix="?")
@bot.command()

async def ban(ctx, user):
  
