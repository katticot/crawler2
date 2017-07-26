import urllib

import bs4

# help(bs4)


url_ligue_1 = "https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2016-2017"

from urllib2 import Request
request_text = Request.get_full_url(url_ligue_1).read()
print(request_text[:1000])
