from tech_news.database import db


# Requisito 10
def top_5_news():
    news_cursor = db.news.aggregate(
        [{"$sort": {"comments_count": -1, "title": 1}}, {"$limit": 5}]
    )
    return [tuple((news["title"], news["url"])) for news in news_cursor]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
