import discord
from discord.ext import commands

from client import AdvancedSuperClient


class TextUtilities(commands.Cog):
    def __init__(self, client: AdvancedSuperClient):
        self.client = client

    @commands.command(name="say", description="say for a specific token")
    async def say_as(self, ctx: commands.Context, who: discord.Member, *, message: str):
        ...
        # todo

    @commands.command(name="sayall", description="say with all tokens")
    async def say_as_all(self, ctx: commands.Context, *, message: str):
        await self.client.botnet.spam_channel(ctx.channel.id, message)

    @commands.command(name="summon", description="summon all the bots")
    async def summon_all(self, ctx: commands.Context):
        await self.client.botnet.spam_channel(ctx.channel.id, "I have been summoned!")

    @commands.command(name="spam_message", description="spam all of your friends with a custom message")
    async def friends_spam(self, ctx: commands.Context, *, message):
        await ctx.message.delete()

        for member in ctx.guild.members:
            print("sending message to", member)
            try:
                await member.send(message)
            except Exception as e:
                print(e)
                print("cannot send message to", member)
                continue

    @commands.command("friend_request_spam", description="send friend requests to all the people in the server")
    async def friend_request_spam(self, ctx, server_id=None):
        server = self.client.get_guild(server_id) or ctx.guild  # type: discord.Guild
        for member in server.members:
            user = await self.client.fetch_user(member.id)
            if user:
                try:
                    await user.send_friend_request()
                except discord.Forbidden | discord.HTTPException:
                    continue


def setup(client):
    client.add_cog(TextUtilities(client))
