# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/04
# Copyright (C) 2020, Centum Factorial all rights reserved.


class Singleton:
    _instance = None

    def __init__(self):
        if not Singleton._instance:
            print('__init__ method called but nothing is created')
        else:
            print(f'instance already created: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Singleton()
        return cls._instance


class MonostateSingleton:
    __shared_state = {'a': 'b'}

    def __init__(self):
        self.__dict__ = self.__shared_state


if __name__ == '__main__':
    # s = Singleton()
    # s1 = Singleton()
    #
    # print(s._instance)
    # print(s1._instance)
    #
    # print(s.get_instance())
    # print(s1.get_instance())

    m1 = MonostateSingleton()
    m2 = MonostateSingleton()
    print(f'm1: {m1}, m2: {m2}')

    print(f'm1.__dict__: {m1.__dict__}, m2.__dict__: {m2.__dict__}')
    m1.__dict__['a'] = 1
    print(f'm1.__dict__: {m1.__dict__}, m2.__dict__: {m2.__dict__}')
    m1.__dict__['x'] = 2
    print(f'm1.__dict__: {m1.__dict__}, m2.__dict__: {m2.__dict__}')

