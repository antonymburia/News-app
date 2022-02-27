
from flask import render_template
from . import main
# from main import app
from ..request import get_sources,article_source,get_articles

#Views
@main.route('/')
def index():

    '''
    View article page function that returns the article details page and its data
    '''
    articles = article_source()
    sources = get_sources()

    return render_template('index.html',articles = articles,sources = sources)

@main.route('/source/<id>')
def source():

    '''
    View root page function that returns the index page and its data
    '''
    sources_display = get_sources()
    # print(sources_display)
    
    
    
    return render_template('sources.html', sources = sources_display)

@main.route('/article/<id>')
def articles(id):

    '''
    View root page function that returns the index page and its data
    '''
    sources_display = get_sources()
    print(sources_display)
    articles = get_articles(id)
    
    
    return render_template('article.html', sources = sources_display, articles = articles)
