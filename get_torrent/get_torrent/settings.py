# Scrapy settings for get_torrent project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

#################
# basic settings:
#################

BOT_NAME = 'get_torrent'

SPIDER_MODULES = ['get_torrent.spiders']

NEWSPIDER_MODULE = 'get_torrent.spiders'

DEFAULT_ITEM_CLASS = 'get_torrent.items.Website'

ITEM_PIPELINES = {
    'get_torrent.pipelines.FilterWordsPipeline': 1,
    'get_torrent.pipelines.FileWriterPipeline': 2
}

REDIRECT_MAX_TIMES = 20

ROBOTSTXT_OBEY = False

# people who will receive stats report after scrapy finishes.
STATSMAILER_RCPTS = []

URLLENGTH_LIMIT = 2083

# if you want to pretent that you are a browser, you should change this.
# USER_AGENT = 'Scrapy/YOUR_SCRAPY_VERSION'

EDITOR = 'vim'

###############
# AWS settings:
###############

AWS_ACCESS_KEY_ID = None

AWS_SECRET_ACCESS_KEY = None

#######################
# concurrency settings:
#######################

CONCURRENT_ITEMS = 100

CONCURRENT_REQUESTS = 16

CONCURRENT_REQUESTS_PER_DOMAIN = 8

CONCURRENT_REQUESTS_PER_IP = 0

#################
# depth settings:
#################

DEPTH_LIMIT = 0

DEPTH_PRIORITY = 0

DEPTH_STATS = True

DEPTH_STATS_VERBOSE = False

###############
# log settings:
###############

LOG_ENABLED = True

LOG_FILE = 'scrapy.log'

# LOG_LEVEL = 'DEBUG'
LOG_LEVEL = 'ERROR'

LOG_STDOUT = 'False'

#################
# debug settings:
#################

MEMDEBUG_ENABLED = False

# people who will receive memory debug report
MEMDEBUG_NOTIFY = []

##################
# memory settings:
##################

MEMUSAGE_ENABLED = False

MEMUSAGE_LIMIT_MB = 0

MEMUSAGE_NOTIFY_MAIL = False

MEMUSAGE_REPORT = False

MEMUSAGE_WARNING_MB = 0

####################
# download settings:
####################

RANDOMIZE_DOWNLOAD_DELAY = True

DOWNLOAD_DELAY = 2

###################
# cookies settings:
###################

COOKIES_ENABLED = True

COOKIES_DEBUG = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'get_torrent (+http://www.yourdomain.com)'
