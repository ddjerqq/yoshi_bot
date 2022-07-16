import base64
import os

import requests
import asyncio as aio

import snowflake
from headers import random_useragent

MESSAGE_POST = "https://discord.com/api/v9/channels/{channel_id}/messages"


class _Bot:
    def __init__(self, token: str):
        self.__token = token
        self.id = int(base64.b64decode(token.split(".")[0]).decode("utf-8"))
        self.session = requests.session()
        self.session.headers.update({
            "authorization": token,
            "user-agent": random_useragent(),
            "referer": "https://discord.com/channels/@me",
        })


    def _post(self, url: str, data: dict):
        return self.session.post(url, json=data)

    async def send_to_channel(self, channel_id: int, message: str):
        loop = aio.get_running_loop()
        resp = await loop.run_in_executor(
            None,
            self._post,
            MESSAGE_POST.format(channel_id=channel_id),
            {"content": message, "nonce": str(snowflake.Id.new()), "tts": False}
        )
        print(self.session.headers)
        print(resp.request.body)
        print(resp.text)


class BotnetService:
    def __init__(self):
        self.__bots: dict[int, _Bot] = {}

        with open("tokens.txt", "r") as f:
            for token in map(str.strip, f.read().splitlines()):
                bot = _Bot(token)
                self.__bots[bot.id] = bot

    async def spam_channel(self, channel_id: int, message: str):
        group = [bot.send_to_channel(channel_id, message) for bot in self.__bots.values()]
        await aio.gather(*group)

