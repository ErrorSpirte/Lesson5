import discord
from discord.ext import commands
import os, random
import requests

print(os.listdir('NameFolder'))

weights = {
    'ImageName1.jpg': 0.45,
    'ImageName2.jpg': 0.3,
    'ImageName3.jpg': 0.2,
    'ImageName4.jpg': 0.04,
    'ImageName5.jpg': 0.01,
    }

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"On ready {bot.user}")

@bot.command()
async def mems(ctx):
    img_name = random.choice(os.listdir('NameFolder'))
    with open(f'NameFolder/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memrandom(ctx):
    img_name = random.choices(list(weights.keys()), weights=list(weights.values()), k=1)[0]
    with open(f'NameFolder/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

#Ducks))
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
bot.run("Paste YOUR Token")
