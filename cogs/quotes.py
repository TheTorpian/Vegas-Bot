import re
import random
from discord.ext import commands
from sql import sql_quotes

tformat = '%d.%m.%Y'


class QuotesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # gets a random or selected quote from server
    async def quote(self, ctx, quote_nr=0):
        try:
            quotes = sql_quotes.get_quote(ctx.guild.id)
            if quote_nr == 0:  # if arg is 0 or is command is called without args
                quote_nr = random.randint(0, len(quotes) - 1)
            else:
                quote_nr -= 1
            quote = quotes[quote_nr]
            time = quote[3].strftime(tformat)
            str_quote = f'Quote #{quote_nr+1}: {quote[2]} - {quote[1]} ({time})'
            await ctx.send(str_quote)
        except IndexError:
            await ctx.send('No quote found')

    @commands.command()  # adds quote for server
    async def add_quote(self, ctx):
        author = re.search(r'(\s[^-"]*$)', ctx.message.content)
        quote = re.search(r'"[^"]*"', ctx.message.content)
        if author and quote:
            sql_quotes.add_quote(author.group(0)[1:], quote.group(0), ctx.guild.id)
            await ctx.send('Quote added')
        else:
            await ctx.send('Wrong format, do `"quote" - user`')

    @commands.command()  # gets all the quotes from the server
    async def quote_list(self, ctx):
        try:
            quotes = sql_quotes.get_quote(ctx.guild.id)
            str_quotes = ''
            for idx, quote in enumerate(quotes, start=1):
                time = quote[3].strftime(tformat)
                str_quote = f'Quote #{idx}: {quote[2]} - {quote[1]} ({time})'
                str_quotes += f'{str_quote}\n'
            await ctx.send(str_quotes)
        except IndexError:
            await ctx.send('No quotes found')


def setup(bot):
    bot.add_cog(QuotesCog(bot))
