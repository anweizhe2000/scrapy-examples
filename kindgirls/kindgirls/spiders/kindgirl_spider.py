# -*- coding: utf-8 -*-

#
#

import scrapy

from kindgirls.items import KindgirlsItem

class KindgirlsPictureSpider(scrapy.Spider):
    name = "kgpic"
    allowed_domains = ["kindgirls.com"]
    start_urls = [
        "http://www.kindgirls.com/girls/?i=a"
    ]

    def parse(self, response):
        items = []
        for div in response.xpath("//div[@class='model_list']"):
            girlPic = "http://www.kindgirls.com" + div.xpath("a/img/@src").extract()[0]
            item = KindgirlsItem()
            item['image_urls'] = girlPic
            items.append(item)

        return items

