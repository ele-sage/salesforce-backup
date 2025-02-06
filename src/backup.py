import os
from dotenv import load_dotenv
from BackupController import BackupController

load_dotenv()

SF_USERNAME = os.getenv("SF_USERNAME")
SF_PASSWORD = os.getenv("SF_PASSWORD")
SF_DOMAIN = os.getenv("SF_DOMAIN")

backup = BackupController(SF_DOMAIN, is_headless=False)
backup.download_backups(SF_USERNAME, SF_PASSWORD)
