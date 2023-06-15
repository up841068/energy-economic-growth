FROM python:3.10.6-buster

COPY energy_economy energy_economy
# COPY fast_api fast_api
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn energy_economy.api.fast_api:app --host 0.0.0.0 --port $PORT
