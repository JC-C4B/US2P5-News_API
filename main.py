import requests

APIKey = "833159d37484469fa47c4f3650cce8fd"

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=833159d37484469fa47c4f3650cce8fd"

# Making our request
request = requests.get(url)

#  Getting a dictionary with data
content = request.json()

#  Accessing the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])