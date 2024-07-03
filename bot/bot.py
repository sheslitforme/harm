import discord, discord_ios, os, asyncpg

from discord.ext import commands

from bot.startup import Startup
from bot.ext import HarmContext
from bot.database import create_tables

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
        
    async def create_db(self):
        self.db = await asyncpg.create_pool(port="5432", database=os.environ.get["database"], user=os.environ.get["user"], host="localhost", password=os.environ.get["password"])
        
    async def setup_hook(self):
        await create_tables(self)
        await self.create_db()
        await self.load_extension('jishaku')
        await Startup.cogs(self)
        
    async def get_context(self, message: discord.Message, cls=HarmContext) -> HarmContext:
      return await super().get_context(message, cls=cls)