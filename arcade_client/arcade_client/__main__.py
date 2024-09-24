import asyncio
from sys import argv
from os import mkdir
from os.path import exists
from time import time
from statistics import mean

from core.debug import create_log
from core.dot_env import get_env
from core.aio_request import make_async_get_request


async def main(args: list):
    api = get_env('API_REQ')
    times_len = 10_000
    times = []
    for i in range(times_len):
        st = time()
        await make_async_get_request(api, params={
            'username': f'User{i}',
            'password': f'password{i}'
        })
        times.append(time() - st)
    times = sorted(times)
    print(f'Mean: {mean(times)}\nMin: {times[0]}\nMax:{times[times_len - 1]}')


if __name__ == "__main__":
    try:
        create_log(f'Run main: {argv}')
        asyncio.run(main(argv[1:]))
    except Exception as err:
        create_log(err, "crit")
