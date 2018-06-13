from bs4 import BeautifulSoup
import urllib.request
import os


url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India" #defining the url
source_code = urllib.request.urlopen(url) #storing the content of url in source code
plain_text = source_code                  #getting plain text  from the content ie. accessing required info from all the info
soup = BeautifulSoup(plain_text, "html.parser") #parsing is nothing but extracting info like title, heading
print(soup.title.text)
print(soup.find_all('a'))                      #extracting all anchor tags
for links in soup.find_all('a'):               #we define a hyperlink with < a href="link"> here we are accessing all the links which are in <a> tag
    print(links.get('href'))
table=soup.find("table",{"class":"wikitable sortable plainrowheaders"}) #finding a table with the class name
for row in table.find_all('tr'):                                        #finding all the rows from the table
   for columns in row.find_all('td'):                                    #finding all the columns in a row
      print(columns)
   print(row.find('th'))