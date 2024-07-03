from discord.ext import commands

async def create_tables(self: commands.Bot): 
    await self.db.execute("CREATE TABLE IF NOT EXISTS prefixes (guild_id BIGINT, prefix TEXT)")  