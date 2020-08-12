# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/12
# Copyright (C) 2020, Centum Factorial all rights reserved.
import datetime
import time
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def notify(self, unix_timestamp: time):
        pass


class Subject:
    def __init__(self):
        self.observers = []
        self.cur_time = None

    def register_observer(self, observer: Observer):
        if observer in self.observers:
            print(f'{observer} already in subscribed observers')
        else:
            self.observers.append(observer)

    def unregister_observer(self, observer: Observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('No such observer in subject')

    def notify_observers(self):
        self.cur_time = time.time()
        for observer in self.observers:
            observer.notify(self.cur_time)


class USATimeObserver(Observer):
    def __init__(self, name: str):
        self.name = name

    def notify(self, unix_timestamp: time):
        usa_time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %I:%M:%S%p')
        print(f'Observer {self.name} says: {usa_time}')


class EUTimeObserver(Observer):
    def __init__(self, name: str):
        self.name = name

    def notify(self, unix_timestamp: time):
        eu_time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %H:%M:%S')
        print(f'Observer {self.name} says: {eu_time}')


if __name__ == '__main__':
    subject = Subject()

    print('Adding usa_time_observer')
    observer1 = USATimeObserver('usa_time_observer')
    subject.register_observer(observer1)
    subject.notify_observers()

    time.sleep(2)
    print('Adding eu_time_observer')
    observer2 = EUTimeObserver('eu_time_observer')
    subject.register_observer(observer2)
    subject.notify_observers()

    time.sleep(2)
    print('Removing usa_time_observer')
    subject.unregister_observer(observer1)
    subject.notify_observers()

