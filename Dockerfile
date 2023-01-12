# pull official base image
FROM python:3.8.3-alpine

EXPOSE 8000

# set work directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .


# install dependencies
RUN apk update \
    && apk add git \
    && pip install --upgrade pip


RUN /bin/sh -c /bin/sh -c && apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m compileall
RUN rm -rf /tmp/*
RUN apk del git
RUN rm -rf /var/cache/apk/*

WORKDIR /usr/src

# develop like environment
CMD [ "python", "manage.py", "runserver" ]