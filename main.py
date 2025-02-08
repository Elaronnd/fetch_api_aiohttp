from aiohttp import web
from aiohttp_request import fetch_todos_from_api


async def todos_answer(request):
    todos_fetch = await fetch_todos_from_api()
    if todos_fetch[0] is False:
        return web.json_response(todos_fetch[1], status=400)
    return web.json_response(todos_fetch[1])


def main():
    app = web.Application()
    app.router.add_get(path="/todos", handler=todos_answer)

    return app

if __name__ == '__main__':
    app = main()
    web.run_app(app=app, host='0.0.0.0', port=80)