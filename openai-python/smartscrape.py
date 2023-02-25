import sys
import requests
from bs4 import BeautifulSoup
import os
# import openai_secret_manager
import openai

# Usage: python smartscrape.py https://www.nytimes.com/2020/09/01/technology/elon-musk-tesla.html extracted_text.txt
# Check if arguments are passed

if len(sys.argv) < 3:
    print("Please pass the URL to scrape as an argument")
    print("Usage: python smartscrape.py <url> <extractfile>")
    sys.exit(1)

# Get the OpenAI API key from the environment variable
# openai_secrets = openai_secret_manager.get_secret("openai")

# Authenticate with the OpenAI API
# openai.api_key = openai_secrets["api_key"]
openai.api_key = os.environ["OPENAI_API_KEY"]


def scrape_and_summarize(url, extractfile):
    # Make a request to the URL and get the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the text from the page
    title = soup.find("title").get_text()
    about_author = soup.find("div", class_="author-about")
    if about_author:
        about_author = about_author.get_text()
    else:
        about_author = ""
    text = ""
    for paragraph in soup.find_all("p"):
        if paragraph.text == about_author:
            break
        text += paragraph.text + "\n"

    # Write the extracted text to a file
    with open(extractfile, "w", encoding="utf-8") as f:
        f.write(text)

    # Summarize the extracted text using OpenAI's GPT-3 API
    summary = openai.Completion.create(
        engine="davinci",
        prompt=f"Please summarize the following text:\n{text}",
        max_tokens=60,
    )

    # Print the summary
    print(f"Title: {title}")
    print(f"Summary: {summary.choices[0].text}")


if __name__ == "__main__":

    url = sys.argv[1]
    extractfile = sys.argv[2]
    scrape_and_summarize(url, extractfile)

