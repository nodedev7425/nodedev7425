
import requests
import xml.etree.ElementTree as ET

RSS_URL = "https://medium.com/feed/@buelenard"

rss = requests.get(RSS_URL).text
root = ET.fromstring(rss)

items = root.findall("./channel/item")[:3]

stories = []
for item in items:
    title = item.find("title").text
    link = item.find("link").text
    stories.append(f"- [{title}]({link})")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start = "<!-- MEDIUM-STORIES:START -->"
end = "<!-- MEDIUM-STORIES:END -->"

new_content = (
    start + "\n"
    + "\n".join(stories)
    + "\n" + end
)

before = readme.split(start)[0]
after = readme.split(end)[1]

updated = before + new_content + after

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
