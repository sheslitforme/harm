import discord, discord_ios
from discord.ext import commands
from bot.startup import Startup
from bot.ext import HarmContext

class harm(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=",", owner_ids=[214753146512080907],
                         intents = discord.Intents.all(), allowed_mentions=discord.AllowedMentions(roles=False, everyone=False, users=True, replied_user=False), 
                         activity=discord.CustomActivity(name="🔗 harm.cc"))
        
        self.color = 0xffffff
        
    async def setup_hook(self):
        await self.load_extension('jishaku')
        await Startup.cogs(self)
        
    async def get_context(self, message: discord.Message, cls=HarmContext) -> HarmContext:
      return await super().get_context(message, cls=cls)