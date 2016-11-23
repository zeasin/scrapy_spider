# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LkdbinitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HospitalCheckItem(scrapy.Item):
    title = scrapy.Field()
    remark = scrapy.Field()
    pass

class HosptailCheckPacakgeItem(scrapy.Item):
    title = scrapy.Field() #套餐标题
    image = scrapy.Field() #套餐图片
    feature = scrapy.Field() #套餐特色
    price = scrapy.Field() #套餐价格
    items = scrapy.Field()


