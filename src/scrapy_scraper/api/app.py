import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from scrapy_scraper.api.endpoints import flats_to_sell

# Start api.
app = Starlette(debug=True, routes=[Route('/api/flats-to-sell', flats_to_sell)])

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True)
