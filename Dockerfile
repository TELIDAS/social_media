FROM python:3.9-alpine as backend

WORKDIR /app

COPY requirements.txt requirements.txt


RUN apk --no-cache add \
        jpeg \
        libffi \
        postgresql-libs \
        openssl \
        postgresql-client \
        && \
    apk --no-cache add \
        --virtual .requirements-build-deps \
        gcc \
        jpeg-dev \
        libffi-dev \
        musl-dev \
        postgresql-dev \
        zlib-dev \
        linux-headers \
        && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .requirements-build-deps

COPY . .

RUN python3 ./manage.py collectstatic --noinput

CMD python3 ./manage.py migrate && python3 ./manage.py runserver 0.0.0.0:8000