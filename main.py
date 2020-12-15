import discord
from discord import Client
import config
import re

rule = re.compile(config.RULE)


class DuckbotBot(Client):
    async def on_ready(self):
        print(f"Connected to Discord as {self.user}.")

    async def on_message(self, message):
        dm = isinstance(message.channel, discord.DMChannel)
        if not dm and message.guild.unavailable:
            return
        if rule.search(message.content):
            # Are we allowed to react?
            # For some reason adding reactions randomly fails, so i'm wrapping it in a try/catch block
            try:
                await message.add_reaction(u"\U0001f986")
            except Exception:
                pass
            
            # Are we allowed to send messages?
            if dm or message.channel.permissions_for(message.guild.me).send_messages:
                await message.channel.send("Quack! Watch your language.")
            print("\U0001f986", end="")


bot = DuckbotBot()


if __name__ == '__main__':
    bot.run(config.TOKEN)
