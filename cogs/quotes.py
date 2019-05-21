import re
from discord.ext import commands
from sql import sql_quotes

tformat = '%d.%m.%Y'


class QuotesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        try:
            quote = sql_quotes.rand_quote(ctx.guild.id)
            time = quote[3].strftime(tformat)
            str_quote = f'Quote #{quote[0]}: {quote[2]} - {quote[1]} ({time})'
            await ctx.send(str_quote)
        except IndexError:
            await ctx.send('No quote found')

    @commands.command()
    async def add_quote(self, ctx):
        msg = ctx.message.content
        author = re.findall(r'(\s[^-"]*$)', msg)
        quote = re.findall(r'"[^"]*"', msg)
        if len(author) == 1 and len(quote) == 1:
            sql_quotes.add_quote(author[0][1:], quote[0], ctx.guild.id)
            await ctx.send('Quote added')
        else:
            await ctx.send('Wrong format')


def setup(bot):
    bot.add_cog(QuotesCog(bot))
