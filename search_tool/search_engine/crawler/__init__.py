import urllib.robotparser
from random import randint


class Crawler:
    def __init__(self, seed, queue, downloader, parser, scheduler):
        self.seed = seed
        self.queue = queue
        self.downloader = downloader
        self.parser = parser
        self.scheduler = scheduler

    def crawl(self, document):
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(self.seed + "/robots.txt")
        rp.read()

        self.queue.add(self.seed)

        while not self.queue.is_empty():
            current_url = self.queue.next()

            # Check if page with this url has already been crawled
            if self.has_crawled(current_url, document):
                self.queue.remove(current_url)
                continue

            # Consult robots.txt for pages that are allowed to crawl
            if not rp.can_fetch('*', current_url):
                print('Not allowed to crawl ' + current_url)

            # Set delay for crawling
            delay = randint(4, 10)
            print('Waiting for ' + str(delay) + ' seconds...')

            download = self.scheduler.add_interval_job(lambda: self.downloader.download(current_url), delay)

            document.save({
                'title': self.parser.get_document_title(download.content),
                'url': current_url,
                'content': download.content
            })

            urls = self.parser.parse(self.seed, download.content)

            for url in urls:
                self.queue.add(url)

            self.queue.remove(current_url)

            # Limit the number of documents to crawl
            # if len(document.all()) == 1:
            #     self.queue.empty()

    def has_crawled(self, url, document):
        for stored_document in document.all():
            if stored_document['url'] == url:
                print('Page already crawled, skipping ' + url)
                return True

        return False
