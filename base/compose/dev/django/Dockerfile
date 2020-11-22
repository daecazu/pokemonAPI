FROM python:3.6-alpine
LABEL Daniel Eduardo Canon

ENV PYTHONUNBUFFERED 1

COPY ./base/requirements /requirements
# psycopg2 dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements/dev.txt
# new entrypoint
COPY ./base/compose/dev/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

RUN apk del .tmp-build-deps

RUN mkdir /app
COPY ./base/app /app
WORKDIR /app
ENTRYPOINT ["/entrypoint"]

