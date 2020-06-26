FROM python:3.8.0-alpine

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt
