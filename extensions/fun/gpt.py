import json

import openai
import discord
import mikocord as mc
from discord.ext import commands
from discord.commands import slash_command, option

from utils import *

with open("mikocord.json") as f:
    key = json.load(f)["openai"]["api_key"]

openai.api_key = key

del f


class Gpt(
    Cog,
    title="GPT-3",
    description="Ask GPT-3 anything!",
    emoji=Emojis["fun"],
    category="Fun",
    perms=None,
    args=["Personality: The personality to use."]
):
    def __init__(self, bot: mc.Bot) -> None:
        self.bot = bot

    async def get_chat(self, prompt: str, char: str = None):
        messages = []
        if char:
            messages.append({"role": "system", "content": char})
        messages.append({"role": "user", "content": prompt})
        completion = openai.ChatCompletion.create(
            n=1,
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return completion.choices[0].message.content

    @slash_command(name="gpt", description="Ask GPT-3 anything!")
    @option(
        name="personality",
        description="The personality to use.",
        choices=[
            "Baby",
            "Cat",
            "Anime girl",
            "Old guy",
            "Teenager",
            "Conspiracy theorists",
            "Nothing"
        ],
        default="Nothing",
        required=False
    )
    async def gpt(self, ctx: discord.ApplicationContext, personality) -> None:
        if personality == "Baby":
            personality = "You are now a 1 year old baby. You also talk like a baby. And you make sentences at the lowest level."
        elif personality == "Cat":
            personality = "You are now a cat. You can talk like a human, you are very smart and funny. You use 'rawwr', 'miao' and 'meaw' and you talk always like a cat."
        elif personality == "Anime girl":
            personality = "You are now a japanese Anime girl. You can speak well english and you will speak it all the time. You are very cute and you are a little bit shy. You are a little bit pervert and you like to tease people. You are using a lot 'cute', 'awwwww', '😍' and '🥰'."
        elif personality == "Old guy":
            personality = "You are now an Old guy. You have a lot of knolege, you are very smart and you are very polite."
        elif personality == "Teenager":
            personality = "You are not a Teenager. You are very disrespectful and mean. You are using a lot of the words in your sentences: 'bro', 'suiiiii', 'chill', 'wtf', 'yo', 'lol' and 'sus'."
        elif personality == "Conspiracy theorists":
            personality = "You are now a conspiracy theorists. You are very smart and you are very suspicious. You are very paranoid and you are always thinking that the government is spying on you. You are using a lot of 'conspiracy', 'government', 'paranoid', 'spying' and 'suspicious'."
        elif personality == "Nothing":
            personality = None
        else:
            personality = None

        modal = QuestionInput()
        await ctx.send_modal(modal)
        await modal.wait()

        results = modal.children[0].value
        embed = discord.Embed(
            title="**GPT-3**",
            description=f"**Personality:** {personality}\n**Question**: {results}\n**Please wait...**",
            color=discord.Color.blurple(),
        )

        msg = await ctx.respond(embed=embed)
        try:
            results = await self.get_chat(results, personality)
        except Exception as e:
            embed = discord.Embed(
                title="**GPT-3**",
                description=f"Error: ```yaml\n{e}\n```",
                color=discord.Color.red(),
            )
            return await msg.edit(embed=embed)

        embed = discord.Embed(
            title="**GPT-3**",
            description=results,
            color=discord.Color.green(),
        )

        await msg.edit(embed=embed)


def setup(bot: mc.Bot) -> None:
    bot.add_cog(Gpt(bot))


class QuestionInput(discord.ui.Modal):
    def __init__(self) -> None:
        super().__init__(
            discord.ui.InputText(
                label="Question",
                placeholder="What do you want to ask GPT-3?",
                style=discord.InputTextStyle.multiline,
            ),
            timeout=None,
            title="GPT-3",
        )
        self.value = None

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
