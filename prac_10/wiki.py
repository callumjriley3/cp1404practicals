"""
CP1404 Practical 10
Program that uses Wikipedia API
"""
import wikipedia

search_phrase = input("Search: ").title()
while search_phrase != "":
    try:
        article_page = wikipedia.page(search_phrase, auto_suggest=False)
        print(article_page.title)
        print(wikipedia.summary(article_page))
        print(article_page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = input("Search: ").title()
