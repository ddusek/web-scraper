from starlette.responses import JSONResponse


async def flats_to_sell(request):
    return JSONResponse({'hello': 'world'})
