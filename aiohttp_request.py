from aiohttp import ClientSession


TODOS_API_URL = 'https://jsonplaceholder.typicode.com/todos'

async def fetch_todos_from_api():
    async with ClientSession() as session:
        async with session.get(TODOS_API_URL) as response:
            if response.status != 200:
                return [False, {}]
            return [True, await response.json()]
