# access api and parse array of json objects
import json
import urllib.request
import sys

url = sys.argv[1]
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('Count:', len(info))
sum = 0
print(info)
for item in info:
    print(item, ":", info[item])




