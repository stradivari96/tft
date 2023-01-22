FROM python:3.9-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements-dev.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements-dev.txt

COPY . .
