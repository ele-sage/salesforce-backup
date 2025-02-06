FROM infologistix/docker-selenium-python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env
COPY src/ src/

RUN mkdir -p /usr/src/app/backup

CMD ["python3", "src/backup.py"]