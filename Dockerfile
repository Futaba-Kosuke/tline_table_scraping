FROM python:3.9.6

WORKDIR /app
COPY . /app

RUN apt update -y
RUN apt install -y tzdata
RUN pip3 install -r requirements.txt --no-cache-dir

ENV TZ Asia/Tokyo

ENV PORT=8000

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 main:app