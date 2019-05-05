from bs4 import BeautifulSoup, Comment
import re


class Parser:
    def parse(self, seed, html_document):
        urls = []

        soup = BeautifulSoup(html_document, 'html.parser')
        anchors = soup.find_all('a')

        for anchor in anchors:
            raw_url = anchor.attrs['href']

            # Ignore empty links
            if raw_url == '#':
                continue

            # ensure we save an absolute url
            if '://' not in raw_url:
                url = self.prepare_page_url(seed, raw_url)
            else:
                url = raw_url

            # remove query parameters
            if '?' in url:
                url = url[:url.find('?')]

            # Do not crawl external websites
            if seed not in url:
                continue

            urls.append(url)

        return urls

    def prepare_page_url(self, seed, page_url):
        if seed != page_url:
            return seed + page_url

        return page_url

    def get_document_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        return soup.title.string

    def extract_visible_text(self, page):
        soup = BeautifulSoup(page['content'], 'html.parser')

        # Remove script and style elements
        for tag in soup.findAll():
            if tag.name.lower() in ['script', 'style']:
                tag.extract()

        # Remove comment elements
        comments = soup.findAll(text=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()

        elements = soup.findAll(text=True)

        # Filter visible elements
        elements = list(filter(
            lambda element: element.parent.name not in ['style', 'script', '[document]', 'head', 'title', 'link'],
            elements
        ))

        # Filter line breaks
        elements = [x.replace('\n', '') for x in elements]

        # Keep only letters and whitespace
        elements = [self.letters_and_whitespace_only(x) for x in elements]

        # Strip whitespace around stings
        elements = [x.strip() for x in elements]

        # Filter empty elements
        elements = list(filter(lambda text: text not in [None, ' ', ''], elements))

        return elements

    def letters_and_whitespace_only(self, element):
        pattern = re.compile(r'[^a-zA-Z ]+')
        return re.sub(pattern, '', element)
