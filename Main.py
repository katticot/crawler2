import urllib

import bs4

# help(bs4)

#import the library used to query a website
import urllib2
#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
wiki2="http://www.welcometofrance.com/en/you-are-an-employee-your-employer-is-outside-france"
#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki2)
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page,"html.parser")

#print soup.prettify()

ref = soup.a
soup.a.string
all_tables=soup.find_all("a")
or

print all_tables