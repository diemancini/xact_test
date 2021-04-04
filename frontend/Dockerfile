# Base Image
FROM node:12.4.0

# FRONTEND APPLICATION (QUASAR)
RUN mkdir /frontend
WORKDIR /frontend

ADD . /frontend/

RUN apt-get update; \
    apt-get install -y curl gnupg; \
    curl -sL https://deb.nodesource.com/setup_10.x | bash -; \
    apt-get install -y nodejs; \
    rm -rf /var/lib/apt/lists/*
RUN apt-get install -y npm
RUN npm install -g @quasar/cli
RUN npm install --save axios

ENV PORT=8080

EXPOSE 8080

CMD quasar dev
