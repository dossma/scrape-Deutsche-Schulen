# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import logging

#
# class PagecrawlerPipeline(object):
#     def process_item(self, item, spider):
#         item['firmenname'] = item['firmenname']
#         # logging.DEBUG("item['strasse'] %s" % item['strasse'])
#
#         # item['strasse'] = item['strasse'].replace(" ", "")
#         # item['strasse'] = item['strasse'].replace("\n", "")
#         item['strasse'] = item['strasse'].strip()
#
#         # item['ort'] = item['ort'].replace(" ", "")
#         # item['ort'] = item['ort'].replace("\n", "")
#         item['ort'] = item['ort'].strip()
#
#         # item['plz'] = item['plz'].replace(" ", "")
#         # item['plz'] = item['plz'].replace("\n", "")
#         item['plz'] = item['plz'].strip()
#
#         # item['website'] = item['website'].replace(" ", "")
#         # item['website'] = item['website'].replace("\n", "")
#         item['website'] = item['website'].strip()
#
#         # item['land'] = item['land'].replace(" ", "")
#         # item['land'] = item['land'].replace("\n", "")
#         item['land'] = item['land'].strip()
#
#         if item['telefon']:
#             # item['telefon'] = item['telefon'].replace(" ", "")
#             # item['telefon'] = item['telefon'].replace("\n", "")
#             item['telefon'] = item['telefon'].strip()
#
#         # item['email'] = item['email'].strip()
#
#         return item
