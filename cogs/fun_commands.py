import random
from discord.ext import commands


class FunCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="ping")
    async def ping(self, ctx):
        """
        ping command, used to get the latency of the bot
        example:
            ?ping
        """
        await ctx.send(f"{round(self.client.latency * 1000)}ms")

    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, question):
        """
        8ball command, used to get a random answer from the bot
        example:
            ?8ball <question>
        """
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - Definitely.",
            "You may rely on it"
            "As I see it, yes.",
            "Most Likely.",
            "Yes.",
            "Ask again later.",
            "Better not tell you.",
            "Cannot predict now",
            "Error 404, answer not found, please ask again.",
            "Don't count on it.",
            "No.",
            "My sources say no.",
            "Quite unlikely"
        ]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


def setup(client):
    client.add_cog(FunCommands(client))
