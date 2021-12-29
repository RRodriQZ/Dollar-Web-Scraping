from app.constants import NACION_BANK_URL, ROFEX_BANK_URL
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests
import json
import urllib3

urllib3.disable_warnings()


class DollarAdapter:
    @staticmethod
    def get_nacion_bank_data() -> BeautifulSoup:
        response = requests.get(url=NACION_BANK_URL, verify=False, timeout=5)
        if response.status_code != 200:
            return None
        elif response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")


class RofexAdapter:
    @staticmethod
    def get_rofex_bank_data() -> BeautifulSoup:
        response = requests.get(url=ROFEX_BANK_URL, verify=False, timeout=5)
        if response.status_code != 200:
            return None
        elif response.status_code == 200:
            return BeautifulSoup(response.content, "html.parser")


class CmeAdapter:
    @staticmethod
    def get_cme_data(url) -> dict:
        header = {"User-Agent": "XYZ/3.0"}
        request = Request(url=url, headers=header)
        webpage = urlopen(request, timeout=5).read()
        html_content = BeautifulSoup(webpage, "html.parser")
        return json.loads(html_content.text)


class BloombergAdapter:
    @staticmethod
    def get_bloomberg_data(url) -> dict:
        header = {"User-Agent": "Mozilla/5.0"}
        request = Request(url=url, headers=header)
        webpage = urlopen(request, timeout=5).read()
        html_content = BeautifulSoup(webpage, "html.parser")
        return json.loads(html_content.text)
