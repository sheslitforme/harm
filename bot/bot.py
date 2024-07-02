import discord
from discord.ext import commands


class harm(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=",", owner_ids=[214753146512080907],
                         intents = discord.Intents.all())
        
bot = harm()

async def setup_hook(self):
    await bot.load_extension('jishaku')
    await bot.load_extension('cogs.owner')