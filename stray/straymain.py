import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned for: {reason}')
    except discord.Forbidden:
        await ctx.send("I don't have permission to ban this user.")
    except discord.HTTPException:
        await ctx.send("An error occurred while trying to ban this user.")

bot.run('YOUR_BOT_TOKEN')
