# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:36:53 2018

@author: Cristi
"""

import webbrowser
import scrapy
start_URLs=[]


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
# The url generator with the car specs
def _build_base_url(marca,model,caroserie,an_inceput,pret_maxim,km_maxim,capacitate_cilindrica_maxima):
    base_URL = ""
    base_URL = "https://www.autovit.ro/autoturisme/"+marca+"/"+model+"/"+caroserie+"/"+"de-la-"+an_inceput
    base_URL +="?search%5Bfilter_float_price%3Ato%5D="+pret_maxim+"&search%5Bfilter_float_mileage%3Ato%5D="+km_maxim
    base_URL +="&search%5Bfilter_float_engine_capacity%3Ato%5D="+capacitate_cilindrica_maxima+"&search%5Bcountry%5D="
    start_URLs.append(base_URL)
    return start_URLs
start_URLs = _build_base_url("volkswagen","passat","sedan","2002","3000","250000","2000")
webbrowser.open(start_URLs[0])

    

class CarSpider(scrapy.Spider):
    name = "car"
    #def start_request(self):
    #url = start_URLs[0]
   # url = "http://quotes.toscrape.com/"
   # start_urls = ['http://quotes.toscrape.com/tag/humor/']
    def parse(self, response):
            for quote in response.css('div.offer-item__content'):
                yield {
                    'text': car.css('a.text::text').extract_first(),
                    'author': quote.xpath('span/small/text()').extract_first(),
                }
    
            next_page = response.css('li.next a::attr("href")').extract_first()
            if next_page is not None:
                yield response.follow(next_page, self.parse)