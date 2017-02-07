from os import environ

from aiohttp import web

REDIRECTER_TARGET = environ.get('REDIRECTER_TARGET', 'http://example.com')
REDIRECTER_HOST = environ.get('REDIRECTER_HOST', '0.0.0.0')
REDIRECTER_PORT = int(environ.get('REDIRECTER_PORT', '8000'))


async def handle(request):
    raise web.HTTPFound(
        '{prefix}{path}'.format(
            prefix=REDIRECTER_TARGET, path=request.rel_url))


app = web.Application()
app.router.add_get(r'/{_:.*}', handle)


if __name__ == '__main__':
    web.run_app(app, host=REDIRECTER_HOST, port=REDIRECTER_PORT)
