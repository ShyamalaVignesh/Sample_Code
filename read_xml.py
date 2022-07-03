
import xml
# Reading the data inside the xml
# file to a variable under the name
# data
#install pip3 install lxml

from bs4 import BeautifulSoup

with open('test_demo.xml', 'r') as f:
    data = f.read()

# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object
Bs_data = BeautifulSoup(data, features="xml")

# Finding all instances of tag
# `unique`
name = Bs_data.find_all('name')
print(name)
