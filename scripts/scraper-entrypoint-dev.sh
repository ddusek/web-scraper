#!/usr/bin/env bash

echo "Scrape flats"
python /scrapy_scraper/init_db.py

echo "Running webserver"
python /scrapy_scraper/api/app.py