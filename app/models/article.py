class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,title,author,time,image,url,content):
        self.id =id
        self.title = title
        self.author = author
        self.time = time
        self.image = image
        self.url = url
        self.content = content