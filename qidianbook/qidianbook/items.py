# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class QidianbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    tag_1 = Field()
    tag_2 = Field()
    qianming = Field()
    numbers_word = Field()
    dianjishu = Field()
    numbers_tuijian = Field()
    mulu = Field()
    introduce = Field()
    Tags = Field()
    author = Field()
    rongyu = Field()
    pinjie = Field()
    au_intro = Field()
    works_num = Field()
    zishu = Field()
    day = Field()
    zuopin_num = Field()


