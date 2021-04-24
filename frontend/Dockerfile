FROM node:14.16.1

WORKDIR /frontend

COPY /frontend/package.json /frontend/package.json
COPY /frontend/package-lock.json /frontend/package-lock.json
RUN npm install
COPY /frontend/ /frontend/
