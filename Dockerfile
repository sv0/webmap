FROM python:slim-bullseye as base

FROM base as builder
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential
COPY requirements.txt /tmp/
RUN pip3 install \
    --disable-pip-version-check \
    --compile \
    --no-cache-dir \
    -r /tmp/requirements.txt && \
    rm -fr /root/.cache
RUN apt-get remove -y --purge build-essential \
    && apt-get -y autoremove

FROM base
COPY --from=builder /usr/local /usr/local
COPY --from=builder /usr/lib /usr/lib
WORKDIR /app
COPY . /app

ENTRYPOINT ["/usr/local/bin/python3", "manage.py", "runserver", "0.0.0.0:8000"]
