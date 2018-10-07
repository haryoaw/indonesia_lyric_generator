# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class LyricScrapperSpider(CrawlSpider):
    name = 'lyric_scrapper'
    allowed_domains = ['lirik.kapanlagi.com']
    start_urls = ['https://lirik.kapanlagi.com/lagu/a_id']
    rules = (Rule(LinkExtractor(allow=(), restrict_css=(".pagination2 ul li a",".col-lirik .div-horizontal2-list a", "div .letterLinksAnchor")), callback="parse_page", follow=True),)
    def parse_page(self, response):
        song = response.css('.col-lirik').extract_first()
        title= response.css('.head-lirik h5::text').extract_first()
        if len(title) > 0 and len(song) > 0:
scraped_info = {
            'song' : song,
            'title' : title,
        }
yield scraped_info
