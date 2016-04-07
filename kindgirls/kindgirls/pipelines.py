# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy

from scrapy.exceptions import DropItem

class KindgirlsPipeline(object):
    def process_item(self, item, spider):
        if item['image_urls']:
            print '1'
        else:
            raise DropItem("Missing price in %s" % item)
        # yield scrapy.Request(item['image_urls'])
        # return item
