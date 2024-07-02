from discord.ext import commands
import discord

class information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="avatar", aliases=["av", "uav"])
    async def useravatar(self, ctx: commands.Context, member: discord.User=None):
        
        if member is None: 
            member = ctx.author
        
        member = await self.bot.fetch_user(member.id)
        
        embed = discord.Embed(title = f"{member.name}'s avatar", url=member.display_avatar.url)
        embed.set_image(url=member.avatar.url)
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(information(bot))