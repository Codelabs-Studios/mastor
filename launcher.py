import json
import discord
import mikocord as mc


bot = mc.Bot(intents=discord.Intents.all())

if __name__ == "__main__":
    bot.load_cogs("events")
    bot.load_cogs("extensions", subdirectory=True)

    with open("mikocord.json", "r") as f:
        config = json.load(f)

    if not "openai" in config:
        config["openai"] = {"api_key": ""}

    if "owner_id" not in config:
        config["owner_id"] = 0

    with open("mikocord.json", "w") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    bot.run()
