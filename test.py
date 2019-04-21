import unittest
from search_tool import SearchTool
from search_tool.router import Router
from search_tool.search_engine import SearchEngine
from search_tool.search_engine.crawler import Crawler
from search_tool.search_engine.crawler.queue import Queue
from search_tool.search_engine.crawler.downloader import Downloader
from search_tool.search_engine.crawler.parser import Parser
from search_tool.search_engine.crawler.scheduler import Scheduler
from search_tool.search_engine.database import Document, Model
from search_tool.search_engine.indexer import Indexer, Appearance
from search_tool.search_engine.filesystem import Filesystem


class TestSearchTool(unittest.TestCase):
    pass


class TestRouter:
    pass


class TestController:
    pass


class TestSearchEngine(unittest.TestCase):
    def setUp(self):
        self.search_engine = SearchEngine(
            Crawler(
                'http://example.webscraping.com',
                Queue(),
                Downloader(),
                Parser(),
                Scheduler()
            ),
            Indexer(),
            Filesystem(),
        )

    def test_can_build_inverted_index(self):
        self.search_engine.build_inverted_index()

        inverted_index = self.search_engine.filesystem.get('inverted_index.json')

        """
        The following assertions assume an inverted index structure:
         {
             'test': [{document_id: 1, frequency: 1}]
         }
        """
        for term in inverted_index:
            for appearance in inverted_index[term]:
                self.assertEqual(1, appearance['document_id'])


class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = Crawler(
            'http://example.webscraping.com',
            Queue(),
            Downloader(),
            Parser(),
            Scheduler()
        )

    def test_can_crawl(self):
        page = Document()

        self.crawler.crawl(page)

        self.assertEqual('http://example.webscraping.com', page.get(1)['url'])


class TestQueue:
    pass


class TestDownloader:
    def test_it_downloads_a_page(self):
        pass


