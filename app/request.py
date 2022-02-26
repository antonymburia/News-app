from app import app
import urllib.request,json
from .models import article, source


Article = article.Article
Source = source.Source

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

  


  

  get_article_details_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)

  with urllib.request.urlopen(get_article_details_url) as url:
    article_details_data = url.read()
    article_details_response = json.loads(article_details_data)

    article_object = None
    if article_details_response:
      id = article_details_response.get('id')
      title = article_details_response.get('title')
      author = article_details_response.get('author')
      time = article_details_response.get('time')
      image = article_details_response.get('image')
      url = article_details_response.get('url')
      content = article_details_response.get('content')

      article_object = Article(id,title,author,time,image,url,content)

  return source_results, article_object

