# coding=utf-8
# auther:wangc
# 2020-08-28

import csv

with open("../static/features_all.csv") as f:
    res = csv.reader(f)
    for row in res:
        print(row)
        print(len(row))