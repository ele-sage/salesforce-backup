import os
from dotenv import load_dotenv
from BackupController import BackupController

load_dotenv()

SF_USERNAME = os.getenv("SF_USERNAME")
SF_PASSWORD = os.getenv("SF_PASSWORD")
SF_SECURITY_TOKEN = os.getenv("SF_SECURITY_TOKEN")
SF_DOMAIN = os.getenv("SF_DOMAIN")

backup = BackupController(SF_DOMAIN)
backup.download_backups(SF_USERNAME, SF_PASSWORD)