FROM python:3.7-alpine

COPY project/requirements.txt /requirements.txt
COPY compose/entrypoint /entrypoint
COPY compose/start /start

RUN sed -i 's/\r//' /entrypoint && chmod +x /entrypoint \
    && sed -i 's/\r//' /start && chmod +x /start \
    && pip install -r /requirements.txt

COPY project /project
WORKDIR /project
ENTRYPOINT ["/entrypoint"]
