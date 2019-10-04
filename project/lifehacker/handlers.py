import logging
import aiohttp
from urllib.parse import urljoin
from string import ascii_letters

from aiohttp import web


if __name__ != '__main__':
    logging.basicConfig(filename='/logs/handlers.log', level=logging.DEBUG)

logger = logging.getLogger("handler")

URL = 'https://lifehacker.ru'


def join_text(text: str, emoji: list, period: int) -> str:
    text_pointer = 0
    emoji_pointer = 0
    emoji_len = len(emoji)
    rst_text = ''

    a = ord('a')
    A = ord('A')
    for i, c in enumerate(text):
        if (
                (c not in ascii_letters)
                and (c not in [chr(i) for i in range(a, a+32)])
                and (c not in [chr(i) for i in range(A, A+32)])
        ):
            if (i - text_pointer) == period:
                rst_text += (text[text_pointer:i] + emoji[emoji_pointer] + text[i])
                if emoji_pointer < emoji_len-1:
                    emoji_pointer += 1
                else:
                    emoji_pointer = 0
            else:
                rst_text += text[text_pointer:i+1]
            text_pointer = i+1

    if text_pointer != len(text):
        if (len(text) - text_pointer) == period:
            rst_text += (text[text_pointer:] + emoji[emoji_pointer])
        else:
            rst_text += text[text_pointer:]

    return rst_text


async def handle(request):
    url = urljoin(URL, request.match_info.get('uri', ''))

    emojis = request.app['emojis']

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                text = await resp.text()
            else:
                text = ''

    emojis_text = join_text(text, emojis, 6)

    return web.Response(body=emojis_text, status=resp.status, headers={'Content-Type': 'text/html; charset=utf-8'})
