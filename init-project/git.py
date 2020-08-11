# Created by Yoo Ju Jin(jujin@100fac.com) 
# Created Date : 2020/08/11
# Copyright (C) 2020, Centum Factorial all rights reserved.
import os


def create_branch(name: str):
    os.system(f'git branch {name}')


def create_chapter_branches(start: int, end: int):
    for number in range(start, end + 1):
        create_branch(f'feature/chapter{number}')


if __name__ == '__main__':
    create_chapter_branches(5, 7)
