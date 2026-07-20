from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tags = soup.find_all(name="a", class_="storylink")
article_upvotes = soup.find_all(name="span", class_="score")

# Loop through each story tag and pull out what you need
article_texts = [tag.get_text() for tag in article_tags]
article_links = [tag.get("href") for tag in article_tags]
upvote_counts =[int(score.getText().split()[0]) for score in article_upvotes]

largest_number = max(upvote_counts)
largest_index = upvote_counts.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])