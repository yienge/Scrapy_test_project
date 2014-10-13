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

EDITOR = 'vim'

CLOSESPIDER_PAGECOUNT = 1000

CLOSESPIDER_TIMEOUT = 3600

BOT_NAME = 'get_torrent'

SPIDER_MODULES = ['get_torrent.spiders']

NEWSPIDER_MODULE = 'get_torrent.spiders'

DEFAULT_ITEM_CLASS = 'get_torrent.items.Website'

ITEM_PIPELINES = {
    'get_torrent.pipelines.FilterWordsPipeline': 1,
}

REDIRECT_MAX_TIMES = 20

ROBOTSTXT_OBEY = False

URLLENGTH_LIMIT = 2083

# people who will receive stats report after scrapy finishes.
STATSMAILER_RCPTS = []


#############################
# random user agent settings:
#############################

# if you want to pretent that you are a browser, you should change this.
# and rotate the user-agent with different browser can avoid getting banned.
DOWNLOADER_MIDDLEWARES = {
    'get_torrent.middleware.RandomUserAgent': 1,
}

# default browser UA string
# USER_AGENT = 'Scrapy/YOUR_SCRAPY_VERSION'

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'get_torrent (+http://www.yourdomain.com)'

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

# LOG_ENABLED = True

# LOG_FILE = 'scrapy.log'

# LOG_LEVEL = 'DEBUG'
# LOG_LEVEL = 'ERROR'

# LOG_STDOUT = 'False'


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

# increase download delay can avoid getting banned.
DOWNLOAD_DELAY = 2


###################
# cookies settings:
###################

# disable cookies can avoid getting banned.
COOKIES_ENABLED = True

COOKIES_DEBUG = True
