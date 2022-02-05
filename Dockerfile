FROM python:3.8-alpine

ENV NEW_RELIC_CONFIG_FILE=newrelic.ini PORT=80 NEW_RELIC_LICENSE_KEY=licensekey

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD newrelic-admin run-program gunicorn app:app --bind 0.0.0.0:$PORT