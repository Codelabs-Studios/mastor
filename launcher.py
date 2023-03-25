import discord
import mikocord as mc


bot = mc.Bot(intents=discord.Intents.all())

if __name__ == "__main__":
    bot.load_cogs("events")
    bot.load_cogs("extensions", subdirectory=True)
    
    bot.run()