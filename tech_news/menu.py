from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
import io
import sys

message_0 = "Digite quantas notícias serão buscadas:"
message_1 = "Digite o título:"
message_2 = "Digite a data no formato aaaa-mm-dd:"
message_3 = "Digite a tag:"
message_4 = "Digite a categoria:"


def populate_db():
    amount = input(message_0)
    print(get_tech_news(int(amount)))


def search_title():
    title = input(message_1)
    print(search_by_title(title))


def search_date():
    date = input(message_2)
    print(search_by_date(date))


def search_tag():
    tag = input(message_3)
    print(search_by_tag(tag))


def search_category():
    category = input(message_4)
    print(search_by_category(category))


def search_5_best_news():
    print(top_5_news())


def search_5_best_category():
    print(top_5_categories())


def exit_program():
    sys.exit(0)


def gui_generate():
    menu_text = io.StringIO()
    print(
        "Selecione uma das opções a seguir:\n",
        "0 - Popular o banco com notícias;\n",
        "1 - Buscar notícias por título;\n",
        "2 - Buscar notícias por data;\n",
        "3 - Buscar notícias por tag;\n",
        "4 - Buscar notícias por categoria;\n",
        "5 - Listar top 5 notícias;\n",
        "6 - Listar top 5 categorias;\n",
        "7 - Sair.",
        sep=" ",
        file=menu_text,
        end="",
    )
    return menu_text


def start_user_interaction(menu_text):
    listening = True
    while listening:
        user_action = input(menu_text.getvalue())
        if not possibilites.__contains__(user_action):
            print("Opção inválida", file=sys.stderr)
            listening = False
        if listening:
            possibilites[user_action]()


possibilites = {
    "0": populate_db,
    "1": search_title,
    "2": search_date,
    "3": search_tag,
    "4": search_category,
    "5": search_5_best_news,
    "6": search_5_best_category,
    "7": exit_program,
}


# Requisito 12
def analyzer_menu():
    try:
        menu_text = gui_generate()
        start_user_interaction(menu_text)
    except SystemExit:
        print("Encerrando script")
    except Exception:
        err = sys.exc_info()[0]
        print(err, file=sys.stderr)
    finally:
        menu_text.close()
