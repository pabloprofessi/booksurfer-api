FROM python:2-alpine

RUN apk update && \
    apk add bash     ## Install bash for CI scripts.

RUN apk add python-dev gcc openssl libc-dev iputils py-mysqldb mysql-dev

RUN mkdir /app

RUN pip install gunicorn mysql-python pytest pytest-cov mock

RUN pip install -U flask-cors

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY . /app

RUN pip install .

ENV APP_ENV=dev

RUN sleep 5

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "runner"]
