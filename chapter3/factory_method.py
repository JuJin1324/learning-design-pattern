# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/05
# Copyright (C) 2020, Centum Factorial all rights reserved.
from abc import ABC, abstractmethod

import requests
from ftplib import FTP

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


class Connector(ABC):
    def __init__(self, is_secure):
        self.is_secure = is_secure
        self.port = self.port_factory_method()
        self.protocol = self.protocol_factory_method()

    # Factory method: Product -> protocol
    @abstractmethod
    def protocol_factory_method(self) -> Port:
        pass

    # Factory method: Product -> port
    @abstractmethod
    def port_factory_method(self) -> str:
        pass

    @abstractmethod
    def read(self, host, path) -> str:
        pass

    @abstractmethod
    def parse(self, content: str) -> str:
        pass


class HTTPConnector(Connector):
    def protocol_factory_method(self):
        if self.is_secure:
            return 'https'
        return 'http'

    def port_factory_method(self) -> Port:
        if self.is_secure:
            return HTTPSecurePort()
        return HTTPPort()

    def read(self, host, path) -> str:
        url = f'{self.protocol}://{host}:{self.port}{path}'
        print(f'Connecting to {url}')
        response = requests.get(url, timeout=2)
        return str(response.content)

    def parse(self, content: str) -> str:
        filenames = []
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.findAll('a')
        for link in links:
            filenames.append(link['href'])
        return '\n'.join(filenames)


class FTPConnector(Connector):
    def protocol_factory_method(self):
        return 'ftp'

    def port_factory_method(self) -> Port:
        return FTPPort()

    def parse(self, content: str) -> str:
        filenames = content.split('\n')
        return '\n'.join(filenames)

    def read(self, host, path) -> str:
        print(f'Connecting to {host}')
        with FTP(host) as ftp:
            ftp.login()
            ftp.cwd(path)
            return '\n'.join(ftp.nlst())


if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'

    protocol = input(f'Connecting to {domain}. Which Protocol to use? (0-http, 1-ftp)')
    if protocol == '0':
        is_secure = bool(int(input('Use secure connection? (1-yes, 0-no): ')))
        connector = HTTPConnector(is_secure)
    else:
        is_secure = False
        connector = FTPConnector(is_secure)

    try:
        content = connector.read(domain, path)
    except requests.HTTPError as e:
        print('Can not access resource with this method')
    except requests.ConnectionError as e:
        print('Can not access resource with this method')
    else:
        print(connector.parse(content))
