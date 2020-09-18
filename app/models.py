class Source:
    '''
    Sources class to define Movie Objects
    '''

    def __init__(self, id, title, description, url, category,):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.category = category


class Articles:
    '''
    Article class to define Article objects
    '''

    def __init__(self, title, description, url, image, date):
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date
