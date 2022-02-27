from flask import render_template
from app import app
from .request import get_sources,article_source

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources_display = get_sources()
    print(sources_display)
    article = article_source()
    title = 'Home - Welcome to The best News Website '
    
    return render_template('index.html', title = title, sources = sources_display, article = article)

