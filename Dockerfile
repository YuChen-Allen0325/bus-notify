FROM python:3.9.19-slim-bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata procps && \
    apt-get clean && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app

ENTRYPOINT ["python3"]
CMD ["main.py"]
