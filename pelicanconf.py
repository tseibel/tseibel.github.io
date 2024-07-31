import os

AUTHOR = 'Trey Seibel'
SITENAME = 'Trey Seibel'
SITETITLE = 'My Personal Website'
SITEDESCRIPTION = "What am I up to now?"
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
#LINKS = (
#    ("github", "https://github.com/tseibel/"),
#    ("linkedin", "https://www.linkedin.com/in/trey-seibel/")
#)

# Social widget
SOCIAL = (
    ("github", "https://github.com/tseibel/"),
    ("linkedin", "https://www.linkedin.com/in/trey-seibel/")
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True