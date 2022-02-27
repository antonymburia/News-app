from app import app
import urllib.request,json
from .models import  models



Source = models.Source
Article = models.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

#getting base URL
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources():
  '''
    Function that gets the json response to our url request
  '''
  get_sources_url = base_url.format(api_key)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    source_results = None

    if get_sources_response['sources']:
      source_results_list = get_sources_response['sources']
      source_results = process_results(source_results_list)

  return source_results

def process_results(source_list):
  '''
  Function  that processes the article result and transform them to a list of Objects

  Args:
      article_list: A list of dictionaries that contain article details

  Returns :
      article_results: A list of article objects
  '''

  source_results = []
  for source_item in source_list:
    id =source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    

    if id:
      source_object = Source(id,name,description,url)
      source_results.append(source_object)

  return source_results

def article_source():
    '''
    function that gets the response to the category json
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        get_articles_results = None

        if get_articles_response['articles']:
            get_articles_list = get_articles_response['articles']
            get_articles_results = process_articles_results(get_articles_list)

    return get_articles_results


def get_articles(id):
    article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id, api_key)
    # print(article_url)
    with urllib.request.urlopen(article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        article_results = None

        if article_response['articles']:
            article_list = article_response['articles']
            article_results = process_articles_results(article_list)

            


    return article_results
 

def process_articles_results(articles):
    '''
    function that processes the json files of articles from the api key
    '''
    article_results = []
    for article in articles:
        author = article.get('author')
        description = article.get('description')
        date = article.get('publishedAt')
        url = article.get('url')
        image = article.get('urlToImage')
        title = article.get ('title')
        content= article.get('content')
        source = article.get('source')
        
        if url:
            article_objects = Article(author,description,date,image,url,title,content,source)
            article_results.append(article_objects)

    return article_results

  



