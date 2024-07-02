import discord, logging, os, dotenv
from discord.ext import commands

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

dotenv.load_dotenv(verbose=True)

token = os.environ['token']

class harm(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=",", owner_ids=[214753146512080907],
                         intents = discord.Intents.all())
        
bot = harm()

@bot.event()
async def on_ready():
    print(f"{bot.user.name} has successfully connected to Discord API.")
    await bot.load_extension('jishaku')
    await bot.load_extension('cogs.owner')