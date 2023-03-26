import discord
from discord.ext import commands
from discord.cog import CogMeta


class CustomCogMeta(CogMeta):
    def __new__(cls, *args, **kwargs) -> CogMeta:
        name, bases, attrs = args

        attrs["emoji"] = kwargs.pop("emoji", None)
        attrs["category"] = kwargs.pop("category", None)
        attrs["perms"] = kwargs.pop("perms", None)
        attrs["args"] = kwargs.pop("args", None)
        attrs["title"] = kwargs.pop("title", None)

        return super().__new__(cls, name, bases, attrs, **kwargs)


class Cog(commands.Cog, metaclass=CustomCogMeta):
    """Base class for all cogs."""
    pass
