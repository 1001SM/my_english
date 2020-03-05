import chardet
import requests
from bs4 import BeautifulSoup

url = r'https://progeigo.org/learning/essential-words-600-plus/'
r = requests.get(url)

print(r.status_code)
print(type(r.text))
print(type(r.content))
print(r.encoding)

soup = BeautifulSoup(r.content, 'lxml',from_encoding='utf-8')
# soup.encoding = 'shift_jis'
# print(soup)

# words_class = soup.find_all("table", class_="wp-block-table")
# words_tbody = [word for word in words_class]
# print(word_tbody)

text_file = open("test.txt", "wt")


words = soup.select('tbody tr td')
#post-57 > div > table:nth-child(12) > tbody > tr:nth-child(1) > td:nth-child(1)

for word in words:
    print(word.get_text())
    text_file.write((word.get_text()))

text_file.close()

