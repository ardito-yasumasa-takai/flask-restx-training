FROM python:3.9-buster AS builder

WORKDIR /code

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
    && pipenv install --system

FROM python:3.9-slim-buster as dev

ENV PYTHONUNBUFFERED=1

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
