FROM python:3.8.5-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY ./src /app
COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]