import discord
from discord.ext import commands
from discord.cog import CogMeta


class CustomCogMeta(CogMeta):
    def __new__(cls, *args, **kwargs) -> CogMeta:
        name, bases, attrs = args

        attrs["emoji"] = kwargs.pop("emoji", None)
        attrs["category"] = kwargs.pop("category", None)
        attrs["perms"] = kwargs.pop("perms", discord.Permissions())

        return super().__new__(cls, name, bases, attrs, **kwargs)


class Cog(commands.Cog, metaclass=CustomCogMeta):
    pass
