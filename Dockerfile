FROM python:3.10.6-buster

COPY fast_api /fast_api
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn fast_api.api:fast_api --host 0.0.0.0 --port $PORT
