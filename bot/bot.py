import discord, discord_ios
from discord.ext import commands
from bot.startup import Startup

class harm(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=",", owner_ids=[214753146512080907],
                         intents = discord.Intents.all(), activity=discord.CustomActivity(name="🔗 harm.cc"))
        

    async def setup_hook(self):
        await self.load_extension('jishaku')
        await Startup.cogs(self)