from discord import Client
import config
import re

rule = re.compile(config.RULE)


class DuckbotBot(Client):
    async def on_ready(self):
        print(f"Connected to Discord as {self.user}.")

    async def on_message(self, message):
        if rule.search(message.content):
            await message.add_reaction(u"\U0001f986")
            await message.channel.send("Quack! Watch your language.")
            print("\U0001f986", end="")


bot = DuckbotBot()


if __name__ == '__main__':
    bot.run(config.TOKEN)
