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


# Create Worker Threads (Will Die When Main Exit)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do The Next Job In The Queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done() 


# Each Queue Links Is A New Job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check If There Are Items In The Queue, If So Crawl Them
def crawl():
    queue_links = file_to_set(QUEUE_FILE)

    if len(queue_links) > 0:
        print(str(len(queue_links)) + " Links In The Queue")
        create_jobs()


create_workers()
crawl()
