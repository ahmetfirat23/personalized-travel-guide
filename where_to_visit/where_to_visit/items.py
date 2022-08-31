# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WhereToVisitItem(scrapy.Item):
    # define the fields for your item here like:
    city_name = scrapy.Field()
    attraction_name = scrapy.Field()
    rating = scrapy.Field()
    image_url = scrapy.Field()
    reviews = scrapy.Field()
    about = scrapy.Field()

