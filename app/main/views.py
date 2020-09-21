from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_sources, get_articles, search_articles
from ..models import Source


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting News Sources
    business_news_sources = get_sources('business')
    technology_news_sources = get_sources('technology')
    entertainment_news_sources = get_sources('entertainment')
    sports_news_sources = get_sources('sports')

    title = 'Home - Welcome Duely Updated News'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search', article_name=search_article))
    else:
        return render_template('index.html', title=title, business=business_news_sources, technology=technology_news_sources, entertainment=entertainment_news_sources, sports=sports_news_sources)


@main.route('/source/<id>')
def articles(id):
    '''
    View news_source page function that returns the news_source page and its articles
    '''
    articles = get_articles(id)
    title = f'NH | {id}'
    

    return render_template('news_article.html', title=title, articles=articles)


@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_articles(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html', articles=searched_articles)
