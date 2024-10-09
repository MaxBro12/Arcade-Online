#import aiohttp


#async def make_async_get_request(
#    ulr: str,
#    headers: dict | None = None,
#    params: dict | None = None
#) -> dict | str:
#    async with aiohttp.ClientSession() as session:
#        async with session.get(
#            ulr,
#            headers=headers,
#            data=params,
#        ) as response:
#            return await response.text()
