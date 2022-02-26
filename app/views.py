from flask import render_template
from app import app
from .request import article_source, get_headlines, get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources_display = get_sources()
    print(sources_display)
    articles = article_source(id)
    title = 'Home - Welcome to The best News Website '
    headlines = get_headlines()
    return render_template('index.html', title = title, sources = sources_display, articles = articles,headlines= headlines)

@app.route('/article/<article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)