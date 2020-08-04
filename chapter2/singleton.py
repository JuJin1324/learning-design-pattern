# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/04
# Copyright (C) 2020, Centum Factorial all rights reserved.


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# class Child(Singleton):
#     pass


class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class Child(Borg):
    pass


class AnotherChild(Borg):
    _shared_state = {}