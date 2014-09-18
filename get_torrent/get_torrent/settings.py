# Scrapy settings for get_torrent project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'get_torrent'

SPIDER_MODULES = ['get_torrent.spiders']

NEWSPIDER_MODULE = 'get_torrent.spiders'

DEFAULT_ITEM_CLASS = 'get_torrent.items.Website'

ITEM_PIPELINES = {
    'get_torrent.pipelines.FilterWordsPipeline': 1,
    'get_torrent.pipelines.FileWriterPipeline': 2
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'get_torrent (+http://www.yourdomain.com)'