class TestParser(unittest.TestCase):
    def setUp(self):
        self.pages = [
            # Homepage
            {
                'id': 1,
                'content': '<!--[if HTML5]><![endif]--> <!DOCTYPE html><!--[if lt IE 7]><html class="ie ie6 ie-lte9 ie-lte8 ie-lte7 no-js" lang="en-us"> <![endif]--> <!--[if IE 7]><html class="ie ie7 ie-lte9 ie-lte8 ie-lte7 no-js" lang="en-us"> <![endif]--> <!--[if IE 8]><html class="ie ie8 ie-lte9 ie-lte8 no-js" lang="en-us"> <![endif]--> <!--[if IE 9]><html class="ie9 ie-lte9 no-js" lang="en-us"> <![endif]--> <!--[if (gt IE 9)|!(IE)]><!--><html class="no-js" lang="en-us"> <!--<![endif]--><head><title>Example web scraping website</title> <!--[if !HTML5]><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> <![endif]--><meta charset="utf-8" /><meta name="application-name" content="places" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link rel="shortcut icon" href="/places/static/images/favicon.ico" type="image/x-icon"><link rel="apple-touch-icon" href="/places/static/images/favicon.png"> <script src="/places/static/js/modernizr.custom.js"></script> <script type="text/javascript">var w2p_ajax_confirm_message="Are you sure you want to delete this object?";var w2p_ajax_disable_with_message="Working...";var w2p_ajax_date_format="%Y-%m-%d";var w2p_ajax_datetime_format="%Y-%m-%d %H:%M:%S";var ajax_error_500=\'An error occured, please <a href="/places/default/index">reload</a> the page\'</script> <meta name="keywords" content="web2py, python, web scraping" /><meta name="generator" content="Web2py Web Framework" /><meta name="author" content="Richard Penman" /> <script src="/places/static/js/jquery.js" type="text/javascript"></script><link href="/places/static/css/calendar.css" rel="stylesheet" type="text/css" /><script src="/places/static/js/calendar.js" type="text/javascript"></script><script src="/places/static/js/web2py.js" type="text/javascript"></script><link href="/places/static/css/web2py.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/bootstrap.min.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/style.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/web2py_bootstrap.css" rel="stylesheet" type="text/css" /> <noscript><link href="/places/static/css/web2py_bootstrap_nojs.css" rel="stylesheet" type="text/css" /></noscript></head><body><div class="navbar navbar-inverse"><div class="flash"></div><div class="navbar-inner"><div class="container"> <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse" style="display:none;"> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button><ul id="navbar" class="nav pull-right"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#" rel="nofollow">Log In</a><ul class="dropdown-menu"><li><a href="/places/default/user/register?_next=/places/default/index" rel="nofollow"><i class="icon icon-user glyphicon glyphicon-user"></i> Sign Up</a></li><li class="divider"></li><li><a href="/places/default/user/login?_next=/places/default/index" rel="nofollow"><i class="icon icon-off glyphicon glyphicon-off"></i> Log In</a></li></ul></li></ul><div class="nav"><ul class="nav"><li class="web2py-menu-first"><a href="/places/default/index">Home</a></li><li class="web2py-menu-last"><a href="/places/default/search">Search</a></li></ul></div></div></div></div><div class="container"> <header class="mastheader row" id="header"><div class="span12"><div class="page-header"><h1> Example web scraping website <small></small></h1></div></div> </header><section id="main" class="main row"><div class="span12"><div id="results"><table><tr><td><div><a href="/places/default/view/Afghanistan-1"><img src="/places/static/images/flags/af.png" /> Afghanistan</a></div></td><td><div><a href="/places/default/view/Aland-Islands-2"><img src="/places/static/images/flags/ax.png" /> Aland Islands</a></div></td></tr><tr><td><div><a href="/places/default/view/Albania-3"><img src="/places/static/images/flags/al.png" /> Albania</a></div></td><td><div><a href="/places/default/view/Algeria-4"><img src="/places/static/images/flags/dz.png" /> Algeria</a></div></td></tr><tr><td><div><a href="/places/default/view/American-Samoa-5"><img src="/places/static/images/flags/as.png" /> American Samoa</a></div></td><td><div><a href="/places/default/view/Andorra-6"><img src="/places/static/images/flags/ad.png" /> Andorra</a></div></td></tr><tr><td><div><a href="/places/default/view/Angola-7"><img src="/places/static/images/flags/ao.png" /> Angola</a></div></td><td><div><a href="/places/default/view/Anguilla-8"><img src="/places/static/images/flags/ai.png" /> Anguilla</a></div></td></tr><tr><td><div><a href="/places/default/view/Antarctica-9"><img src="/places/static/images/flags/aq.png" /> Antarctica</a></div></td><td><div><a href="/places/default/view/Antigua-and-Barbuda-10"><img src="/places/static/images/flags/ag.png" /> Antigua and Barbuda</a></div></td></tr></table></div><div id="pagination">&lt; Previous|<a href="/places/default/index/1">Next &gt;</a></div></div> </section><div class="row"> <footer class="footer span12" id="footer"> </footer></div></div> <script src="/places/static/js/bootstrap.min.js"></script> <script src="/places/static/js/web2py_bootstrap.js"></script> <!--[if lt IE 7 ]> <script src="/places/static/js/dd_belatedpng.js"></script> <script>DD_belatedPNG.fix(\'img, .png_bg\');</script> <![endif]--></body></html>'
            },
            # Country page
            {
                'id': 2,
                'content': '<!--[if HTML5]><![endif]--> <!DOCTYPE html><!--[if lt IE 7]><html class="ie ie6 ie-lte9 ie-lte8 ie-lte7 no-js" lang="en-us"> <![endif]--> <!--[if IE 7]><html class="ie ie7 ie-lte9 ie-lte8 ie-lte7 no-js" lang="en-us"> <![endif]--> <!--[if IE 8]><html class="ie ie8 ie-lte9 ie-lte8 no-js" lang="en-us"> <![endif]--> <!--[if IE 9]><html class="ie9 ie-lte9 no-js" lang="en-us"> <![endif]--> <!--[if (gt IE 9)|!(IE)]><!--><html class="no-js" lang="en-us"> <!--<![endif]--><head><title>Example web scraping website</title> <!--[if !HTML5]><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> <![endif]--><meta charset="utf-8" /><meta name="application-name" content="places" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link rel="shortcut icon" href="/places/static/images/favicon.ico" type="image/x-icon"><link rel="apple-touch-icon" href="/places/static/images/favicon.png"> <script src="/places/static/js/modernizr.custom.js"></script> <script type="text/javascript">var w2p_ajax_confirm_message="Are you sure you want to delete this object?";var w2p_ajax_disable_with_message="Working...";var w2p_ajax_date_format="%Y-%m-%d";var w2p_ajax_datetime_format="%Y-%m-%d %H:%M:%S";var ajax_error_500=\'An error occured, please <a href="/places/default/view/Australia-14">reload</a> the page\'</script> <meta name="keywords" content="web2py, python, web scraping" /><meta name="generator" content="Web2py Web Framework" /><meta name="author" content="Richard Penman" /> <script src="/places/static/js/jquery.js" type="text/javascript"></script><link href="/places/static/css/calendar.css" rel="stylesheet" type="text/css" /><script src="/places/static/js/calendar.js" type="text/javascript"></script><script src="/places/static/js/web2py.js" type="text/javascript"></script><link href="/places/static/css/web2py.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/bootstrap.min.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/style.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/web2py_bootstrap.css" rel="stylesheet" type="text/css" /> <noscript><link href="/places/static/css/web2py_bootstrap_nojs.css" rel="stylesheet" type="text/css" /></noscript></head><body><div class="navbar navbar-inverse"><div class="flash"></div><div class="navbar-inner"><div class="container"> <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse" style="display:none;"> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button><ul id="navbar" class="nav pull-right"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#" rel="nofollow">Log In</a><ul class="dropdown-menu"><li><a href="/places/default/user/register?_next=/places/default/view/Australia-14" rel="nofollow"><i class="icon icon-user glyphicon glyphicon-user"></i> Sign Up</a></li><li class="divider"></li><li><a href="/places/default/user/login?_next=/places/default/view/Australia-14" rel="nofollow"><i class="icon icon-off glyphicon glyphicon-off"></i> Log In</a></li></ul></li></ul><div class="nav"><ul class="nav"><li class="web2py-menu-first"><a href="/places/default/index">Home</a></li><li class="web2py-menu-last"><a href="/places/default/search">Search</a></li></ul></div></div></div></div><div class="container"> <header class="mastheader row" id="header"><div class="span12"><div class="page-header"><h1> Example web scraping website <small></small></h1></div></div> </header><section id="main" class="main row"><div class="span12"><form action="#" enctype="multipart/form-data" method="post"><table><tr id="places_national_flag__row"><td class="w2p_fl"><label class="readonly" for="places_national_flag" id="places_national_flag__label">National Flag: </label></td><td class="w2p_fw"><img src="/places/static/images/flags/au.png" /></td><td class="w2p_fc"></td></tr><tr id="places_area__row"><td class="w2p_fl"><label class="readonly" for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">7,686,850 square kilometres</td><td class="w2p_fc"></td></tr><tr id="places_population__row"><td class="w2p_fl"><label class="readonly" for="places_population" id="places_population__label">Population: </label></td><td class="w2p_fw">21,515,754</td><td class="w2p_fc"></td></tr><tr id="places_iso__row"><td class="w2p_fl"><label class="readonly" for="places_iso" id="places_iso__label">Iso: </label></td><td class="w2p_fw">AU</td><td class="w2p_fc"></td></tr><tr id="places_country__row"><td class="w2p_fl"><label class="readonly" for="places_country" id="places_country__label">Country: </label></td><td class="w2p_fw">Australia</td><td class="w2p_fc"></td></tr><tr id="places_capital__row"><td class="w2p_fl"><label class="readonly" for="places_capital" id="places_capital__label">Capital: </label></td><td class="w2p_fw">Canberra</td><td class="w2p_fc"></td></tr><tr id="places_continent__row"><td class="w2p_fl"><label class="readonly" for="places_continent" id="places_continent__label">Continent: </label></td><td class="w2p_fw"><a href="/places/default/continent/OC">OC</a></td><td class="w2p_fc"></td></tr><tr id="places_tld__row"><td class="w2p_fl"><label class="readonly" for="places_tld" id="places_tld__label">Tld: </label></td><td class="w2p_fw">.au</td><td class="w2p_fc"></td></tr><tr id="places_currency_code__row"><td class="w2p_fl"><label class="readonly" for="places_currency_code" id="places_currency_code__label">Currency Code: </label></td><td class="w2p_fw">AUD</td><td class="w2p_fc"></td></tr><tr id="places_currency_name__row"><td class="w2p_fl"><label class="readonly" for="places_currency_name" id="places_currency_name__label">Currency Name: </label></td><td class="w2p_fw">Dollar</td><td class="w2p_fc"></td></tr><tr id="places_phone__row"><td class="w2p_fl"><label class="readonly" for="places_phone" id="places_phone__label">Phone: </label></td><td class="w2p_fw">61</td><td class="w2p_fc"></td></tr><tr id="places_postal_code_format__row"><td class="w2p_fl"><label class="readonly" for="places_postal_code_format" id="places_postal_code_format__label">Postal Code Format: </label></td><td class="w2p_fw">####</td><td class="w2p_fc"></td></tr><tr id="places_postal_code_regex__row"><td class="w2p_fl"><label class="readonly" for="places_postal_code_regex" id="places_postal_code_regex__label">Postal Code Regex: </label></td><td class="w2p_fw">^(d{4})$</td><td class="w2p_fc"></td></tr><tr id="places_languages__row"><td class="w2p_fl"><label class="readonly" for="places_languages" id="places_languages__label">Languages: </label></td><td class="w2p_fw">en-AU</td><td class="w2p_fc"></td></tr><tr id="places_neighbours__row"><td class="w2p_fl"><label class="readonly" for="places_neighbours" id="places_neighbours__label">Neighbours: </label></td><td class="w2p_fw"><div><a href="/places/default/iso//"> </a></div></td><td class="w2p_fc"></td></tr></table><div style="display:none;"><input name="id" type="hidden" value="3937010" /></div></form><a href="/places/default/edit/Australia-14">Edit</a></div> </section><div class="row"> <footer class="footer span12" id="footer"> </footer></div></div> <script src="/places/static/js/bootstrap.min.js"></script> <script src="/places/static/js/web2py_bootstrap.js"></script> <!--[if lt IE 7 ]> <script src="/places/static/js/dd_belatedpng.js"></script> <script>DD_belatedPNG.fix(\'img, .png_bg\');</script> <![endif]--></body></html>'
            }
        ]
        self.parser = Parser()

    def test_it_extracts_visible_text(self):
        for page in self.pages:
            elements = self.parser.extract_visible_text(page)

            for word in elements:
                self.assertTrue(word.replace(' ', '').isalpha())

    # def test_it_gets_excerpt_for_term(self):
    #     term = 'Log In'
    #     document = self.pages[0]['content']
    #
    #     excerpt = self.parser.get_excerpt_for_term(document, term)
    #
    #     self.assertTrue(term in excerpt)


