from discord import Client
import re
rule = ["shit", "piss", "fuck"]
token = ""
# I got rid of the config file to consolidate it to one file cuz simplicity
# The old bot was picking up words like "briefcase" as profanity because of the regex, just switched it to a list and its checking if it contains.
# Same process, different method. 
class DuckbotBot(Client):
    async def on_ready(self):
        print(f"Connected to Discord as {self.user}.")

    async def on_message(self, message):
         if message.content.lower() in rule:
                await message.add_reaction(u"\U0001f986")
                await message.channel.send("Quack! Watch your language.")
                print("\U0001f986", end="")


bot = DuckbotBot()


if __name__ == '__main__':
    bot.run(token)
