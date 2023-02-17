

import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

#url = 'http://www.gutenberg.org/files/2591/2591-h/2591-h.htm'
url = sys.argv[1]

page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text)

# write to file
f = open(sys.argv[2], 'w')
f.write(text)
f.close()
