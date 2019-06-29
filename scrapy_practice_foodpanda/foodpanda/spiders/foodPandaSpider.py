# -*- coding: utf-8 -*-
import scrapy

cityDict = {'taipei' : 'taipei-city',
            'taoyuan' : 'taoyuan-city',
            'newTaipei' : 'new-taipei-city',
            'taichung' : 'taichung-city',
            'kaohsiung' : 'kaohsiung-city',
            'hsinchu' : 'hsinchu-city',
            'keelung': 'keelung',
            'tainan' : 'tainan-city',
            'miaoli' : 'miaoli-county'}

class FoodpandaspiderSpider(scrapy.Spider):
    name = 'foodPandaSpider'
    allowed_domains = ['https://www.foodpanda.com.tw/']
    print("Which city do you want to send meal to?")
    city_name = input("City Name:")
    if ('桃園' in city_name.lower()) or ('taoyuan' in city_name.lower()):
        url = cityDict['taoyuan']
    elif '臺北' in city_name.lower() or '台北' in city_name.lower() or 'taipei' in city_name.lower():
        url = cityDict['taipei']
    elif '新北' in city_name.lower() or 'new taipei' in city_name.lower():
        url = cityDict['newTaipei']
    elif '臺中' in city_name.lower() or '台中' in city_name.lower() or 'taichung' in city_name.lower():
        url = cityDict['taichung']
    elif '高雄' in city_name.lower() or 'kaohsiung' in city_name.lower():
        url = cityDict['kaohsiung']
    elif '新竹' in city_name.lower() or 'hsinchu' in city_name.lower():
        url = cityDict['hsinchu']
    elif '基隆' in city_name.lower() or 'keelung' in city_name.lower():
        url = cityDict['keelung']
    elif '臺南' in city_name.lower() or '台南' in city_name.lower() or 'tainan' in city_name.lower():
        url = cityDict['tainan']
    elif '苗栗' in city_name.lower() or 'miaoli' in city_name.lower():
        url = cityDict['miaoli']
    else:
        print("......")

    print(city_name.lower())
    start_urls = ['https://www.foodpanda.com.tw/city/' + url]
    print(start_urls)

    def parse(self, response):
        data = response.xpath('//a[@class="hreview-aggregate url"]')
#        print(data)
        for restaurants in data:
            restaurant_name = restaurants.xpath('.//figure[@class="vendor-tile  item"]/figcaption/span[@class="headline"]/span[@class="name fn"]/text()').extract_first()
            restaurant_feature = restaurants.xpath('.//figure[@class="vendor-tile  item"]/figcaption/ul[@class="categories summary"]/li[@class="vendor-characteristic"]/span/text()').extract_first()
            restaurant_relative_url = restaurants.xpath('.//@href').extract_first()
            restaurant_absolute_url = response.urljoin(restaurant_relative_url)
            
            yield{'Name' : restaurant_name, 'Feature' : restaurant_feature, 'URL' : restaurant_absolute_url}

            print('Name:' + str(restaurant_name))
            print('Feature:' + str(restaurant_feature))
            print('Url:' + str(restaurant_absolute_url) + '\n')

