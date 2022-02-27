from flask import render_template
from app import app
from .request import get_sources,article_source

#Views
@app.route('/article/<name>')
def article(name):

    '''
    View root page function that returns the index page and its data
    '''
    sources_display = get_sources(name)
    print(sources_display)
    article = article_source()
    
    
    return render_template('article.html', sources = sources_display, article = article)

@app.route('/')
def index():

    '''
    View article page function that returns the article details page and its data
    '''
    articles = article_source()
    sources = get_sources(id)

    return render_template('index.html',articles = articles,sources = sources)