from search_tool import SearchTool
from search_tool.router import Router
from search_tool.search_engine import SearchEngine
from search_tool.search_engine.crawler import Crawler
from search_tool.search_engine.crawler.queue import Queue
from search_tool.search_engine.crawler.downloader import Downloader
from search_tool.search_engine.crawler.parser import Parser
from search_tool.search_engine.crawler.scheduler import Scheduler
from search_tool.search_engine.database import Database
from search_tool.search_engine.indexer import Indexer
from search_tool.search_engine.filesystem import Filesystem

if __name__ == '__main__':
    search_tool = SearchTool(
        Router(),
        SearchEngine(
            Crawler(
                'http://example.webscraping.com',
                Queue(),
                Downloader(),
                Parser(),
                Scheduler()
            ),
            Database(),
            Indexer(),
            Filesystem()
        ),
    )

    search_tool.run()
