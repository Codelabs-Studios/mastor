import discord
import mikocord as mc
from discord.ext import commands
from discord.commands import slash_command, option

from utils import *


class Ban(
    Cog,
    name="Ban",
    description="Ban a member from the server.",
    emoji=Emojis["administration"],
    category="Administration",
    perms=ePerm.BAN_MEMBERS
):
    def __init__(self, bot: mc.Bot):
        self.bot = bot

    @slash_command(name="ban", description="Ban a member from the server.")
    @commands.bot_has_permissions(ban_members=True)
    @discord.default_permissions(ban_members=True)
    @option("member", discord.Member, description="The member to ban.")
    @option("reason", str, description="The reason for the ban.", default="No reason provided.", required=False)
    async def _ban(self, ctx: discord.ApplicationContext, member: discord.Member, reason: str) -> None:
        if member == ctx.author:
            return await mc.Embeds.error(ctx, "You can't ban yourself!")

        if member.top_role >= ctx.author.top_role:
            return await mc.Embeds.error(ctx, "You can't ban this member!")

        await member.ban(reason=reason)
        await mc.Embeds.success(ctx, f"Successfully banned {member.mention}!")


def setup(bot: mc.Bot) -> None:
    bot.add_cog(Ban(bot))
