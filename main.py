import sys
from search_tool import SearchTool
from search_tool.router import Router
from search_tool.search_engine import SearchEngine
from search_tool.search_engine.crawler import Crawler
from search_tool.search_engine.crawler.queue import Queue
from search_tool.search_engine.crawler.downloader import Downloader
from search_tool.search_engine.crawler.parser import Parser
from search_tool.search_engine.crawler.scheduler import Scheduler
from search_tool.search_engine.indexer import Indexer
from search_tool.search_engine.filesystem import Filesystem
from search_tool.search_engine.query_processor import QueryProcessor

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please set a website URL to crawl')
        sys.exit()

    search_tool = SearchTool(
        Router(),
        SearchEngine(
            Crawler(
                sys.argv[1],
                Queue(),
                Downloader(),
                Parser(),
                Scheduler()
            ),
            Indexer(),
            Filesystem(),
            QueryProcessor()
        ),
    )

    search_tool.run()
