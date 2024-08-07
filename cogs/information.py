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
        
        embed = discord.Embed(title = f"{member.name}'s avatar", url = member.display_avatar.url, color = self.bot.color)
        embed.set_image(url=member.avatar.url)
        await ctx.reply(embed=embed)
        
    @commands.command(name="serveravatar", aliases=["sav"])
    async def serveravatar(self, ctx: commands.Context, member: discord.Member=None):
        
        if member is None: 
            member = ctx.author
            
        if member.guild_avatar is None: 
            return await ctx.warning(f'**{member}** doesnt have a server avatar set.')
        
        embed = discord.Embed(title = f"{member.name}'s server avatar", url=member.display_avatar.url, color = self.bot.color)
        embed.set_image(url=member.guild_avatar.url)
        await ctx.reply(embed=embed)
        
    @commands.command(name='serverbanner', aliases=["sb", "sbanner", "gbanner"])
    async def serverbanner(self, ctx: commands.Context):
        
        if ctx.guild.banner is None:
            return await ctx.warning(f"This server **doesn't** have a server banner.")
        
        embed = discord.Embed(title = f"{ctx.guild.name}'s banner", url=ctx.guild.banner.url, color = self.bot.color)
        embed.set_image(url=ctx.guild.banner.url)
        await ctx.reply(embed=embed)
    
    @commands.command(name='servericon', aliases=["sicon", "gicon"])
    async def servericon(self, ctx: commands.Context):
        
        if ctx.guild.icon is None:
            return await ctx.warning(f"This server **doesn't** have a server icon.")
        
        embed = discord.Embed(title = f"{ctx.guild.name}'s icon", url=ctx.guild.icon.url, color = self.bot.color)
        embed.set_image(url=ctx.guild.banner.url)
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(information(bot))