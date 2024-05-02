from bs4 import BeautifulSoup
import lxml
import requests

#-----Request for YC Webpage Logic-----#
response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
yc_web_page = response.text
#-----Soup Logic-----#
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_tags = soup.find_all(name="span", class_="titleline")
article_texts = [article_tag.a.getText() for article_tag in article_tags]
#article_text = article_tag.a.getText()
#article_link = article_tag.a.get('href')
article_links = [article_tag.a.get('href') for article_tag in article_tags)]
article_upvotes = soup.find_all(name='span', class_="score").getText()

print(article_texts)
print(article_links)
print(article_upvotes)

#article_text = article_tag.getText()
#header_title = soup.select_one(selector='.athing .title span a')
#print(header_title)




'''
with open('./website.html', encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

company_url = soup.select_one(selector="p a")
print(company_url)
'''