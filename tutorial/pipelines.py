# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class Bxwx9Pipeline(object):
    def process_item(self, item, spider):
        path = os.getcwd() + '-'.join(('\\home\\lonki\\pythonspider\\books\\' + item['novel_name'] + '\\').split())
        if (os.path.exists(path) == False):
            os.makedirs(path)  # 创建多级文件夹目录
        file_name = path + '-'.join((item['novel_title'] + '.txt').split())

        with open(file_name, mode='w', encoding='utf-8') as f:
            print(item['novel_name'], file=f)
            print(item['novel_author'], file=f)
            print(item['novel_title'], file=f)
            print(item['novel_content'], file=f)
            return item