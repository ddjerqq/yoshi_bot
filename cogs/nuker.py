import discord
from discord.ext import commands


class NukerUtilities(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="bal_all", desctription="ban all users inside a server")
    async def ban_all(self, ctx: commands.Context, server_id=None):
        server = await self.client.fetch_guild(server_id) or ctx.guild
        for member in server.guild.members:
            await member.ban()

    @commands.command(name="kick_all", desctription="kick all users inside a server")
    async def kick_all(self, ctx: commands.Context, server_id=None):
        server = self.client.fetch_guild(server_id) or ctx.guild
        for member in server.members:
            await member.kick()


def setup(client):
    client.add_cog(NukerUtilities(client))
