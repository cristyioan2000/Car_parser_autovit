'''
1.Anaconda promt -> scrapy startproject -name-
2.Create spider in the project folder in spider folder
3.Anaconda promt -> scrapy crawl -crawler_name- (In the example 'car')
'''
# -*- coding: utf-8 -*-
"""
UPDATED on Wed Aug  1 21:36:53 2018

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
    name = "car"
    def start_requests(self):
            for url in urls:
                yield scrapy.Request(url=url,callback = self.parse)
                    
    def parse(self,response):
        filename = 'html_page.html'
        with open(filename,'wb') as outfile:
            outfile.write(response.body)
            self.log('Saved file %s' % filename)
