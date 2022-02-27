from flask import render_template
from app import app
from .request import get_sources,article_source

#Views
@app.route('/article/<id>')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources_display = get_sources()
    print(sources_display)
    article = article_source()
    title = 'Home - Welcome to The best News Website '
    
    return render_template('article.html', title = title, sources = sources_display, article = article)

@app.route('/')
def article():

    '''
    View article page function that returns the article details page and its data
    '''
    articles = article_source()
    sources = get_sources()

    return render_template('index.html',articles = articles,sources = sources)