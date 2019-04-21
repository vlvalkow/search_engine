import requests


class Downloader:
    def download(self, page_url):
        print('Crawling: ' + page_url)

        page = requests.get(page_url)

        return page
