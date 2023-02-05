FROM node:18.14-bullseye

RUN mkdir frontend

COPY src/frontend/src /frontend/src
COPY src/frontend/public /frontend/public
COPY src/frontend/package.json /frontend/package.json
COPY src/frontend/package-lock.json /frontend/package-lock.json
COPY scripts/frontend-entrypoint-dev.sh /scripts/frontend-entrypoint-dev.sh

RUN chmod 774 /scripts/frontend-entrypoint-dev.sh

WORKDIR /frontend/
RUN npm i

EXPOSE 8080

ENTRYPOINT [ "/scripts/frontend-entrypoint-dev.sh" ]