FROM python:3.9-alpine

RUN mkdir /app/
WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./src/ /app/

ENV FLASK_APP=main.py

EXPOSE 5000

CMD flask run -h 0.0.0.0 -p 5000