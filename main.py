from config import TOKEN, COGS

import os
import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix="s.", intents=discord.Intents.all()
)
cogs = [
    "cogs.%s" % os.path.splitext(cog_name)[0] for cog_name in os.listdir(COGS)
]


@bot.event
async def on_ready():
    print("[ BOT ] %s on ready" % bot.user)


def main():
    for cog in cogs:
        bot.load_extension(cog)
    
    bot.run(TOKEN)

if __name__ == "__main__":
    main()