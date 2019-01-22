from html.parser import HTMLParser
from urllib import parse


class LinksFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attr, value) in attrs:
                if attr == 'href':
                    # If Relative Link It Will Join It With The Base url
                    # If Full Qualified Url It Will Reformat It Only
                    # Very Ridicules Right
                    url = parse.urljoin(self.base_url, value)

    def error(self, message):
        pass