class TestScheduler:
    pass


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def test_where_in(self):
        self.model.entries = [{'id': 1}, {'id': 2}]
        inverted_index_for_term = [
            Appearance(1, 1).__dict__,
            Appearance(2, 1).__dict__,
            Appearance(3, 1).__dict__,
            Appearance(5, 1).__dict__
        ]

        models = self.model.where_in('id', inverted_index_for_term)

        self.assertEqual(2, len(models))


class TestIndexer(unittest.TestCase):
    def setUp(self):
        self.indexer = Indexer()

    def test_adds_new_term(self):
        self.indexer.add_new_term('apple', 1)

        for appearance in self.indexer.index['apple']:
            self.assertEqual(1, appearance['document_id'])
            self.assertEqual(1, appearance['frequency'])

    def test_updates_existing_term_new_document(self):
        self.indexer.index = {
            'apple': [Appearance(1, 1).__dict__]
        }

        self.indexer.update_existing_term('apple', 2)

        self.assertEqual(2, len(self.indexer.index['apple']))

    def test_generates_2grams(self):
        term = 'the crazy brown fox jumps over the lazy dog'

        iterations = self.indexer.generate_ngrams(term, 2)

        self.assertEqual('the crazy', iterations[0])
        self.assertEqual('crazy brown', iterations[1])
        self.assertEqual('brown fox', iterations[2])
        self.assertEqual('fox jumps', iterations[3])
        self.assertEqual('jumps over', iterations[4])

    def test_generates_3grams(self):
        term = 'the crazy brown fox jumps over the lazy dog'

        iterations = self.indexer.generate_ngrams(term, 3)

        self.assertEqual('the crazy brown', iterations[0])
        self.assertEqual('crazy brown fox', iterations[1])
        self.assertEqual('brown fox jumps', iterations[2])
        self.assertEqual('fox jumps over', iterations[3])
        self.assertEqual('jumps over the', iterations[4])

    def test_generates_index(self):
        texts = ['the crazy brown fox jumps over the lazy dog', 'something else that is cool']
        document_id = 1

        self.indexer.generate_index(document_id, texts)

        for appearance in self.indexer.index['the crazy']:
            self.assertEqual(1, appearance['document_id'])
            self.assertEqual(1, appearance['frequency'])


    def test_remove_query_string(self):
        url = 'http://example.webscraping.com/places/default/user/register'

        if '?' in url:
            url = url[:url.find('?')]

        print(url)

if __name__ == '__main__':
    unittest.main()
