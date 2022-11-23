# create a discord.py command called ping that takes a user as an argument and then creates 100 webhooks in the original channel and mentions the user in the original channel with every webhook

import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx, user: discord.Member):
    # create a webhook then use it to mention the user
    for i in range(100):
        webhook = await ctx.channel.create_webhook(name='webhook')
        await webhook.send(f'{user.mention}', username='webhook', avatar_url=ctx.author.avatar_url)
        await webhook.delete()
        await asyncio.sleep(0.5)