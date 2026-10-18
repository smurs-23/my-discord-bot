import discord
from discord.ext import commands
from datetime import datetime


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}!")
    print("Type !uceed in your Discord server to test it.")

# 2. The On-Demand Command
@bot.command(name="uceed")
async def uceed_reminder(ctx):
    # Target: Jan 17, 2027 at 9:00 AM sharp
    exam_date = datetime(2027, 1, 17, 9, 0)
    now = datetime.now()
    
    # Calculate the exact time gap
    time_left = exam_date - now
    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    minutes_left = (time_left.seconds % 3600) // 60
    
    # Check if the exam has already started/passed
    if time_left.total_seconds() <= 0:
        await ctx.send("The UCEED 2027 exam has begun or is already over! Hope everyone did amazing!")
    else:
        # Send the precise countdown directly to the channel where they typed the command
        await ctx.send(f"**UCEED REMINDER** \n **{days_left} days, {hours_left} hours, and {minutes_left} minutes** left for UCEED 2027.\nBe mindful. Keep grinding! 💪")


@bot.command(name="nid")
async def nid_reminder(ctx):
    # Target: Dec 20, 2026 at 9:00 AM sharp
    exam_date = datetime(2026, 12, 20, 9, 0)
    now = datetime.now()
    
    # Calculate the exact time gap
    time_left = exam_date - now
    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    minutes_left = (time_left.seconds % 3600) // 60
    
    # Check if the exam has already started/passed
    if time_left.total_seconds() <= 0:
        await ctx.send("The NID exam has begun or is already over! Hope everyone did amazing!")
    else:
        # Send the precise countdown directly to the channel where they typed the command
        await ctx.send(f"**NID REMINDER** \n **{days_left} days, {hours_left} hours, and {minutes_left} minutes** left for NID.\nBe mindful. Keep grinding! 💪")




import os

# Fetch the token safely from the cloud platform's memory
token = os.getenv("DISCORD_TOKEN")
bot.run(token)

