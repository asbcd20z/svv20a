#!/usr/bin/python
# -*- coding: utf-8 -*-
#date:2017-10-07
##https://blog.csdn.net/sunchengquan/article/details/78170569
##https://www.cnblogs.com/mzc1997/p/7813801.html
__author__ = 'sunchengquan'
__project__ = 'XXXXXX'
__doc__ = 'XXXXXX'
__mail__ ='1641562360@qq.com'

#import pdb; pdb.set_trace()
import re #正则表达式需要的包
import json #解析json数据需要的包
import requests

url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=552369102522&spuId=853893286&sellerId=701751992&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvv9vJvJgvUpCkvvvvvjiPP2SWljn8nLLhsjrCPmPhzjt8PLqw6jDUR2SW6jiURIhCvCLNqtoaWxdNzA2kZM1wCYM1zQjwQUhCvvsNvVxYZDdNzAmkraACvpvWzQmDSxE4zYG97u5wdphvmpvZEQfH1oLg4FyCvvpvvvvvRphvCvvvvvmCvpvWzQ2HcPB4zYG9RBdwdphvmpvZmpEd4AoZj86Cvvyvm8GmwzWwEBVrvpvBUvQT940rHEHx84GuUZWE3wervpvEvv2Q9fAG2mqYiQhvCvvv9UUCvpvVvmvvvhCvmphvLvkD69vjcWL9a4QB%2BFZc%2BEj6sCywJxcXS47BhC3qVUcnDOmOezIUDajxALwpEcqhtjc6eX1z7tj61WkfV7Q4S47B9CkaU6bnDO2hjC0tvpvIvvvvvhCvvvvvvUUdphvv%2B9vv9krvpvQvvvmm86CvmVWvvUUsphvUIgyCvvOWvvVvaZRivpvUvvmvbqZr%2F%2FZPvpvhJ2X572yCvvpvvvvv3QhvCvvhvvmrvpvBUv9wvyCvvWMD84GuUZWE3wervpvEvvASvFwzCm7kdphvmpvUfpUhCCQiPT6Cvvyv22UmwjvwXN%2FrvpvEvvsKv3O7EjvE9phv2nGv1xQ07rMNUhybzUhCvvsNvWxGaldNzACBIaQtvpvhvvvvvUhCvvsNvmXazxdNzA2XZnACvpvWzQmDSB34zYG975dw&isg=Ag4O1UVS26FtwG4En5NuROh9XuQQJ7YR1hBPrjhRe5DJm471oBzumTMZpfwJ&needFold=0&_ksTS=1507359613080_4232&callback=jsonp4233';
web_content = requests.get(url).text # 获取网页中json数据
content = re.findall(r'\w+[(]{1}(.*)[)]{1}',web_content,re.S)# 正则表达式除去网页中json数据多余的部分
python_content = json.loads(content[0])
count = len(python_content['rateDetail']['rateList'])#获取用户评论数（这里只是当前页的）
for i in range(count):
    print(python_content['rateDetail']['rateList'][i]['rateContent'])

