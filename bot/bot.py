import discord, discord_ios, os, asyncpg
from discord.ext import commands
from bot.startup import Startup
from bot.ext import HarmContext

class harm(commands.Bot):
    def __init__(self, db: asyncpg.Pool=None):
        super().__init__(command_prefix=",", owner_ids=[214753146512080907],
                         intents = discord.Intents.all(), allowed_mentions=discord.AllowedMentions(roles=False, everyone=False, users=True, replied_user=False), 
                         activity=discord.CustomActivity(name="🔗 harm.cc"))
        
        
        self.db = db
        self.color = 0xffffff
        
        self.resent_api = os.environ.get["resent_api"]
        self.proxy = os.environ.get["proxy"]
        
        self.commands_url = os.environ.get("commands_url")
        self.support_server = os.environ.get("support_server")
        
    async def setup_hook(self):
        await self.load_extension('jishaku')
        await Startup.cogs(self)
        
    async def get_context(self, message: discord.Message, cls=HarmContext) -> HarmContext:
      return await super().get_context(message, cls=cls)