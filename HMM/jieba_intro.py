# !/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import jieba
import jieba.posseg


if __name__ == "__main__":
    f = open('.\\res\\novel.txt', 'rb')
    str = f.read().decode('utf-8')
    f.close()

    seg = jieba.posseg.cut(str)
    for s in seg:
        print(s.word, s.flag, '|',)
        # print s.word, '|',
