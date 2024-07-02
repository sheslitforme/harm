import dotenv, logging, os
from bot.bot import harm

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

bot = harm()

if __name__ == '__main__':
  bot.run(token, reconnect=True)