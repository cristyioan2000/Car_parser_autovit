# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:36:53 2018

@author: Cristi
"""
import re
import webbrowser
import scrapy
from scrapy.crawler import CrawlerProcess
start_URLs=[]
page_number_div=""

"""
base_URL = "https://www.autovit.ro/autoturisme/volkswagen/passat/sedan
/de-la-2002/?search%5Bfilter_float_price%3Ato%5D=3000&search%5Bfilter_float_mileage
%3Ato%5D=250000&search%5Bfilter_float_engine_capacity%3Ato%5D=2000&search%5Bcountry%5D="
"""
"""
https://www.autovit.ro/autoturisme/volkswagen/passat/sedan/de-la-2002
/?search%5Bfilter_float_price%3Ato%5D=3000&search%5Bfilter_float_mileage%3Ato%5D=250000
&search%5Bfilter_float_engine_capacity%3Ato%5D=2000&search%5Bcountry%5D=
"""



'''
https://www.autovit.ro/autoturisme/volkswagen/passat/sedan/de-la-2002/
'''
# Generates start url using searching preferences
class Url_generator():
    def _build_base_url(marca,model,caroserie,an_inceput,pret_maxim,km_maxim,capacitate_cilindrica_maxima):
        base_URL = ""
        base_URL = "https://www.autovit.ro/autoturisme/"+marca+"/"+model+"/"+caroserie+"/"+"de-la-"+an_inceput
        base_URL +="?search%5Bfilter_float_price%3Ato%5D="+pret_maxim+"&search%5Bfilter_float_mileage%3Ato%5D="+km_maxim
        base_URL +="&search%5Bfilter_float_engine_capacity%3Ato%5D="+capacitate_cilindrica_maxima+"&search%5Bcountry%5D="
        start_URLs.append(base_URL)
        return start_URLs
    
urls = Url_generator._build_base_url("volkswagen","passat","sedan","1999","9000","250000","2000")
# Opens in the broswer the page
#webbrowser.open(start_URLs[0])



class CarSpider(scrapy.Spider):
    name = "car"
    max_page = ""
    page_url=""
    # starting link to parse
    start_urls = [urls[0]]
           
    def parse(self, response ): 
        page_number_div = response.css('ul.om-pager.rel li a')
        # the max page for the current search
        max_page = int(page_number_div.css('span::text').extract()[-1])
        if max_page>0:
            for i in range(max_page):
                if i == (max_page-1):
                    break
                page_url=urls[0]+"&page="+str(i+2)                                                    
                CarSpider.start_urls.append(page_url)
        # Fetching to parse each page
        for pages in CarSpider.start_urls:
          yield response.follow(pages, callback=self.link_parse)
          # breaking to take just the first page
          break
        # Fetching each post from each page
    def link_parse(self,response):
        for href in response.css('article'):
            link = href.css('div.offer-item__photo a::attr(href)').extract()[0]
            # printing all the links from the current page
           # yield{
            #        'link' : link
             #       }
            yield response.follow(link, self.parse_post)                
    def parse_post(self,response):
        #label_index = 0;
        for post in response.css('div.offer-params'):
            label = post.css('ul.offer-params__list li.offer-params__item span.offer-params__label::text').extract()
            label_value = post.css('ul.offer-params__list li.offer-params__item div.offer-params__value a.offer-params__link::text').extract()
            #for element in label_value:    
                #element.strip("\n")
            
            #to_print = [(l,lv) for l in label for lv in label_value]
          #  for l in label:
                # find label index and find the index of the value pair
                #label_index = index.label if label == l
               # yield {l: label_value[label_index]] , 
                #       }                   
            yield {
                    'label' : label,
                     'label_value' : label_value
                    }
          #  
           # yield{
                #   'label_value' : element
                 #   }
           # yield {
            #        'value_len' : len(label)
             #       }
        
           # label = response.follow.css('ul').extract()
               #div.offer-item__photo a::attr(href)
           
         
            #span.offer-params__label::text
                
    
          
