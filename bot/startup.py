import discord, os, sys
from discord.ext import commands


class Startup:
    async def startup(bot):
        await bot.wait_until_ready()
    
    async def cogs(self):
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
             try:
                await self.load_extension(f"cogs.{file[:-3]}")
                print(f"Loaded plugin {file[:-3]}".lower())
             except Exception as e: print("failed to load %s %s".lower(), file[:-3], e)