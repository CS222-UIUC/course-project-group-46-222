# Dockerfile, Image, Container
FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
ADD src .

ENV FLASK_APP=app.py


ENTRYPOINT [ "flask","run","--host=0.0.0.0" ]