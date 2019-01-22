import threading
from queue import Queue

from domain import *
from general import *
from spider import Spider

PROJECT_NAME = 'elzero'
HOME_PAGE = 'https://elzero.org/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)
