import discord
import json
from discord.ext import commands
from discord import app_commands
import json
import logging

TOKEN = 'SOMEONES TOKEN HERE' 
intents = discord.Intents.default()
intents.members = True # Example: Enable member events
intents.message_content = True  # Enable the message_content intent
intents.presences = True  # Enable the presence intent

bot = commands.Bot(command_prefix='/', case_insensitive=True, intents=intents)

with open('data.json') as f:
    data = json.load(f)

tree = bot._connection._command_tree 

@bot.command(name='sync', description='Owner only')
async def sync(interaction: discord.Interaction):
        await tree.sync()
        print('Command tree synced.')



@bot.tree.command(name="gen2", description="Display information about Generation 2 AirPods")
async def gen2info(interaction: discord.Interaction):
    embed = discord.Embed(title="Gen 2", color=discord.Color.blue())
    product = data['versions']['gen2']

    embed.add_field(name="Chip Models", value=product['chipmodels'], inline=False)
    embed.add_field(name="Features", value="\n".join(product['features']), inline=False) 
    embed.add_field(name="Price", value=product['price'], inline=True)
    embed.add_field(name="Notes", value=product['note'], inline=True)

    # Add seller fields
    for seller_name in product['sellers']:
        seller = data['sellers'][seller_name]
        embed.add_field(name=seller_name, value=seller['store_link'], inline=True)

    await interaction.response.send_message(embed=embed)
