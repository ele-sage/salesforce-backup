import os
from dotenv import load_dotenv
from BackupController import BackupController

load_dotenv()

SF_USERNAME = os.getenv("SF_USERNAME")
SF_PASSWORD = os.getenv("SF_PASSWORD")
SF_DOMAIN = os.getenv("SF_DOMAIN")

if not SF_USERNAME or not SF_PASSWORD or not SF_DOMAIN:
    raise Exception("Please set the environment variables")

backup = BackupController(SF_DOMAIN)
backup.download_backups(SF_USERNAME, SF_PASSWORD)
