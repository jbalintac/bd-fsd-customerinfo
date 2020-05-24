# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.7-alpine

COPY . /app

WORKDIR /app

RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

RUN apk add --no-cache bash

RUN chmod u+x ./init.sh
ENTRYPOINT ["./init.sh"]