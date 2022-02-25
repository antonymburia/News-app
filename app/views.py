from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources_display = get_sources()
    print(sources_display)
    title = 'Home - Welcome to The best News Website '
    return render_template('index.html', title = title, sources = sources_display)

@app.route('/article/<article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    return render_template('article.html',id = article_id)