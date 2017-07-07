# -*- coding: utf-8 -*-
#起点男女频VIP小说爬取
import scrapy
from scrapy.http import Request
from qidianbook.items import QidianbookItem



class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']

    start_urls = ['http://a.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&page={}&month=-1&style=1&action=-1&vip=1'.format(m) for m in range(1160)] + [
                'http://a.qidian.com/mm?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&page={}&month=-1&style=1&action=-1&vip=1'.format(n) for n in range(1437)]

    def parse(self, response):
        post_urls = response.css('.book-mid-info h4 a::attr(href)').extract()
        for po_url in post_urls:
            post_url = 'http:'+po_url
            yield Request(url=post_url,callback=self.parse_detail)

    def parse_detail(self,response):
        item = QidianbookItem ()
        item['title'] = response.css('.book-info h1 em::text').extract()
        item['tag_1'] = response.css('.tag span::text').extract()
        item['tag_2'] = response.css('.tag a::text').extract()
        item['qianming'] = response.css('.intro::text').extract()
        item['numbers_word'] = response.css('.book-info p em::text').extract()[0]
        item['dianjishu'] = response.css('.book-info p em::text').extract()[1]
        item['numbers_tuijian'] = response.css('.book-info p em::text').extract()[2]
        item['mulu'] = response.css('#J-catalogCount::text').extract()
        ab = response.css('.book-intro p::text').extract()
        item['introduce'] = ''.join(ab).strip()
        item['Tags'] = response.css('.tag-wrap a::text').extract()
        item['author'] = response.css ( '.writer::text' ).extract ()
        item['rongyu'] = response.css('.detail strong::text').extract()
        item['pinjie'] = response.css('.author-photo span::text').extract()
        cd = response.css('.info-wrap.nobt p::text').extract()
        item['au_intro'] = ''.join(cd).strip()
        item['works_num'] = response.css('.work-state.cf li em ::text').extract()[0]
        item['zishu'] = response.css('.work-state.cf li em ::text').extract()[1]
        item['day'] = response.css('.work-state.cf li em ::text').extract()[2]
        item['zuopin_num'] = response.css('.text h4 a::text').extract()
        yield item




