# -*- coding: utf-8 -*-
import scrapy

## other modules
import sys
import csv
import time

from scrapy.spiders import Spider
from scrapy.selector import Selector


class StatspiderSpider(Spider):
    name = "statspider"
    allowed_domains = ["kickstarter.com"]
    start_urls = (
        'https://www.kickstarter.com/help/stats',
    )

    def parse(self, response):
        def scrape_table(xpath, rootdir):
            for i in range(1, 16):
                category = 'tr['+str(i)+']/'
                title = xpath.xpath(category+'td[1]/text()').extract()[0].encode("ascii", "ignore")
                f = open(rootdir + '/' + title + '.csv', 'ab')
                csvWriter = csv.writer(f)
                
                launched_proj = xpath.xpath(category+'td[2]/text()').extract()[0].encode("ascii", "ignore")
                column_1 = xpath.xpath(category+'td[3]/@data-table-value').extract()[0].encode("ascii", "ignore")
                column_2 = xpath.xpath(category+'td[4]/@data-table-value').extract()[0].encode("ascii", "ignore")
                column_3 = xpath.xpath(category+'td[5]/@data-table-value').extract()[0].encode("ascii", "ignore")
                column_4 = xpath.xpath(category+'td[6]/@data-table-value').extract()[0].encode("ascii", "ignore")
                column_5 = xpath.xpath(category+'td[7]/@data-table-value').extract()[0].encode("ascii", "ignore")
                column_6 = xpath.xpath(category+'td[8]/@data-table-value').extract()[0].encode("ascii", "ignore")
                
                title = unicode(title, "utf-8")
                launched_proj = unicode(launched_proj, "utf-8")
                column_1 = unicode(column_1, "utf-8")
                column_2 = unicode(column_2, "utf-8")
                column_3 = unicode(column_3, "utf-8")
                column_4 = unicode(column_4, "utf-8")
                column_5 = unicode(column_5, "utf-8")
                column_6 = unicode(column_6, "utf-8")
                
                item = [title, launched_proj, column_1,column_2,column_3,column_4,column_5,column_6]
                csvWriter.writerow(item)
                f.close()
                
        
        sel = Selector(response)
        
        rootdir = "/Users/haruyaishikawa/Desktop/Programming/scraping/kick_stats/dollars"
        dollars = sel.xpath('//*[@id="projects_and_dollars"]/div/table/tbody')
        
        scrape_table(dollars, rootdir)
            
        
        rootdir = "/Users/haruyaishikawa/Desktop/Programming/scraping/kick_stats/successful"
        successful = sel.xpath('//*[@id="successful_projects"]/div/table/tbody')
        
        scrape_table(successful, rootdir)
        

        

