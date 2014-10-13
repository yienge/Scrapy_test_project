# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Website(Item):
    name = Field()
    description = Field()
    url = Field()
    date = Field()


class Page(Item):
    name = Field()
    description = Field()
    url = Field()
    date = Field()
    size = Field()
