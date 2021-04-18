FROM python:3.8.9-buster

WORKDIR /backend
COPY /backend/requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt
COPY /backend/ /backend/
