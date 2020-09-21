import urllib.request,json
from .models import Source, Articles
from datetime import datetime


# Getting api key
api_key = None

# Getting the movie base url
base_url = None

# Getting the news articles url
news_articles_url = None


def configure_request(app):
    global api_key, base_url, base_url, news_articles_url

    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    news_articles_url = app.config['NEWS_ARTICLES_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    '''
    Function  that processes the news source result and transform them to a list of Objects

    Args:
        news_source_list: A list of dictionaries that contain news source details

    Returns :
        news_source_results: A list of news source objects
    '''

    sources_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        title = source_item.get('original_title')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        sources_object = Source(id, title, description, url, category)
        sources_results.append(sources_object)

    return sources_results


def get_articles(id):
    '''
    Function that gets the json response to our articles request
    '''

    get_articles_url = news_articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []

    for article_item in articles_list:
        title = article_item.get('title')
        image = article_item.get('urlToImage')
        description = article_item.get('description')
        url = article_item.get('url')
        date = article_item.get('publishedAt')

    if image:
        articles_object = Articles(id, title, image, description, url, date)
        articles_results.append(articles_object)

    return articles_results


def search_articles(article_name):
    search_articles_url = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'.format(
        api_key, article_name)
    with urllib.request.urlopen(search_articles_url) as url:
        search_articles_data = url.read()
        search_articles_response = json.loads(search_articles_data)

        search_articles_results = None

        if search_articles_response['articles']:
            search_articles_list = search_articles_response['articles']
            search_articles_results = process_articles(search_articles_list)

    return search_articles_results
