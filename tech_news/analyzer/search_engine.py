from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    a = list()
    user_search = {"$regex": fr'.*{title}.*', "$options": "i"}
    query = {'title': user_search}
    news_list = search_news(query)
    response = [
        tuple((news['title'], news['url'])) for news in news_list
    ]
    return response


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
