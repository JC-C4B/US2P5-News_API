import requests
import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "jcxc4b@gmail.com"
    password = "GMAILAPPPASSWORD"

    receiver = "jcxc4b@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

topic = "techcrunch"

APIKey = "833159d37484469fa47c4f3650cce8fd"

url = "https://newsapi.org/v2/top-headlines?" \
    f"sources={topic}&" \
    "apiKey=833159d37484469fa47c4f3650cce8fd&" \
    "language=en"

# Making our request
request = requests.get(url)

#  Getting a dictionary with data
content = request.json()

#  Accessing the article titles and descriptions
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: TechCrunch Today" \
            + "\n" + body + article["title"] + "\n" \
            + article["description"] + "\n" \
            + article["url"] + 2*"\n"

body = body.encode("utf-8")
# Calling our send email function; leaving commented for now
# send_email(message=body)