# Install the base requirements for the app.
# This stage is to support development.
FROM python:alpine AS base
WORKDIR /app
COPY Textchain .
RUN pip install -r requirements.txt
RUN ./manage.py makemigrations
RUN ./manage.py migrate
CMD ["python", "./manage.py", "runserver"]
EXPOSE 8000
