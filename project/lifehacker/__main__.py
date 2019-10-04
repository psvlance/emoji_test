from aiohttp import web

from lifehacker.handlers import handle


def load_emojis() -> list:
    rst = []
    with open('emoji.txt') as f:
        rst = [x for x in f]
    return rst
emojis = load_emojis()


app = web.Application()
app.add_routes(
    [
        web.get('/', handle),
        web.get('/{uri:.*?}', handle)
    ]
)
app['emojis'] = emojis


if __name__ == '__main__':
    web.run_app(app, port=80)
