import unittest
from app.models import Source,Articles


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(
            'BBC', 'BBC News', 'worldwide News Coverage', 'bbc.com', 'environment')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id, 'BBC')
        self.assertEquals(self.new_source.title, 'BBC News')
        self.assertEquals(self.new_source.description,
                          'worldwide News Coverage')
        self.assertEquals(self.new_source.url, 'bbc.com')
        self.assertEquals(self.new_source.category, 'environment')


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('BBC', 'Earthquake "hack" reveals scale of ocean warming', 'A look at Global warming effects', 'BBC.com',
                                    'https://ichef.bbci.co.uk/news/660/cpsprodpb/6613/production/_114413162_gettyimages-621685344.jpg', '2020-09-11T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id, 'BBC')
        self.assertEquals(self.new_article.title,
                          'Earthquake "hack" reveals scale of ocean warming')
        self.assertEquals(self.new_article.description,
                          'A look at Global warming effects')
        self.assertEquals(self.new_article.url, 'bbc.com')
        self.assertEquals(self.new_article.image,
                          'https://ichef.bbci.co.uk/news/660/cpsprodpb/6613/production/_114413162_gettyimages-621685344.jpg')
        self.assertEquals(self.new_article.date, '2020-09-11T07:57:16Z')
