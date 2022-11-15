import time
from requests import get
from requests.exceptions import ConnectionError, RetryError, Timeout


# Requisito 1
def fetch(url):
    try:
        custom_headers = {"user-agent": "Fake user-agent"}
        page = get(url, timeout=3, headers=custom_headers)
        time.sleep(1)
        if page.status_code == 200:
            return page.text
        return None
    except (ConnectionError, RetryError, Timeout):
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
