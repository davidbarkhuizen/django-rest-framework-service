FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

WORKDIR /api

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY codebase/services/btc_price/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt