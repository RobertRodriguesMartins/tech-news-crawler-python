import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    user_search = {"$regex": rf".*{title}.*", "$options": "i"}
    query = {"title": user_search}
    news_list = search_news(query)
    response = [tuple((news["title"], news["url"])) for news in news_list]
    return response


# Requisito 7
def search_by_date(date):
    try:
        iso_date = datetime.date.fromisoformat(date)
        br_date = iso_date.strftime("%d/%m/%Y")
        query = {"timestamp": br_date}
        news_list = search_news(query)
        response = [tuple((news["title"], news["url"])) for news in news_list]
        return response
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    user_search = {"$regex": rf"{tag}", "$options": "i"}
    query = {"tags": user_search}
    news_list = search_news(query)
    response = [tuple((news["title"], news["url"])) for news in news_list]
    return response


# Requisito 9
def search_by_category(category):
    user_search = {"$regex": rf"{category}", "$options": "i"}
    query = {"category": user_search}
    news_list = search_news(query)
    response = [tuple((news["title"], news["url"])) for news in news_list]
    return response
