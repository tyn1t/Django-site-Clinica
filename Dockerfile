ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

RUN python -m venv .venv

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh","-c","python manage.py migrate && python  manage.py  runserver 0.0.0.0:8000"]