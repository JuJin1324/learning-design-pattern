# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/05
# Copyright (C) 2020, Centum Factorial all rights reserved.
from abc import ABC, abstractmethod
from ftplib import FTP

import requests
from bs4 import BeautifulSoup


class Port(ABC):
    @abstractmethod
    def __str__(self):
        pass


class FTPPort(Port):
    def __str__(self):
        return '21'


class HTTPSecurePort(Port):
    def __str__(self):
        return '443'


class HTTPPort(Port):
    def __str__(self):
        return '80'


class Parser(ABC):
    @abstractmethod
    def __call__(self, content) -> str:
        pass


class HTTPParser(Parser):
    def __call__(self, content) -> str:
        filenames = []
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.findAll('a')
        for link in links:
            filenames.append(link.text)
        return '\n'.join(filenames)


class FTPParser(Parser):
    def __call__(self, content) -> str:
        filenames = content.split(',')
        return '\n'.join(filenames)


class Reader(ABC):
    @abstractmethod
    def __call__(self, protocol, host, port, path) -> str:
        pass


class FTPReader(Reader):
    def __call__(self, protocol, host, port, path) -> str:
        print(f'Connecting to {host}')
        with FTP(host) as ftp:
            ftp.login()
            ftp.cwd(path)
            return ','.join(ftp.nlst())


class HTTPReader(Reader):
    def __call__(self, protocol, host, port, path) -> str:
        url = f'{protocol}://{host}:{port}{path}'
        print(f'Connecting to {url}')
        response = requests.get(url, timeout=2)
        return str(response.content)


# Factory method 들의 모음
class AbstractFactory(ABC):
    def __init__(self, is_secure):
        self.is_secure = is_secure

    @abstractmethod
    def create_protocol(self) -> str:
        pass

    @abstractmethod
    def create_port(self) -> Port:
        pass

    @abstractmethod
    def create_parser(self) -> Parser:
        pass

    @abstractmethod
    def create_reader(self) -> Reader:
        pass


class HTTPFactory(AbstractFactory):
    def create_protocol(self) -> str:
        if self.is_secure:
            return 'https'
        return 'http'

    def create_port(self) -> Port:
        if self.is_secure:
            return HTTPSecurePort()
        return HTTPPort()

    def create_parser(self) -> Parser:
        return HTTPParser()

    def create_reader(self) -> Reader:
        return HTTPReader()


class FTPFactory(AbstractFactory):
    def create_protocol(self) -> str:
        return 'ftp'

    def create_port(self) -> Port:
        return FTPPort()

    def create_parser(self) -> Parser:
        return FTPParser()

    def create_reader(self) -> Reader:
        return FTPReader()


class Connector:
    def __init__(self, factory: AbstractFactory):
        self.protocol = factory.create_protocol()
        self.port = factory.create_port()
        self.parse = factory.create_parser()
        self.reader = factory.create_reader()

    def read(self, host, path):
        return self.reader(self.protocol, host, self.port, path)


if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'
    factory = None

    protocol = int(input(f'Connecting to {domain}. Which Protocol to use? (0-http, 1-ftp)'))
    if protocol == 0:
        is_secure = bool(int(input('Use secure connection? (1-yes, 0-no): ')))
        factory = HTTPFactory(is_secure)
    elif protocol == 1:
        is_secure = False
        factory = FTPFactory(is_secure)
    else:
        print('Sorry, wrong answer')

    connector = Connector(factory)
    try:
        content = connector.read(domain, path)
    except requests.HTTPError as e:
        print('Can not access resource with this method')
    except requests.ConnectionError as e:
        print('Can not access resource with this method')
    else:
        print(connector.parse(content))
