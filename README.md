# Web scraper
Scrape data from sreality.cz, save it in database and show it on react app.

## How does it work
First 500 flats (title and first image) on SReality are scraped using scrapy and saved in Postgres database.  
Flats are then accessible from api made with Starlette framework and Uvicorn server.  
Frontend is made in react with very simple 2 components.