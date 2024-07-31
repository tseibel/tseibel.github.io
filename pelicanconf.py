import os

AUTHOR = 'Trey Seibel'
SITENAME = 'Personal Website'
SITEURL = ""

PATH = "content"

TIMEZONE = 'US/Central'
path = os.path.join(os.getenv('USERPROFILE'), 'pelican-themes')

THEME = path + '\Flex'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Github/tseibel", "https://github.com/tseibel/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True