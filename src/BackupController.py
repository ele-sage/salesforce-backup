from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from urllib.parse import unquote
import re
import time
import requests
import os

DOWNLOAD_PATH = '/lightning/setup/DataManagementExport/home'
BACKUP_DIR = '/usr/src/app/backups'

class BackupController:
    def __init__(self, org_domain, is_headless=True, implicit_wait=10):
        self.org_domain = org_domain.startswith("http") and org_domain or "https://" + org_domain

        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        if is_headless:
            options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(implicit_wait)
    
    def login(self,user_name,password):
        self.driver.get(self.org_domain)
        self.driver.find_element(By.ID, "username").send_keys(user_name)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "Login").click()
    
    def detect_lightning(self,timeout):
        try:
            WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//div[contains(@class,'iframe-parent')]/iframe")))
            print('Lightning Detected')
            return 1
        except TimeoutException:
            print("Classic Detected")
            return 0
    
    def extract_file_info(self,link):
        if self.is_lightning:
            link=unquote(link)
            extract_link = re.search(r'srcUp\(\'(.*?)\'\)',link)
            link= extract_link.group(1)
        
        extract_file_name = re.search(r'fileName=(.*?)&id',link)
        file_name= extract_file_name.group(1)
        link = f'{self.org_domain}{link}'
        return link,file_name

    def download(self, download_url, file_name, cookies):
        os.makedirs(BACKUP_DIR, exist_ok=True)
        target_path = os.path.join(BACKUP_DIR, file_name)
        
        print(f'Downloading {file_name}')
        with requests.get(download_url, cookies=cookies, stream=True) as r:
            r.raise_for_status()
            with open(target_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    def download_files(self, cookies):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        download_links = soup.find_all('a', text='download')

        for link in download_links:
            download_url, file_name = self.extract_file_info(link["href"])
            self.download(download_url, file_name, cookies)

    def download_backups(self, user_name, password):
        self.login(user_name, password)
        self.driver.get(f'{self.org_domain}{DOWNLOAD_PATH}')
        time.sleep(5)
        timeout=5 
        self.is_lightning=self.detect_lightning(timeout)

        cookies = {'oid': self.driver.get_cookie("oid")["value"], 'sid':self.driver.get_cookie("sid")["value"]}
        print('Downloading Files')
        self.download_files(cookies)
        print('Download Completed')
        self.driver.quit()








