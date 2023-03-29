FROM python:3.10-alpine

WORKDIR /app
COPY requirements.txt ./
RUN python -m venv venv && venv/bin/pip install -r requirements.txt
COPY ./ ./

ENTRYPOINT [ "venv/bin/python", "-m", "menubot" ]