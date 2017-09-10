# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import matplotlib.pyplot as plt
import sys
import seaborn as sns
import json


class ReviewsPipeline(object):
    def __init__(self):
        self.id = 1
        self.file = open('YuHsiang_Tsai_cdr.jl', 'wb')
        self.sizes = []

    def process_item(self, item, spider):
        # if (self.id <= 50):
        item['doc_id'] = self.id
        line = json.dumps(item) + "\n"
        self.file.write(line)

        response_body = item['raw_content']
        self.sizes.append(sys.getsizeof(response_body))
        self.id = self.id + 1
        return item

    def close_spider(self, spider):
        self.file.close()
        sns_plot = sns.distplot(self.sizes, axlabel='size(B)')
        fig = sns_plot.get_figure()
        print("total crawl page: " + str(self.id))
        fig.savefig("output.png")


