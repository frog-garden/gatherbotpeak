import asyncio
import discord
import random

from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready to use!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("/gather"):
            await client.send_message(message.channel, random.choice([ "```What the...? A **Perfectly Round Pebble** sits by your paws! *(1 point)*```",]
            
client.run("NTQzNTYyNTY0NjU1NjQ0Njc0.D1INqw.G4SOFq80z3KGNbxogA2HmE3zr0c")
client.login(process.env.BOT_TOKEN);
