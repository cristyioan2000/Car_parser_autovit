# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:36:53 2018

@author: Cristi
"""

import webbrowser
import scrapy
from scrapy.crawler import CrawlerProcess
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



'''
https://www.autovit.ro/autoturisme/volkswagen/passat/sedan/de-la-2002/
'''
# The url generator with the car specs
class Url_generator():
    def _build_base_url(marca,model,caroserie,an_inceput,pret_maxim,km_maxim,capacitate_cilindrica_maxima):
        base_URL = ""
        base_URL = "https://www.autovit.ro/autoturisme/"+marca+"/"+model+"/"+caroserie+"/"+"de-la-"+an_inceput
        base_URL +="?search%5Bfilter_float_price%3Ato%5D="+pret_maxim+"&search%5Bfilter_float_mileage%3Ato%5D="+km_maxim
        base_URL +="&search%5Bfilter_float_engine_capacity%3Ato%5D="+capacitate_cilindrica_maxima+"&search%5Bcountry%5D="
        start_URLs.append(base_URL)
        return start_URLs
   # def page_number:
   #def url_gen(marca,moel,caroserie,an_inceput):
        
       
#start_URLs = _build_base_url("volkswagen","passat","sedan","2002","3000","250000","2000")
urls = Url_generator._build_base_url("volkswagen","passat","sedan","2002","3000","250000","2000")

#webbrowser.open(start_URLs[0])


    

class CarSpider(scrapy.Spider):
    start_urls = [urls[0]]
    name = "car"
    def parse(self, response ):
        for car in response.css('article'):
            yield {
                'item': car.css('a.offer-title__link::text').extract()
                }
        
            

      
