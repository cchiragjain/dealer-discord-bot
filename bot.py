from NHentai import NHentai
from discord.ext import commands

DISCORD_TOKEN = 'NzgwMDk4Njk4MzMxMTYwNTc2.X7qJhw.pOMSyMr8CySfkikBeCc4FWPrSMc'

bot = commands.Bot(command_prefix='!')
nhentai = NHentai()


def get_random_number():
    if __name__ == '__main__':
        random_doujin: dict = nhentai.get_random()
        return random_doujin["id"]


@bot.command(name='random', help='Gives link to a random hentai')
async def random_number(ctx):
    response = get_random_number()
    link = f"https://nhentai.net/g/{response}"
    await ctx.send(link)


@bot.command(
    name='search',
    help='returns the first 5 hentai that matches the search query')
async def search(ctx, search_query):
    search_obj: dict = nhentai.search(
        query=search_query, sort='popular', page=1)
    doujins = search_obj["doujins"]
    index = 0
    for doujin in doujins:
      if(index<5):
        id = doujin["id"]
        await ctx.send(f"https://nhentai.net/g/{id}")
        index = index + 1
bot.run(DISCORD_TOKEN)
