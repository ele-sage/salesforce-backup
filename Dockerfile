FROM infologistix/docker-selenium-python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env
COPY src/ src/

# Create backup directory
RUN mkdir -p /usr/src/app/backup

# Command runs the backup script using python3 instead of python
CMD ["python3", "src/backup.py"]