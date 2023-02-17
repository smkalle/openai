import requests
from bs4 import BeautifulSoup
import sys

# Make a request to the URL
# url = "https://www.example.com"
url = sys.argv[1]
page = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.content, "html.parser")

# Find all the text on the page
text = soup.get_text()

# Print the text
print(text)

f = open(sys.argv[2], 'w')
f.write(text)
f.close()

