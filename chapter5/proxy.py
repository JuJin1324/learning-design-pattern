# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/12
# Copyright (C) 2020, Centum Factorial all rights reserved.
import random
from abc import abstractmethod, ABC


class AbstractSubject(ABC):
    @abstractmethod
    def sort(self, reverse=False):
        pass


class RealSubject(AbstractSubject):
    def __init__(self):
        self.digits = []
        for i in range(10000000):
            self.digits.append(random.random())

    def sort(self, reverse=False):
        self.digits.sort()

        if reverse:
            self.digits.reverse()


class Proxy(AbstractSubject):
    cached_object = None
    reference_count = 0

    def __init__(self):
        if not getattr(self.__class__, 'cached_object', None):
            self.__class__.cached_object = RealSubject()
            print('Created new object')
        else:
            print('Using cached object')
        self.__class__.reference_count += 1

    def sort(self, reverse=False):
        print(f'Called sort method with args: {locals().items()}')
        self.__class__.cached_object.sort(reverse=reverse)

    def __del__(self):
        self.__class__.reference_count -= 1

        if self.__class__.reference_count == 0:
            print('Number of reference_count is 0. Deleting cached object...')
            del self.__class__.cached_object
        print(f'Deleted object. Count of objects: {self.__class__.reference_count}')


if __name__ == '__main__':
    proxy1 = Proxy()
    print(f'proxy1: {proxy1}')

    proxy2 = Proxy()
    print(f'proxy2: {proxy2}')

    proxy3 = Proxy()
    print(f'proxy3: {proxy3}')

    proxy1.sort(reverse=True)
    print(f'proxy1: {proxy1}')

    print('Deleting proxy2')
    del proxy2
    print('The other objects are deleted upon program termination')
