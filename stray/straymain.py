import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

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

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked for: {reason}')
    except discord.Forbidden:
        await ctx.send("I don't have permission to kick this user.")
    except discord.HTTPException:
        await ctx.send("An error occurred while trying to kick this user.")

@bot.command()
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, duration: int, *, reason=None):
    try:
        timeout_until = discord.utils.utcnow() + discord.timedelta(minutes=duration)
        await member.edit(timeout_until=timeout_until, reason=reason)
        await ctx.send(f'{member} has been muted out for {duration} minutes. Reason: {reason}')
    except discord.Forbidden:
        await ctx.send("I don't have permission to mute this user.")
    except discord.HTTPException:
        await ctx.send("An error occurred while trying to mute this user.")
        
@bot.command()
@commands.has_permissions(moderate_members=True)
async def delmute(ctx, member: discord.Member):
    try:
        await member.edit(timeout_until=None)
        await ctx.send(f'{member} has been unmuted.')
    except discord.Forbidden:
        await ctx.send("I don't have permission to unmute this user.")
    except discord.HTTPException:
        await ctx.send(f"An error occurred while trying to unmute {member}.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount} messages have been deleted.', delete_after=5)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    await ctx.send(f"Server Name: {guild.name}\nMembers: {guild.member_count}")

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar.url)

bot.run(token)