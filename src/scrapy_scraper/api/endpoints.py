from starlette.responses import JSONResponse
from scrapy_scraper.queries import retrieve_flats


async def flats_to_sell(request):
    flats = retrieve_flats()
    return JSONResponse(flats)
