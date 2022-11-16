import time
from tech_news.database import create_news
from parsel import Selector
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
    selected = Selector(text=html_content)

    news_url_list = [
        url
        for url in selected.css("body .entry-title > a::attr(href)").getall()
    ]
    return news_url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selected = Selector(text=html_content)
    next_page_url = selected.css("body .next::attr(href)").get()
    if not bool(next_page_url):
        return None
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    unique_data_keys = [
        "url",
        "title",
        "timestamp",
        "writer",
        "category",
    ]
    unique_search_params = [
        "head > link[rel=canonical]::attr(href)",
        "body .entry-header-inner > h1::text",
        "body ul > li.meta-date::text",
        "body ul > li.meta-author span.author > a::text",
        "body span.label::text",
    ]
    summary_search = "body .entry-content > p:nth-of-type(1) *::text"
    tags_search = "body .post-tags li > a *::text"
    comments_search = "body #comments > h5::text"
    selected = Selector(text=html_content)
    scrapped_dict = dict()
    for index, key in enumerate(unique_data_keys):
        data = selected.css(unique_search_params[index]).get()
        scrapped_dict[key] = data
        if key == "title":
            scrapped_dict[key] = data.strip()

    scrapped_dict["tags"] = selected.css(tags_search).getall()
    scrapped_dict["comments_count"] = 0
    scrapped_dict["summary"] = "".join(
        selected.css(summary_search).getall()
    ).strip()
    comments = selected.css(comments_search).re(r"/[0-9]/g")
    if bool(comments):
        scrapped_dict["comments_count"] = comments
    return scrapped_dict


# Requisito 5
def get_tech_news(amount):
    scrape_target = "https://blog.betrybe.com/"
    notices_amount_count = 0
    notices = list()
    while notices_amount_count != amount:
        notice = fetch(scrape_target)
        scrape_url_targets = scrape_novidades(notice)
        for url in scrape_url_targets:
            if notices_amount_count != amount:
                html_content = fetch(url)
                notices.append(scrape_noticia(html_content))
                notices_amount_count += 1
        scrape_target = scrape_next_page_link(notice)
    create_news(notices)
    return notices
