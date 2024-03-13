FROM python:3.10.13-alpine3.18

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN pip install Flask

RUN pip install requests

CMD python app.py