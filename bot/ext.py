import discord
from discord.ext.commands import Context 
from typing import Any, Dict

class HarmContext(Context): 
  flags: Dict[str, Any] = {}
 
  async def success(self, message: str) -> discord.Message:  
    return await self.reply(embed=discord.Embed(color=self.bot.color, description=f"> {self.author.mention}: {message}") )
 
  async def error(self, message: str) -> discord.Message: 
    return await self.reply(embed=discord.Embed(color=self.bot.color, description=f"> {self.author.mention}: {message}") ) 
 
  async def warning(self, message: str) -> discord.Message: 
    return await self.reply(embed=discord.Embed(color=self.bot.color, description=f"> {self.author.mention}: {message}") )