# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .