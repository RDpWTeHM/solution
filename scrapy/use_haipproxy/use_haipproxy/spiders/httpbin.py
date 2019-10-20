# -*- coding: utf-8 -*-
import json
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print("httpbin.org/ip: '{}'".format(json.loads(response.text)))

