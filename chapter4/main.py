# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/11
# Copyright (C) 2020, Centum Factorial all rights reserved.
from chapter4.weather import Facade

if __name__ == '__main__':
    facade = Facade()
    # print(f"Seoul, KR: {facade.get_forecast('Seoul', 'KR')}")
    print(f"London, UK: {facade.get_forecast('London', 'UK')}")

