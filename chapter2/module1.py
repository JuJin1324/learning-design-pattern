# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/04
# Copyright (C) 2020, Centum Factorial all rights reserved.

from chapter2 import singleton as sgt

# singleton = sgt.Singleton()
# another_singleton = sgt.Singleton()
# print(singleton is another_singleton)
#
# singleton.only_one_var = "I'm only one var"
# print(another_singleton.only_one_var)
#
# child = sgt.Child()
# print(child is singleton)
# print(child.only_one_var)

borg = sgt.Borg()
another_borg = sgt.Borg()
print(borg is another_borg)

child = sgt.Child()
borg.only_one_var = "I'm only one var"
print(child.only_one_var)

another_child = sgt.AnotherChild()
print(another_child.only_one_var)