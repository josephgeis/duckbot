from discord import Client
import re
token = ""
# I got rid of the config file to consolidate it to one file cuz simplicity
# The old bot was picking up words like "briefcase" as profanity because of the regex, just switched it to a list and its checking if it contains.
# Same process, different method. 

class DuckbotBot(Client):
    async def on_ready(self):
        print(f"Connected to Discord as {self.user}.")


    async def on_message(self, message):
        with open('words.txt') as words:
            words = words.read().split(',')

        lmc = message.content.lower()
        
        for words in filter(lmc.__contains__, words):
            await message.add_reaction(u"\U0001f986")
            await message.channel.send("Quack! Watch your language.")
            raise StopIteration
            print("\U0001f986", end="")



bot = DuckbotBot()


if __name__ == '__main__':
    bot.run(token)
