FROM python:3.12.2-alpine3.19


COPY requirements.txt /app/

RUN pip3 install -r /app/requirements.txt

COPY lambda_function.py /app/