FROM python:3.11.1-bullseye

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED=TRUE

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE=TRUE

ENV PYTHONPATH=./

RUN mkdir scrapy_scraper

COPY scripts/scraper-entrypoint-dev.sh /scripts/scraper-entrypoint-dev.sh
COPY src/scrapy_scraper/ /scrapy_scraper/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --requirement /scrapy_scraper/requirements.txt

RUN chmod 774 /scrapy_scraper -R
RUN chmod 774 /scripts/scraper-entrypoint-dev.sh


EXPOSE 8000

ENTRYPOINT [ "/scripts/scraper-entrypoint-dev.sh" ]
