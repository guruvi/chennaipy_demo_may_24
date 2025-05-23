import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.request('GET', url) as response:
        return await response.text()


async def main():
    urls = [f"https://www.google.com/search?q={i}" for i in range(25)]

    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

if __name__ == '__main__':
    import time
    start = time.time()
    asyncio.run(main())
    print("Asyncio time:", time.time() - start)
