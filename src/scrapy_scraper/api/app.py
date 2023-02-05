import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from scrapy_scraper.api.endpoints import flats_to_sell

middlewares = [
    Middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_headers=['Content-Type', 'Authorization'],
        allow_methods=['GET', 'OPTIONS'],
    ),
]

# Start api.
app = Starlette(debug=True,
                routes=[Route('/api/flats-to-sell', flats_to_sell)],
                middleware=middlewares)

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True)
