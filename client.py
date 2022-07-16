import os

import discord
from discord.ext import commands

from botnet_service import BotnetService


class AdvancedSuperClient(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            case_insensitive=True,
            command_prefix="?",
            intents=discord.Intents.all(),
            self_bot=True,
            **kwargs,
        )
        self.__load_cogs()

        self.botnet = BotnetService()

    def __load_cogs(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename.removesuffix('.py')}")

    def run(self):
        super().run(os.getenv("TOKEN"), bot=False)

    async def on_ready(self):
        print(f"Logged in as {self.user}")
