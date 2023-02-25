import requests
import json
import os
import sys
import time
import datetime
import logging
import logging.handlers
import argparse
import configparser
import re
import urllib
import urllib.request
import urllib.parse

from medium_api import Medium
api_key = os.getenv("RAPID_API_KEY")
print(api_key)
medium = Medium(api_key)

user = medium.user(username="nishu-jain")

print(f'{user.fullname} has {user.followers_count} followers.')

user.fetch_articles()
for article in user.articles:
        print(article.title)
