from contextlib import suppress

import discord
import mikocord as mc
from discord.ext import commands
from discord.utils import basic_autocomplete
from discord.commands import slash_command, option

from utils import *


async def unban_autocomplete(ctx: discord.AutocompleteContext):
    bans = await ctx.interaction.guild.bans().flatten()
    return [str(ban.user) for ban in bans]


class Unban(
    Cog,
    title="Unban",
    description="Unban a user from the server.",
    emoji=Emojis["administration"],
    category="Administration",
    perms=Perm.ban_members(),
    args=[
        "user: The user to unban.",
        "dm: Whether to DM the user about the unban.",
    ]
):
    def __init__(self, bot: mc.Bot):
        self.bot = bot

    @slash_command(name="unban", description="Unban a user from the server.")
    @commands.bot_has_permissions(ban_members=True)
    @discord.default_permissions(ban_members=True)
    @option("user", str, description="The user to unban.", autocomplete=basic_autocomplete(unban_autocomplete))
    @option("dm", bool, description="Whether to DM the user about the unban.", default=True, required=False)
    async def _unban(self, ctx: discord.ApplicationContext, user: str, dm: bool) -> None:
        async for ban in ctx.guild.bans():
            if str(ban.user) == user:
                await ctx.guild.unban(ban.user)
                await mc.Embeds.success(ctx, f"Successfully unbanned {user}!")
                if dm:
                    with suppress(discord.Forbidden, discord.HTTPException):
                        await ban.user.send(f"You have been unbanned from {ctx.guild.name}!")
                return

        await mc.Embeds.error(ctx, f"Couldn't find a user named {user}!")


def setup(bot: mc.Bot) -> None:
    bot.add_cog(Unban(bot))
