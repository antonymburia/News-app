class Source:

    '''
    source class to define Objects
    '''

    def __init__(self,id,name,description,url):
        self.id= id
        self.name = name
        self.description = description
        self.url = url

class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,title,author,time,image,url,content,source):
        self.id =id
        self.title = title
        self.author = author
        self.time = time
        self.image = image
        self.url = url
        self.content = content
        self.source = source

class Articles:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title,content):
        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
        self.content = content
       
