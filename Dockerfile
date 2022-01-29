FROM python:3.8-alpine

ENV NEW_RELIC_CONFIG_FILE=newrelic.ini

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["newrelic-admin", "run-program", "python", "app.py"]

EXPOSE 5000