# syntax=docker/dockerfile:1.4

FROM scratch AS code
COPY . /code

# ---

FROM python:3.11-slim

ARG APPPATH=/usr/src/app

RUN --mount=type=bind,from=code,source=/code,target=/code,rw \
    pip install -r /code/requirements.txt

RUN useradd app && \
    mkdir -p $APPPATH && \
    chown app -R $APPPATH

USER app
WORKDIR $APPPATH
COPY --from=code --chown=app:app /code .
ENTRYPOINT ["python3", "bot.py"]
