# Install the base requirements for the app.
# This stage is to support development.
FROM python:alpine AS base
WORKDIR /app
COPY Textchain .
RUN apk add build-base linux-headers #musl-dev # install gcc and libc so pip can build uwsgi
RUN pip install -r requirements.txt
RUN pip install uwsgi
RUN ./manage.py makemigrations
RUN ./manage.py migrate
CMD ["uwsgi", "docker-uwsgi.ini"]
EXPOSE 8000
