# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/04
# Copyright (C) 2020, Centum Factorial all rights reserved.
import os
import threading

from urllib.parse import urljoin, urlparse
import requests

from bs4 import BeautifulSoup


class Singleton(object):
    queue_to_parse = []
    to_visit = set()
    downloaded = set()
    parsed_root = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


def download_images(thread_name: str):
    singleton = Singleton()
    while singleton.to_visit:
        url = singleton.to_visit.pop()

        print(f'{thread_name} is starting download images from {url}')
        try:
            response = requests.get(url)
        except Exception:
            continue

        bs = BeautifulSoup(response.content, 'html.parser')
        images = bs.findAll('img')
        for image in images:
            src = urljoin(url, image.get('src'))
            basename = os.path.basename(src)

            if src not in singleton.downloaded:
                singleton.downloaded.add(src)
                print(f'Downloading {src}')
                src_response = requests.get(src)
                with open(os.path.join('images', basename), 'wb') as f:
                    f.write(src_response.content)

        print(f'{thread_name} finished downloading images from {url}')


class ImageDownloaderThread(threading.Thread):
    def __init__(self, thread_id: int, name: str, counter: int):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f'Starting thread {self.name}')
        download_images(self.name)
        print(f'Finished thread {self.name}')


# Link Collector Function
def traverse_site(max_links=10):
    link_parser_singleton = Singleton()

    while link_parser_singleton.queue_to_parse:
        if len(link_parser_singleton.to_visit) == max_links:
            return

        url = link_parser_singleton.queue_to_parse.pop()
        try:
            response = requests.get(url)
        except Exception:
            continue

        content_type = response.headers.get('Content-Type')
        if 'text/html' not in content_type:
            continue

        if url not in link_parser_singleton.to_visit:
            link_parser_singleton.to_visit.add(url)
            print(f'Added {url} to to_visit')

        bs = BeautifulSoup(response.content, 'html.parser')
        for link in BeautifulSoup.findAll(bs, 'a'):
            link_url = link.get('href')

            if not link_url:
                continue

            parsed = urlparse(link_url)
            if parsed.netloc and parsed.netloc != link_parser_singleton.parsed_root.netloc:
                continue
            link_url = (parsed.scheme or link_parser_singleton.parsed_root.scheme) + '://' + \
                       (parsed.netloc or link_parser_singleton.parsed_root.netloc) + parsed.path or ''
            if link_url in link_parser_singleton.to_visit:
                continue
            link_parser_singleton.queue_to_parse = [link_url] + link_parser_singleton.queue_to_parse


if __name__ == '__main__':
    root = 'https://python.org/'

    singleton = Singleton()
    singleton.parsed_root = urlparse(root)
    singleton.queue_to_parse = [root]

    traverse_site()

    if not os.path.exists('images'):
        os.makedirs('images')

    thread1 = ImageDownloaderThread(1, "Thread-1", 1)
    thread2 = ImageDownloaderThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()
