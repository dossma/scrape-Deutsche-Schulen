# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PagecrawlerItem(scrapy.Item):

    Name = scrapy.Field()
    AP = scrapy.Field()
    Funktion = scrapy.Field()
    Telefon = scrapy.Field()
    Mail = scrapy.Field()
    Adresse = scrapy.Field()
    website = scrapy.Field()
    Schuljahresbeginn = scrapy.Field()



