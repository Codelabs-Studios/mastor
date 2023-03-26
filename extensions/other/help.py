import discord
import mikocord as mc
from discord.ext import commands
from discord.utils import basic_autocomplete
from discord.commands import slash_command, option

from utils import *


class Help(
    Cog,
    title="Help",
    description="Get help with the bot or the commands.",
    emoji=Emojis["help"],
    category="Other",
    perms=None,
    args=[]
):
    def __init__(self, bot: mc.Bot) -> None:
        self.bot = bot

    @slash_command(name="help", description="Get help with the bot or the commands.")
    async def help(self, ctx: discord.ApplicationContext) -> None:
        emb = discord.Embed(
            title=f"**{Emojis['help']} Help**",
            colour=discord.Colour.blurple(),
        )

        for name, cog in zip(self.bot.cogs.keys(), self.bot.cogs.values()):
            if not cog.get_commands():
                continue

            if cog.perms:
                if ctx.author.guild_permissions >= cog.perms:
                    emb.add_field(
                        name=f"__**{cog.emoji} | {cog.title}**__",
                        value=f"> {cog.description}",
                        inline=True,
                    )
            else:
                emb.add_field(
                    name=f"__**{cog.emoji} | {cog.title}**__",
                    value=f"> {cog.description}",
                    inline=True,
                )

        await ctx.respond(embed=emb)


def setup(bot: mc.Bot) -> None:
    bot.add_cog(Help(bot))
